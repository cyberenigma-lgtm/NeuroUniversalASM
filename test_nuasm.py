#!/usr/bin/env python3
"""
NUASM Test Suite
Verifies that Neuro-Universal-ASM works correctly
"""

import os
import sys
import subprocess
import json

class NUASMTester:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.tests_run = 0
        
    def test(self, name, func):
        """Run a single test"""
        self.tests_run += 1
        print(f"\n[TEST {self.tests_run}] {name}...", end=" ")
        try:
            func()
            print(f"[PASS]")
            self.passed += 1
            return True
        except AssertionError as e:
            print(f"[FAIL]")
            print(f"  Error: {e}")
            self.failed += 1
            return False
        except Exception as e:
            print(f"[ERROR]")
            print(f"  Exception: {e}")
            self.failed += 1
            return False
    
    def summary(self):
        """Print test summary"""
        print(f"\n{'='*60}")
        print(f"Test Summary:")
        print(f"  Total: {self.tests_run}")
        print(f"  Passed: {self.passed}")
        print(f"  Failed: {self.failed}")
        print(f"{'='*60}")
        
        if self.failed == 0:
            print(f"\n[OK] ALL TESTS PASSED!")
            return 0
        else:
            print(f"\n[FAIL] SOME TESTS FAILED")
            return 1

def test_files_exist():
    """Test that all required files exist"""
    required_files = [
        'src/unasm.py',
        'src/tokenizer.py',
        'src/encoder.py',
        'src/linker.py',
        'README.md',
        'TROUBLESHOOTING.md'
    ]
    
    for file in required_files:
        assert os.path.exists(file), f"Missing file: {file}"

def test_language_packs():
    """Test that language packs are valid JSON"""
    lang_dir = 'languages'
    assert os.path.exists(lang_dir), "Missing languages/ directory"
    
    lang_files = [f for f in os.listdir(lang_dir) if f.endswith('.json')]
    assert len(lang_files) > 0, "No language packs found"
    
    for lang_file in lang_files:
        path = os.path.join(lang_dir, lang_file)
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)  # Will raise if invalid JSON
            assert isinstance(data, dict), f"{lang_file} is not a dict"

def test_spanish_compilation():
    """Test compiling Spanish assembly"""
    test_code = """
; Test Spanish
pon rax, 5
pon rbx, 10
suma rax, rbx
ret
"""
    
    with open('test_temp.asm', 'w', encoding='utf-8') as f:
        f.write(test_code)
    
    result = subprocess.run(
        ['python', 'src/unasm.py', 'test_temp.asm', '-l', 'es', '-o', 'test_temp.bin'],
        capture_output=True,
        text=True
    )
    
    os.remove('test_temp.asm')
    
    assert result.returncode == 0, f"Compilation failed: {result.stderr}"
    assert os.path.exists('test_temp.bin'), "Output file not created"
    
    # Verify binary is not empty
    size = os.path.getsize('test_temp.bin')
    assert size > 0, "Output binary is empty"
    
    os.remove('test_temp.bin')

def test_hindi_compilation():
    """Test compiling Hindi assembly"""
    test_code = """
; Test Hindi
rakho rax, 5
rakho rbx, 10
jodo rax, rbx
wapas
"""
    
    with open('test_temp.asm', 'w', encoding='utf-8') as f:
        f.write(test_code)
    
    result = subprocess.run(
        ['python', 'src/unasm.py', 'test_temp.asm', '-l', 'hi', '-o', 'test_temp.bin'],
        capture_output=True,
        text=True
    )
    
    os.remove('test_temp.asm')
    
    assert result.returncode == 0, f"Compilation failed: {result.stderr}"
    assert os.path.exists('test_temp.bin'), "Output file not created"
    
    os.remove('test_temp.bin')

def test_english_kids_mode():
    """Test English kids mode compilation"""
    test_code = """
; Test English Kids Mode
put rax, 5
add rax, 3
show
"""
    
    with open('test_temp.asm', 'w', encoding='utf-8') as f:
        f.write(test_code)
    
    result = subprocess.run(
        ['python', 'src/unasm.py', 'test_temp.asm', '-l', 'en', '-o', 'test_temp.bin'],
        capture_output=True,
        text=True
    )
    
    os.remove('test_temp.asm')
    
    assert result.returncode == 0, f"Compilation failed: {result.stderr}"
    assert os.path.exists('test_temp.bin'), "Output file not created"
    
    os.remove('test_temp.bin')

def test_error_handling():
    """Test that invalid code produces errors"""
    test_code = """
; Invalid instruction
instruccion_invalida rax, 5
"""
    
    with open('test_temp.asm', 'w', encoding='utf-8') as f:
        f.write(test_code)
    
    result = subprocess.run(
        ['python', 'src/unasm.py', 'test_temp.asm', '-l', 'es', '-o', 'test_temp.bin'],
        capture_output=True,
        text=True
    )
    
    os.remove('test_temp.asm')
    
    # Should fail
    assert result.returncode != 0, "Invalid code should produce error"

def test_examples_compile():
    """Test that example files compile"""
    example_files = [
        ('examples/loop_es.asm', 'es'),
        ('examples/test_es.asm', 'es'),
    ]
    
    for example, lang in example_files:
        if os.path.exists(example):
            result = subprocess.run(
                ['python', 'src/unasm.py', example, '-l', lang, '-o', 'test_example.bin'],
                capture_output=True,
                text=True
            )
            
            assert result.returncode == 0, f"Example {example} failed to compile"
            
            if os.path.exists('test_example.bin'):
                os.remove('test_example.bin')

def test_output_formats():
    """Test different output formats"""
    test_code = """
pon rax, 5
ret
"""
    
    formats = ['bin', 'elf64', 'pe64']
    
    for fmt in formats:
        with open('test_temp.asm', 'w', encoding='utf-8') as f:
            f.write(test_code)
        
        result = subprocess.run(
            ['python', 'src/unasm.py', 'test_temp.asm', '-l', 'es', '-f', fmt, '-o', f'test_temp.{fmt}'],
            capture_output=True,
            text=True
        )
        
        os.remove('test_temp.asm')
        
        assert result.returncode == 0, f"Format {fmt} failed"
        assert os.path.exists(f'test_temp.{fmt}'), f"Output file for {fmt} not created"
        
        os.remove(f'test_temp.{fmt}')

def main():
    print("="*60)
    print("NUASM Test Suite")
    print("Testing Neuro-Universal-ASM")
    print("="*60)
    
    # Change to NUASM directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    tester = NUASMTester()
    
    # Run tests
    tester.test("Required files exist", test_files_exist)
    tester.test("Language packs are valid JSON", test_language_packs)
    tester.test("Spanish compilation works", test_spanish_compilation)
    tester.test("Hindi compilation works", test_hindi_compilation)
    tester.test("English kids mode works", test_english_kids_mode)
    tester.test("Error handling works", test_error_handling)
    tester.test("Example files compile", test_examples_compile)
    tester.test("Output formats work", test_output_formats)
    
    # Print summary
    return tester.summary()

if __name__ == '__main__':
    sys.exit(main())
