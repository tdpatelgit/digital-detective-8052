decimal_text = input("Enter a positive decimal number: ")
decimal_number = int(decimal_text)
binary_result = bin(decimal_number)
hexadecimal_result = hex(decimal_number)

print("Decimal     :", decimal_number)
print("Binary      :", binary_result)
print("Hexadecimal :", hexadecimal_result)
