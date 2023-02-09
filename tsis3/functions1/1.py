def translate (grams):
    ounces = grams * 28.3495231
    return ounces


inp = input()
conv = float(inp)
print(translate(conv))