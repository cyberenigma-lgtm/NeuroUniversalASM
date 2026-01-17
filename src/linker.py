import struct

class Linker:
    """
    Wraps raw machine code in executable containers (ELF64 / PE64).
    """
    
    @staticmethod
    def create_elf64(code_bytes, entry_offset=0):
        # ELF Header (64 bytes)
        # 7F 45 4C 46 02 01 01 00 (Magic + Class64 + DataLittle + Version)
        e_ident = b'\x7FELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        e_type = 2 # ET_EXEC
        e_machine = 62 # EM_X86_64
        e_version = 1
        
        # Virtual Address Base = 0x400000
        base_addr = 0x400000
        e_entry = base_addr + 0x78 + entry_offset # header size + entry
        e_phoff = 64 # Program header follows ELF header
        e_shoff = 0
        e_flags = 0
        e_ehsize = 64
        e_phentsize = 56
        e_phnum = 1 # One segment
        e_shentsize = 64
        e_shnum = 0
        e_shstrndx = 0
        
        elf_hdr = struct.pack("<16sHHIQQQIHHHHHH", 
            e_ident, e_type, e_machine, e_version, e_entry,
            e_phoff, e_shoff, e_flags, e_ehsize, e_phentsize, e_phnum,
            e_shentsize, e_shnum, e_shstrndx)
        
        # Program Header (56 bytes)
        # PT_LOAD, R D X, VAddr, PAddr, FileSz, MemSz, Align
        p_type = 1 # PT_LOAD
        p_flags = 0x7 # RWE
        p_offset = 0
        p_vaddr = base_addr
        p_paddr = base_addr
        
        # Code follows Headers
        headers_size = 64 + 56
        full_size = headers_size + len(code_bytes)
        
        p_filesz = full_size
        p_memsz = full_size
        p_align = 0x1000
        
        prog_hdr = struct.pack("<IIQQQQQQ",
            p_type, p_flags, p_offset, p_vaddr, p_paddr,
            p_filesz, p_memsz, p_align)
        
        # Padding to header size? No, we mapped whole file.
        # But for valid offset execution code needs to be at correct place.
        # Simple flat execution: Headers + Code
        
        return elf_hdr + prog_hdr + code_bytes

    @staticmethod
    def create_pe64(code_bytes):
        # Flatten simple code: 
        # For a truly minimal PE, we need:
        # DOS Header, PE Header, Optional Header, Section Table, Section Data
        
        # Alignments
        file_align = 0x200
        sect_align = 0x1000
        
        def align(val, alignment):
            return (val + alignment - 1) & ~(alignment - 1)

        # 1. DOS Header (64 bytes)
        # Magic MZ
        dos_header = b'MZ' + b'\x00'*58 + struct.pack("<I", 64) # Offset to PE Header
        
        # 2. PE Header (Start at 64)
        # Signature "PE\0\0"
        pe_sig = b'PE\0\0'
        
        # File Header (20 bytes)
        # Machine (AMD64=0x8664), Sections(1), Date, SymPtr, SymNum, OpHdrSize, Charact
        # Charact: RelocStripped(1) + Executable(2) + LargeAddress(20) = 0x23
        file_header = struct.pack("<HHIDDHH", 
            0x8664, 1, 0, 0, 0, 0xF0, 0x23) # OpHdrSize=240 (F0)
        
        # Optional Header (Standard+Windows+DataDir = 240 bytes for PE32+)
        # Magic (0x20B for PE32+), Linker Ver, CodeSize, InitData, UninitData
        # EntryPoint, BaseOfCode
        entry_point = 0x1000 # RVA of section
        
        opt_std = struct.pack("<HBBIIIII",
            0x20B, 1, 0, align(len(code_bytes), file_align), 0, 0, 
            entry_point, 0x1000)
            
        # Windows Specific Fields
        # Updated to Version 6.0 (Vista+)
        
        headers_size = align(64 + 4 + 20 + 240 + 40, file_align) # Dos+PE+File+Opt+SectTable
        
        # Section Config
        sect_virt_addr = 0x1000
        sect_virt_size = align(len(code_bytes), sect_align)
        
        # SizeOfImage must include the last section
        image_size = sect_virt_addr + sect_virt_size

        
        opt_win = struct.pack("<QIIHHHHHHIIIIHHQQQQII",
             0x400000, sect_align, file_align,
             6, 0, # OS Major/Minor
             0, 0, # Image Major/Minor
             6, 0, # Subsys Major/Minor
             0, # Win32
             image_size, headers_size, 0, # Sizes + Checksum
             3, 0, # Subsys (Console) + DLL Charact
             0x100000, 0x1000, 0x100000, 0x1000, # Stack/Heap
             0, 16) # Flags + RVA
        
        # Format string check:
        # Q(ImageBase) I(SectAlign) I(FileAlign) H(MajOS) H(MinOS) H(MajImg) H(MinImg) H(MajSub) H(MinSub)
        # I(Win32) I(SizeImg) I(SizeHdr) I(Checksum) H(Subsys) H(DllChar)
        # Q(StackRes) Q(StackCom) Q(HeapRes) Q(HeapCom) I(LoadFlags) I(RunCount)
        # Count: 1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1 = 21 items?
        # My arg count is 22.
        # Let's clean up args and format string.
        # Format: <QIIHHHHIIIIHHQQQQII (19 items?)
        #          1234567890123456789
        # Correct Args:
        # 1. ImageBase (Q)
        # 2. SectionAlign (I)
        # 3. FileAlign (I)
        # 4. MajOS (H)
        # 5. MinOS (H)
        # 6. MajImg (H)
        # 7. MinImg (H)
        # 8. MajSub (H)
        # 9. MinSub (H)
        # 10. Win32Version (I)
        # 11. SizeOfImage (I)
        # 12. SizeOfHeaders (I)
        # 13. CheckSum (I)
        # 14. Subsystem (H)
        # 15. DllCharacteristics (H)
        # 16. SizeOfStackReserve (Q)
        # 17. SizeOfStackCommit (Q)
        # 18. SizeOfHeapReserve (Q)
        # 19. SizeOfHeapCommit (Q)
        # 20. LoaderFlags (I)
        # 21. NumberOfRvaAndSizes (I)
        
        # New Format string: <QIIHHHHHHIIIIHHQQQQII (21 items)

        opt_win = struct.pack("<QIIHHHHHHIIIIHHQQQQII",
             0x400000, sect_align, file_align,
             4, 0, # OS
             0, 0, # Image
             4, 0, # Subsys
             0, # Win32
             image_size, headers_size, 0, # Sizes + Checksum
             3, 0, # Subsys + DLL
             0x100000, 0x1000, 0x100000, 0x1000, # Stack/Heap
             0, 16) # Flags + RVA
        
        # Data Directories (16 * 8 bytes = 128 bytes)
        opt_dirs = b'\x00' * 128
        
        # 3. Section Table (40 bytes per section)
        # Name (.text), VirtualSize, VirtualAddr, SizeOfRaw, PtrRaw, PtrReloc, PtrLine, Reloc, Line, Charact
        # Charact: Code(20) + Exec(20000000) + Read(40000000) + Write(80000000)? -> 0x60000020
        
        raw_size = align(len(code_bytes), file_align)
        
        sect_entry = struct.pack("<8sIIIIIIHHI",
            b'.text\0\0\0', align(len(code_bytes), sect_align), 0x1000,
            raw_size, headers_size, # PointerToRawData
            0, 0, 0, 0, 0x60000020)
            
        # Assemble Headers
        all_headers = dos_header + pe_sig + file_header + opt_std + opt_win + opt_dirs + sect_entry
        
        # Padding
        padding_len = headers_size - len(all_headers)
        padding = b'\x00' * padding_len
        
        # Code Padding
        code_padding_len = raw_size - len(code_bytes)
        code_padding = b'\x00' * code_padding_len
        
        return all_headers + padding + code_bytes + code_padding
