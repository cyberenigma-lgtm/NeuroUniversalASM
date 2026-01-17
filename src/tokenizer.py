import json
import re
import os

class Token:
    def __init__(self, type, value, line_num):
        self.type = type
        self.value = value
        self.line_num = line_num

    def __repr__(self):
        return f"Token({self.type}, {self.value}, Line:{self.line_num})"

class Tokenizer:
    def __init__(self, lang_code="es"):
        self.lang_code = lang_code
        self.instruction_map = {} # Maps native -> standard (e.g., "suma" -> "add")
        self.pseudo_map = {}
        self.errors = {}
        self.load_language(lang_code)

    def load_language(self, code):
        """Loads the JSON definition with error handling."""
        path = os.path.join(os.path.dirname(__file__), "..", "languages", f"{code}.json")
        if not os.path.exists(path):
            raise FileNotFoundError(f"Language pack not found: {path}")

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Load Instructions
        for standard, aliases in data["instructions"].items():
            for alias in aliases:
                self.instruction_map[alias.lower()] = standard
                
        # Load Errors
        if "errors" in data:
            self.errors = data["errors"]

    def get_error(self, key, *args):
        """Returns a localized error message."""
        msg = self.errors.get(key, f"Unknown Error ({key})")
        return msg.format(*args)

    def tokenize(self, source_code):
        tokens = []
        lines = source_code.splitlines()
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line or line.startswith(";"): # Skip empty or comments (basic)
                continue
            
            # Remove inline comments
            if ";" in line:
                line = line.split(";")[0].strip()

            # Split by whitespace / commas / brackets / operators
            # We want to keep [ ] + - * , as separate tokens
            parts = re.split(r'([,\s\[\]\+\-\*])', line)
            parts = [p.strip() for p in parts if p.strip()] 
            # Note: We keep commas now so the encoder can split operands


            if not parts:
                continue

            # Process Mnemonic (First word)
            mnemonic = parts[0].lower()
            
            # Check for Implicit Label (e.g., "msg db ...")
            if mnemonic not in self.instruction_map and len(parts) > 1:
                 potential_op = parts[1].lower()
                 if ":" not in mnemonic and potential_op in self.instruction_map:
                      # Yes, it's a label followed by an op
                      tokens.append(Token("LABEL", mnemonic, line_num))
                      mnemonic = potential_op
                      parts = parts[1:] # Shift processing

            if mnemonic in self.instruction_map:
                std_op = self.instruction_map[mnemonic]
                tokens.append(Token("OPCODE", std_op, line_num))
            elif mnemonic.endswith(":"):
                tokens.append(Token("LABEL", mnemonic[:-1], line_num))
                # Handle rest of line on same line? classic asm usually separate
                if len(parts) > 1:
                   # Rerun logic for rest of line? For simplicity assumes newline
                   pass 
            else:
                 # Unknown mnemonic
                 err_msg = self.get_error("ERR_UNKNOWN_OPCODE", mnemonic)
                 raise ValueError(f"[Line {line_num}] {err_msg}")

            # Process Operands
            for part in parts[1:]:
                part_lower = part.lower()
                
                # Registers (Simple check for x64 + SIMD)
                if part_lower in ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rsp", "rbp",
                                  "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15",
                                  "eax", "ebx", "ecx", "edx", "esi", "edi", "esp", "ebp"]:
                    tokens.append(Token("REGISTER", part_lower, line_num))
                
                # SIMD Registers (xmm0-15, ymm0-15)
                elif re.match(r'^(x|y)mm\d+$', part_lower):
                     tokens.append(Token("REGISTER", part_lower, line_num))

                # Immediates (Hex/Dec)
                elif re.match(r'^0x[0-9a-fA-F]+$', part):
                    tokens.append(Token("IMMEDIATE", int(part, 16), line_num))
                elif re.match(r'^\d+$', part):
                    tokens.append(Token("IMMEDIATE", int(part), line_num))
                
                elif re.match(r'^\d+$', part):
                    tokens.append(Token("IMMEDIATE", int(part), line_num))
                
                # Check for Symbols ([ ] + - * ,)
                elif part in ["[", "]", "+", "-", "*", ","]:
                    tokens.append(Token("SYMBOL", part, line_num))
                
                else:
                    # Label reference or unknown
                    tokens.append(Token("IDENTIFIER", part, line_num))
            
            tokens.append(Token("NEWLINE", "\n", line_num))
        
        return tokens
