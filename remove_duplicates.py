names = ["Alex", "John", "Mary", "Steve", "John", "Steve"]
duplicate_free = []

for name in names:
    if name not in duplicate_free:
        duplicate_free.append(name)

print(duplicate_free)
