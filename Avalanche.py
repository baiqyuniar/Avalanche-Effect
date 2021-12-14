a = 0b11010101100011010101110101100010011001100111001001010000101111100010011010010011111010110011010100000100010010111110001110110011
b = 0b1000001101100100100000100001111110010110000011101010010100001101100110001100010111010000000101011100100101010001100100111001000
diff = bin(a^b)
print("The difference bit \t:\t", diff)

# next steps to count 1s in binary number
count = 0
for i in diff:
    if i == "1":
        count += 1
print ("Total difference \t:\t", count, "bits")
len_a = len(bin(a))
len_b = len(bin(b))

# To ensure divide by the longest binary string
if (len_a) >= (len_b):
    AE = (count/ len_a) * 100
else:
    AE = (count/ len_b) * 100
print ("Avalanche effect \t:\t", AE, "%")

#simon > 256 = 48%; 128 = 46%; 192 = 54%
#speck > 128 = 57%; 192 = 53%; 256 = 50%