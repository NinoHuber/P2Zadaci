import re

broj = input("Unesite broj u formatu xxx/xxx-xxx: ")

if re.fullmatch(r"(\d){3}\/(\d){3}-(\d){3}", broj):
    print("ispravan unos")
else:
    print("nepravilan format")