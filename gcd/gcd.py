#coding=utf-8
"""最大公约数
"""

def eclud(a, b):
    if b == 0:
        return a
    else:
        return eclud(b, a % b)


if __name__ == '__main__':
    ret  = eclud(3,6)
    print ret