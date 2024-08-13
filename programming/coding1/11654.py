n = input()


try:
    a = int(n)
    print("a",chr(n))
except Exception as e:
    b = str(n)
    print("b",ord(b))
