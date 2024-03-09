def decimal_a_binario(n):
    binario = ""
    while n > 0:
        result = (n // 2)
        rest = n % 2
        binario = str(rest) + binario
        n = result
    return binario if binario else "0"
    
# print(decimal_a_binario())

def binario_a_decimal(b):
    result = 0
    for i in str(b):
        bit = int(i)
        result = result * 2 + bit
    return result
print(binario_a_decimal("1010"))