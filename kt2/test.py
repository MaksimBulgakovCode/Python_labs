a = "abcdefg"
b = ["*"] * 7
for i, ch in enumerate(a):
    print(i, ch)
    if ch == "a":
        b[i] = a[i]

print(b)
