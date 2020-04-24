import sys
import re


def converttobinary():
    x = input("\033[0;37;48mEncrypt: ")
    y = ' '.join(format(ord(i), 'b') for i in x)
    print("\033[0;37;48mBinary:", y)
    options()


def converttotext():
    a = input("\033[0;37;48mDecrypt: ")
    pattern = re.compile('^[01 ]*$')
    if pattern.fullmatch(a):
        a = a.split(" ")
        b = ""
        for binary_value in a:
            c = int(binary_value, 2)
            d = chr(c)
            b += d
        print(b)
        options()
    else:
        print("\033[0;31;50mMake sure your input is in binary.")
        options()


def options():
    e = input("\033[0;37;48mEncrypt or decrypt(e/d): ")
    if e == "e":
        converttobinary()
    elif e == "E":
        converttobinary()
    elif e == "d":
        converttotext()
    elif e == "D":
        converttotext()
    elif e == "quit":
        sys.exit()
    elif e == "Quit":
        sys.exit()
    else:
        print("\033[0;31;50mEnter 'e', 'd', or 'quit'.")
        options()


def main():
    options()


if __name__ == '__main__':
    main()
