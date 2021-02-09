import random

a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
     'X', 'Y', 'Z']
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z']
c = ['!', '#', '$', '%', '&', '*', '+', '-', '.', '/']

a1 = random.sample(a, 3)
b1 = random.sample(b, 6)
c1 = random.sample(c, 2)
a1.extend(b1 + c1)
random.shuffle(a1)
print("".join(a1))
