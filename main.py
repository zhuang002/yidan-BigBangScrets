# This is the decoding method to decode ONE character
def decode(ch, shift):
    shift %= 26
    # wrap the shift
    shift = 26 - shift
    # convert shift left to shift right
    offset = (ord(ch) - ord('A') + shift) % 26
    # wrap the offset
    return chr(ord('A') + offset)
    # add offset back to ascii.


k = int(input())
encoded = input()
decoded = ""
idx = 1

for c in encoded:
    decoded += decode(c, 3 * idx + k)
    idx += 1
print(decoded)
