
value1 = 0b110110100
mask   = 0b001001001

print(f"{value1 | mask:09b}")

# 0b111111101
value2 = 0b111111101
mask   = 0b110110110

print(f"{value2 & mask:09b}")