from piaskownica.simple import linki

max_len = 0
min_len = 9999

for link in linki:
    if link:
        link_length = len(link)
        if len(link) > max_len:
            max_len = len(link)
        if len(link) < min_len:
            min_len = len(link)
print(max_len, min_len)