def getbit(value, n):
    if n <= 0:
        return None
    else:
        return value >> (n - 1) & 1
#-------------------------------------

def setbit(value, n):
    if n <= 0:
        return None
    else:
        mask = 1 << (n - 1)
        return value | mask
#-------------------------------------
def clearbit(value, n):
    mask = 1 << (n - 1) # e.g. n == 2 --> 0000010
    mask = ~mask        #                 1111101
    return value & mask
#-------------------------------------

def togglebit(value, n):
    return value ^ (1 << (n - 1))

#-------------------------------------
# Kernighan's Algorithm
def countsetbits(value):
    
    count = 0
    while value != 0:
        value = value & (value - 1)
        count += 1
    return count    

#-------------------------------------
def hammingdistance(value1, value2):
    value = value1 ^ value2
    return countsetbits(value)

#-------------------------------------
def paritybit(value, even_parity = True):
    count = countsetbits(value)
    if count % 2 == even_parity:
        return 1
    else:
        return 0
        
#-------------------------------------
def getbyte(value, n):
    return (value >> (n - 1) * 8) & 0xFF

#-------------------------------------


assert getbit(0xCA, 1) == 0
assert getbit(0xCA, 2) == 1
assert getbit(0xCA, 3) == 0
assert getbit(0xCA, 4) == 1
assert getbit(0xCA, 5) == 0
assert getbit(0xCA, 6) == 0
assert getbit(0xCA, 7) == 1
assert getbit(0xCA, 8) == 1


assert setbit(0xCA, 1) == 0xCB
assert setbit(0xCA, 2) == 0xCA
assert setbit(0xCA, 3) == 0xCE
assert setbit(0xCA, 4) == 0xCA
assert setbit(0xCA, 5) == 0xDA
assert setbit(0xCA, 6) == 0xEA
assert setbit(0xCA, 7) == 0xCA
assert setbit(0xCA, 8) == 0xCA

assert clearbit(0xCA, 1) == 0xCA
assert clearbit(0xCA, 2) == 0xC8
assert clearbit(0xCA, 3) == 0xCA
assert clearbit(0xCA, 4) == 0xC2
assert clearbit(0xCA, 5) == 0xCA
assert clearbit(0xCA, 6) == 0xCA
assert clearbit(0xCA, 7) == 0x8A
assert clearbit(0xCA, 8) == 0x4A


assert togglebit(0xCA, 1) == 0xCB   
assert togglebit(0xCA, 2) == 0xC8 
assert togglebit(0xCA, 3) == 0xCE 
assert togglebit(0xCA, 4) == 0xC2 
assert togglebit(0xCA, 5) == 0xDA 
assert togglebit(0xCA, 6) == 0xEA
assert togglebit(0xCA, 7) == 0x8A
assert togglebit(0xCA, 8) == 0x4A


assert countsetbits(0x7C) == 5
assert countsetbits(113) == 4
assert countsetbits(0x713DA4A) == 14


assert hammingdistance(0xDF, 0xAE) == 4
assert hammingdistance(0xFF, 0xDD) == 2
assert hammingdistance(0xFF, 255) == 0


assert paritybit(0x2E) == 0
assert paritybit(0x2E, False) == 1
assert paritybit(0x61) == 1
assert paritybit(0x61, False) == 0
assert paritybit(0x5200) == 1
assert paritybit(0x5200, False) == 0

assert getbyte(0xFFCCDBE5, 1) == 0xE5
assert getbyte(0xFFCCDBE5, 2) == 0xDB
assert getbyte(0xFFCCDBE5, 3) == 0xCC
assert getbyte(0xFFCCDBE5, 4) == 0xFF