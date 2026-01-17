import sys
import os
import argparse
from tokenizer import Tokenizer
from encoder import Encoder

def main():
    parser = argparse.ArgumentParser(
        description="Universal NASM (UASM) - The First Native Multi-Language Assembler",
        epilog="Example: python unasm.py code.asm -l es -o program.bin"
    )
    parser.add_argument("source", help="Source assembly file (.asm)")
    parser.add_argument("-o", "--output", help="Output binary file (.bin). Default: output.bin", default="output.bin")
    parser.add_argument("-l", "--lang", help="Language code (es, fr, hi, jp...). Default: es", default="es")
    parser.add_argument("-f", "--format", default="bin", choices=["bin", "elf64", "pe64"], help="Output format (bin, elf64, pe64)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.source):
        print(f"Error: File {args.source} not found.")
        sys.exit(1)
        
    with open(args.source, "r", encoding="utf-8") as f:
        code = f.read()
        
    print(f"[1/3] Tokenizing using language '{args.lang}'...")
    try:
        tokenizer = Tokenizer(args.lang)
        tokens = tokenizer.tokenize(code)
    except Exception as e:
        print(f"Tokenizer Error: {e}")
        sys.exit(1)
        
    print(f"[2/3] Two-Pass Assembly (Symbol Resolution)...")
    try:
        encoder = Encoder()
        binary = encoder.encode(tokens)
        print(f"Generated {len(binary)} bytes.")
    except Exception as e:
         print(f"Encoder Error: {e}")
         sys.exit(1)
            
    # 3. Handling Format
    # Import dynamically
    try:
        from linker import Linker 
    except ImportError:
        class Linker:
            @staticmethod
            def create_elf64(b, e=0): return b
            @staticmethod
            def create_pe64(b): return b

    final_output = binary
    
    # Resolve Entry Point (_start)
    entry_offset = 0
    if "_start" in encoder.symbol_table:
        entry_offset = encoder.symbol_table["_start"]
    elif "inicio" in encoder.symbol_table: # Spanish fallback
        entry_offset = encoder.symbol_table["inicio"]
    
    if args.format == "elf64":
        final_output = Linker.create_elf64(binary, entry_offset)
        print(f"Linking as ELF64 (Entry: +0x{entry_offset:X})...")
    elif args.format == "pe64":
        final_output = Linker.create_pe64(binary)
        print(f"Linking as PE64 (Stub)...")

    # 4. Write Output
    with open(args.output, "wb") as f:
        f.write(final_output)
    print(f"[3/3] Success! Saved to {args.output} ({len(final_output)} bytes)")

if __name__ == "__main__":
    main()
