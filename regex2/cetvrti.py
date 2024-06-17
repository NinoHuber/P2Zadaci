import re

fpmozMail = input("Unesite vas fpmoz mail: ")

if re.fullmatch(r"([a-z]+)\.([a-z]+)(\@fpmoz\.sum\.ba)$", fpmozMail):
    print("mail je pravilan")
else:
    print("mail je nepravilan")

eduID = input("Unesite vas eduID: ")

ime = fpmozMail.split(".")[0]
prezime = fpmozMail.split(".", 1)[1].split("@")[0]

if eduID == ime[0] + prezime + "@sum.ba":
    if re.fullmatch(r"([a-z]+)([0-9]+)?(\@sum\.ba)$", eduID):
        print("eduID je pravilan")
else:
    print("eduID je nepravilan")