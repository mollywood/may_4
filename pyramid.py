spaces = 8
stars = 1

for star in range(1, 18, +2):
    print((" " * spaces) + ("*" * stars))
    spaces -= 1
    stars += 2
