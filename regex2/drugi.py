import re

rođendan = input("Unesite vas datum rođenja u formatu dd.mm.yyyy. koji ne smije biti prije 1900: ")
# moze se unjeti 0x.0x.xxxx. ili x.x.xxxx. 

if re.fullmatch(r"(0[1-9]|^[0-9]|[12][0-9]|3[01])\.(0[1-9]|[0-9]|1[0-2])\.(19[0-9][0-9]|2[0-9][0-9][0-9])\.$", rođendan):
    print("ispravan unos")
else:
    print("nepravilan unos")