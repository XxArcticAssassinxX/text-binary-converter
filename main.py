import sys
import re
import time

gray_text = "\033[0;37;48m"
red_text = "\033[0;31;50m"

def converttobinary():
    x = input("{}Encrypt: ").format(gray_text)
    time.perf_counter_ns()
    y = ' '.join(format(ord(i), 'b') for i in x)
    binaryTime = time.perf_counter_ns()
    print("Binary:", y).format(gray_text)
    print("Converted to binary in", binaryTime, "nanoseconds.")
    options()


def converttotext():
    a = input("{}Decrypt: ").format(gray_text)
    pattern = re.compile('^[01 ]*$')
    if pattern.fullmatch(a):
        time.perf_counter_ns()
        a = a.split(" ")
        b = ""
        for binary_value in a:
            c = int(binary_value, 2)
            d = chr(c)
            b += d
        textTime = time.perf_counter_ns()
        print(b)
        print("Binary converted to text in", textTime, "nanoseconds.")
        options()
    else:
        print("{}Make sure your input is in binary.").format(red_text)
        options()


def options():
    e = input("{}Encrypt or decrypt(e/d): ").format(gray_text).lower()
    if e == "e":
        converttobinary()
    elif e == "d":
        converttotext()
    elif e == "quit":
        sys.exit()
    else:
        print("Enter 'e', 'd', or 'quit'.").format(red_text)
        options()


def main():
    options()


if __name__ == '__main__':
    main()
