import struct

class Operand:
    def __init__(self, type, value, disp=0, base=None, index=None, scale=1):
        self.type = type # REGISTER, IMMEDIATE, MEMORY, LABEL
        self.value = value # reg_name, imm_value, etc.
        # Memory specific
        self.disp = disp
        self.base = base
        self.index = index
        self.scale = scale

class Encoder:
    def __init__(self):
        self.symbol_table = {}
        self.current_offset = 0

    def _parse_operands(self, raw_groups):
        parsed = []
        for group in raw_groups:
            if not group: continue
            
            # Case 1: Single Token
            if len(group) == 1:
                t = group[0]
                if t.type == "REGISTER":
                    parsed.append(Operand("REGISTER", t.value))
                elif t.type == "IMMEDIATE":
                    parsed.append(Operand("IMMEDIATE", t.value))
                elif t.type == "IDENTIFIER" or t.type == "LABEL":
                    parsed.append(Operand("IDENTIFIER", t.value))
                else:
                    # Unknown single token? probably symbol [ or ]
                    # Checking for [ reg ]
                    if t.value == "[": 
                         # Might be start of memory, handled in complex case?
                         # For now assume single token is not memory unless implicit
                         pass
            
            # Case 2: Memory / Complex Expression
            else:
                # Check for [ ... ]
                if group[0].value == "[" and group[-1].value == "]":
                    # It is Memory!
                    # Parse Content: group[1:-1]
                    mem_op = self._parse_memory_expression(group[1:-1])
                    parsed.append(mem_op)
                else:
                    # Maybe "OFFSET label" or just garbage
                    pass
        return parsed

    def _parse_memory_expression(self, tokens):
        # Parses [base + index*scale + disp]
        base = None
        index = None
        scale = 1
        disp = 0
        
        # State machine or ad-hoc? Ad-hoc is fine for simple expressions.
        # Collect all parts
        parts = []
        current_sign = 1
        
        k = 0
        while k < len(tokens):
            t = tokens[k]
            
            if t.type == "SYMBOL":
                if t.value == "+": current_sign = 1
                elif t.value == "-": current_sign = -1
                elif t.value == "*": 
                    # Scale applied to previous register?
                    # This parsers is too simple. Let's look back or forward.
                    if k > 0 and tokens[k-1].type == "REGISTER" and k+1 < len(tokens) and tokens[k+1].type == "IMMEDIATE":
                         # Reg * Scale
                         # We already added Reg as base or index, need to fix it.
                         # If we just saw a register, pop it from 'parts' list or re-classify it?
                         scale_val = tokens[k+1].value
                         if index is None and base == tokens[k-1].value:
                             # Convert base to index
                             index = base
                             base = None
                             scale = scale_val
                             # Skip next token
                             k += 1 
                         elif index == tokens[k-1].value:
                             scale = scale_val
                             k += 1
                k += 1
                continue
            
            if t.type == "REGISTER":
                # Is it Base or Index?
                if base is None: base = t.value
                elif index is None: index = t.value
                else: raise ValueError("Too many registers in memory operand")
            
            elif t.type == "IMMEDIATE":
                # Check for scale * Reg case (Imm * Reg)
                if k+1 < len(tokens) and tokens[k+1].value == "*" and k+2 < len(tokens) and tokens[k+2].type == "REGISTER":
                     scale = t.value
                     index_reg = tokens[k+2].value
                     if index is None: index = index_reg
                     k += 2
                else:
                    disp += (t.value * current_sign)
            
            k += 1
            
        return Operand("MEMORY", None, base=base, index=index, scale=scale, disp=disp)


    def encode(self, tokens):
        """
        Two-Pass Assembly:
        1. Calculate offsets and build Symbol Table.
        2. Generate Machine Code using symbols.
        """
        # PASS 1: Symbol Discovey & Size Calculation
        self.current_offset = 0
        self.symbol_table = {}
        self._run_pass(tokens, build_symbols=True)
        
        # PASS 2: Code Generation
        self.current_offset = 0
        return self._run_pass(tokens, build_symbols=False)

    def _run_pass(self, tokens, build_symbols):
        machine_code = bytearray()
        
        i = 0
        while i < len(tokens):
            token = tokens[i]
            
            if token.type == "LABEL":
                if build_symbols:
                    self.symbol_table[token.value] = self.current_offset
                i += 1
                continue
                
            if token.type == "OPCODE":
                op = token.value
                
                # Fetch operands (Group by comma)
                raw_operand_tokens = []
                current_op_tokens = []
                
                j = i + 1
                while j < len(tokens) and tokens[j].type != "NEWLINE":
                    t = tokens[j]
                    if t.type == "SYMBOL" and t.value == ",":
                         # End of current operand
                         if current_op_tokens:
                             raw_operand_tokens.append(current_op_tokens)
                             current_op_tokens = []
                    else:
                         current_op_tokens.append(t)
                    j += 1
                
                # Append last operand
                if current_op_tokens:
                    raw_operand_tokens.append(current_op_tokens)
                
                # Parse Operands (Convert token lists to logical Operand objects)
                parsed_operands = self._parse_operands(raw_operand_tokens)
                
                # Generate Bytes (or just calculate size)
                instr_bytes = self._encode_instruction(op, parsed_operands, build_symbols)
                
                if not build_symbols:
                    machine_code.extend(instr_bytes)
                
                self.current_offset += len(instr_bytes)
                i = j # Skip operandstokens
            else:
                i += 1
                
        return machine_code

    def _encode_instruction(self, op, operands, build_symbols):
        # Directives (Ignored for Flat Binary for now)
        if op in ["section", "global", "db"]:
            return b''

        # Dispatcher
        if op == "mov":      return self._encode_mov(operands)
        elif op == "add":    return self._encode_add(operands)
        elif op == "sub":    return self._encode_sub(operands)
        elif op == "syscall": return b'\x0F\x05'
        elif op == "jmp":    return self._encode_jump(0xEB, operands, build_symbols) # JMP rel8
        elif op == "je":     return self._encode_jump(0x74, operands, build_symbols) # JE rel8
        elif op == "jne":    return self._encode_jump(0x75, operands, build_symbols) # JNE rel8
        elif op == "syscall":return b'\x0F\x05' # SYSCALL
        elif op == "int":    return self._encode_int(operands)
        
        # SIMD Instructions (SSE)
        elif op == "movaps": return self._encode_simd(0x28, operands) # MOVAPS xmm1, xmm2/m128
        elif op == "addps":  return self._encode_simd(0x58, operands) # ADDPS xmm1, xmm2/m128
        elif op == "subps":  return self._encode_simd(0x5C, operands) # SUBPS
        
        return b'' # Parsing error handled elsewhere or NOP

    def _encode_simd(self, opcode_byte, operands):
        # Encodes standard SSE instruction: 0F <opcode> /r
        # Assumes operands are [xmm, xmm] or [xmm, mem]
        if len(operands) != 2: return b''
        dest = operands[0]
        src = operands[1]
        
        # Helper to parse xmmN -> integer N
        def get_xmm_id(name):
            if name.startswith("xmm"): return int(name[3:])
            if name.startswith("ymm"): return int(name[3:]) # Treat as same ID for VEX later
            return -1

        dest_id = get_xmm_id(dest.value)
        if dest_id == -1: return b'' # Dest must be XMM
        
        # Prefix 0F
        prefix = b'\x0F'
        
        if src.type == "REGISTER":
             src_id = get_xmm_id(src.value)
             if src_id == -1: return b''
             
             # ModRM (Mode 11 for Reg-Reg)
             mod = 0b11
             modrm = (mod << 6) | (dest_id << 3) | src_id
             return prefix + struct.pack("B", opcode_byte) + struct.pack("B", modrm)

        elif src.type == "MEMORY":
             # TODO: Re-use ModRM logic!
             # For now, simple [Reg] only to prove point
             reg_map = {"rax": 0, "rcx": 1, "rdx": 2, "rbx": 3, "rsp": 4, "rbp": 5, "rsi": 6, "rdi": 7}
             if src.base in reg_map:
                 base_id = reg_map[src.base]
                 mod = 0b00 # [rax]
                 modrm = (mod << 6) | (dest_id << 3) | base_id
                 return prefix + struct.pack("B", opcode_byte) + struct.pack("B", modrm)
        
        return b''

    def _encode_int(self, operands):
        # INT imm8 (CD ib)
        if len(operands) == 1 and operands[0].type == "IMMEDIATE":
            imm = operands[0].value
            return b'\xCD' + struct.pack("B", imm)
        return b''

    def _encode_mov(self, operands):
        if len(operands) != 2: return b''
        dest = operands[0]
        src = operands[1]

        reg_map = {"rax": 0, "rcx": 1, "rdx": 2, "rbx": 3, "rsp": 4, "rbp": 5, "rsi": 6, "rdi": 7}

        # Case 1: MOV REG, IMM64 (Existing)
        if dest.type == "REGISTER" and src.type == "IMMEDIATE":
             if dest.value in reg_map:
                reg_idx = reg_map[dest.value]
                opcode = 0xB8 + reg_idx
                return b'\x48' + struct.pack("B", opcode) + struct.pack("<Q", src.value)
        
        # Case 2: MOV REG, MEM ([reg])
        # Opcode: 8B /r
        if dest.type == "REGISTER" and src.type == "MEMORY":
             if dest.value in reg_map and src.base in reg_map:
                  # REX.W + 8B + ModRM
                  # ModRM: Mod(2) Reg(3) RM(3)
                  # Mode 00 (No disp), Mode 01 (Disp8), Mode 10 (Disp32)
                  
                  reg_code = reg_map[dest.value]
                  rm_code = reg_map[src.base]
                  
                  # Logic for SIB:
                  # If index is present OR base is RSP/R12, we need SIB.
                  reg_code = reg_map[dest.value]
                  
                  base_code = reg_map[src.base] if src.base else 5 # 5=RBP/Disp32 only if mod=00
                  index_code = reg_map[src.index] if src.index else 4 # 4=None (RSP)
                  
                  # Verify Scale
                  scale_map = {1: 0, 2: 1, 4: 2, 8: 3}
                  ss = scale_map.get(src.scale, 0)
                  
                  need_sib = (src.index is not None) or (base_code == 4) # 4 is RSP
                  
                  if need_sib:
                      # ModRM.rm = 4 indicates SIB follows
                      rm_field = 4
                      sib_byte = (ss << 6) | (index_code << 3) | base_code
                      
                      # Mod Logic
                      if src.disp == 0 and base_code != 5:
                          mod = 0b00
                          modrm = (mod << 6) | (reg_code << 3) | rm_field
                          return b'\x48\x8B' + struct.pack("B", modrm) + struct.pack("B", sib_byte)
                      elif -128 <= src.disp <= 127:
                          mod = 0b01
                          modrm = (mod << 6) | (reg_code << 3) | rm_field
                          return b'\x48\x8B' + struct.pack("B", modrm) + struct.pack("B", sib_byte) + struct.pack("b", src.disp)
                      else:
                          mod = 0b10
                          modrm = (mod << 6) | (reg_code << 3) | rm_field
                          return b'\x48\x8B' + struct.pack("B", modrm) + struct.pack("B", sib_byte) + struct.pack("<i", src.disp)

                  # Non-SIB (Simple RM)
                  # Simple [Reg] (Mode 00)
                  # Exception: RBP (5) and RSP (4) need SIB.
                  if src.disp == 0 and base_code != 5: # RBP requires disp00 (Mode 01) or explicit Mode 00 with Disp32
                      mod = 0b00
                      modrm = (mod << 6) | (reg_code << 3) | base_code
                      return b'\x48\x8B' + struct.pack("B", modrm)
                  
                  # [Reg + Disp8] (Mode 01)
                  elif -128 <= src.disp <= 127:
                      mod = 0b01
                      modrm = (mod << 6) | (reg_code << 3) | base_code
                      return b'\x48\x8B' + struct.pack("B", modrm) + struct.pack("b", src.disp)
                  
                  # [Reg + Disp32] (Mode 10)
                  else:
                      mod = 0b10
                      modrm = (mod << 6) | (reg_code << 3) | base_code
                      return b'\x48\x8B' + struct.pack("B", modrm) + struct.pack("<i", src.disp)

        return b''

    def _encode_add(self, operands):
        # ... (Existing ADD logic) ...
        if len(operands) == 2 and operands[0].type == "REGISTER" and operands[1].type == "IMMEDIATE":
            reg = operands[0].value
            imm = operands[1].value
            if reg == "rax": return b'\x48\x05' + struct.pack("<I", imm)
        return b''

    def _encode_sub(self, operands):
        # ... (Existing SUB logic) ...
        if len(operands) == 2 and operands[0].type == "REGISTER" and operands[1].type == "IMMEDIATE":
            reg = operands[0].value
            imm = operands[1].value
            if reg == "rax": return b'\x48\x2D' + struct.pack("<I", imm)
        return b''

    def _encode_jump(self, opcode, operands, build_symbols):
        # Generic Short Jump Encoding (Opcode + Rel8)
        # Target must be a label
        if len(operands) == 1 and operands[0].type == "IDENTIFIER":
            target_label = operands[0].value
            
            rel8 = 0
            if not build_symbols:
                # Resolve Label
                if target_label in self.symbol_table:
                    target_offset = self.symbol_table[target_label]
                    # Relative Offset = Target - (Current + InstructionSize)
                    # Instruction Size is 2 bytes (Opcode + 1 byte disp)
                    current_instr_end = self.current_offset + 2
                    offset = target_offset - current_instr_end
                    
                    # Check bounds for signed 8-bit (-128 to 127)
                    if offset < -128 or offset > 127:
                        print(f"Error: Jump to '{target_label}' is out of range for short jump ({offset})")
                        return b'' # Error
                        
                    rel8 = offset & 0xFF
                else:
                     print(f"Error: Label '{target_label}' not found.")
            
            return struct.pack("B", opcode) + struct.pack("B", rel8)
            
        return b''
