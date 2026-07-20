import struct

binary_str = "0000000100000100000010000001101100100010101011100000111010000011"
int_value = int(binary_str, 2)
bytes = struct.pack('!Q', int_value)
float_value = struct.unpack('!d', bytes)[0]

float_conversion = float(int_value)

print("Binary string:",binary_str)
print("int value:",int_value)
print("float from binary:",float_value)
print("float from int:",float_conversion)