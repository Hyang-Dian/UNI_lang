import sys
from .UNI_runtime import UNI_Lang

def main():
    if len(sys.argv) != 2:
        print("Usage: Unilang <filename.uniuni>")
        sys.exit(1)
    filename = sys.argv[1]
    with open(filename, "r", encoding="UTF-8") as file:
        code = file.read()
    
    interpreter = UNI_Lang()
    interpreter.compile(code)

if __name__ == '__main__':
    main()