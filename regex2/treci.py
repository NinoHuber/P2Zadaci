import re

sat = input("Unesite broj sati u formatu hh:mm:ss = ")
# moze i također h:mm:ss

if re.fullmatch(r"(^[1-9]|[0-1][1-9]|2[1-4])\:([0-5][0-9])\:([0-5][0-9])", sat):
    print("ispravan unos")
else:
    print("nepravilan unos")