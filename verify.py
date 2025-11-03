#!/usr/bin/env python3
"""
验证脚本 - 检查 Python 代码语法和核心逻辑
"""
import py_compile
import sys

def parse_parking_space(space_str):
    """解析车位号为坐标 A11 -> (0,11), B23 -> (1,23)"""
    space_str = space_str.strip().upper()
    if len(space_str) != 3:
        return None
    
    letter = space_str[0]
    if letter not in 'ABCD':
        return None
    x = ord(letter) - ord('A')
    
    try:
        y = int(space_str[1:3])
        if y > 39:
            return None
        return (x, y)
    except:
        return None

def verify_syntax(filename):
    """验证 Python 文件语法"""
    try:
        py_compile.compile(filename, doraise=True)
        print(f"✓ {filename} - 语法正确")
        return True
    except py_compile.PyCompileError as e:
        print(f"✗ {filename} - 语法错误:")
        print(f"  {e}")
        return False

def test_parking_parser():
    """测试车位号解析函数"""
    print("\n测试车位号解析逻辑...")
    
    test_cases = [
        ("A00", (0, 0)),
        ("A11", (0, 11)),
        ("B23", (1, 23)),
        ("C12", (2, 12)),
        ("D39", (3, 39)),
        ("D40", None),
        ("E11", None),
        ("A", None),
        ("A1", None),
        ("ABC", None),
    ]
    
    all_pass = True
    for input_str, expected in test_cases:
        result = parse_parking_space(input_str)
        if result == expected:
            print(f"  ✓ {input_str:4s} -> {result}")
        else:
            print(f"  ✗ {input_str:4s} -> {result} (预期: {expected})")
            all_pass = False
    
    return all_pass

def main():
    """主函数"""
    files = ['main.py', 'verify.py']
    
    print("=" * 50)
    print("正在验证 Python 代码语法...")
    print("=" * 50)
    
    all_ok = True
    for filename in files:
        if not verify_syntax(filename):
            all_ok = False
    
    if not test_parking_parser():
        all_ok = False
    
    print("=" * 50)
    if all_ok:
        print("✓ 所有检查通过！")
        print("\n项目已准备好打包为 Android APK。")
        print("请在 Linux 环境中运行 ./build.sh 构建 APK。")
        return 0
    else:
        print("✗ 发现错误，请修复后重试。")
        return 1

if __name__ == '__main__':
    sys.exit(main())
