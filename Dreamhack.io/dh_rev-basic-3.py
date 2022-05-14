byte_140003000 = [0x49, 0x60, 0x67, 0x74, 0x63, 0x67, 0x42, 0x66, 0x80, 0x78,
                  0x69, 0x69, 0x7b, 0x99, 0x6d, 0x88, 0x68, 0x94, 0x9f, 0x8d, 0x4d, 0xa5, 0x9d, 0x45]

'''
byte_140003000[i] == (i ^ target) + 2 * i
target == (byte_140003000[i] - 2 * i) ^ i
'''

FLAG = ''

for i in range(0, 24):
    FLAG += chr((byte_140003000[i] - 2 * i) ^ i)

    print("FLAG : ", FLAG)