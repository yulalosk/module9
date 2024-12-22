def all_variants(text):
    for s in range(len(text)):
        for l in range(len(text) - s):
            yield text[l:l + s + 1]


a = all_variants("abc")
for i in a:
    print(i)
