# Binário
valores = ["1000100", "1101001", "1100101", "1100111", "1101111"]
for v in valores:
    print(chr(int(v, 2)), end="")
print()

valores = ["110001", "111001", "/", "110000", "110001", "/", "110010", "110000", "110000", "110011"]
for v in valores:
    if v != "/":
        print(chr(int(v, 2)), end="")
    else:
        print(v, end="")
print()

# Hexadecimal
valores = ["44", "69", "65", "67", "6F"]
for v in valores:
    print(chr(int(v, 16)), end="")
print()

valores = ["31", "39", "/", "30", "31", "/", "32", "30", "30", "33"]
for v in valores:
    if v != "/":
        print(chr(int(v, 16)), end="")
    else:
        print(v, end="")
print()

# Decimal
valores = ["68", "105", "101", "103", "111"]
for v in valores:
    print(chr(int(v)), end="")
print()

valores = ["49", "57", "/", "48", "49", "/", "50", "48", "48", "51"]
for v in valores:
    if v != "/":
        print(chr(int(v)), end="")
    else:
        print(v, end="")
print()