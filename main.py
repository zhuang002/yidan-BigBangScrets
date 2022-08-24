def decode(ch, shift):
    shift %= 26
    shift = 26 - shift
    offset = (ord(ch)-ord('A')+shift) % 26
    return chr(ord('A')+offset)

k = int(input())
encoded = input()
decoded = ""
idx=1

for c in encoded:
    decoded += decode(c, 3*idx+k)
    idx += 1
print(decoded)
