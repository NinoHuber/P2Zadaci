import re

# zadatak: provjeriti je li korisnik unjeo pravilu lozinku, pravilna lozinka treba: imati 9 karaktera najmanje, jedno veliko slovo i treba zavrsiti s tockom

lozinka1 = "kljaslifjliajwflj200"
lozinka2 = "aeiou"
lozinka3 = "DobraLozinka9000."
lozinke = [lozinka1, lozinka2, lozinka3]

def provjera(loz):
    if re.fullmatch(r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{9,}\.$", loz):
        print("lozinka je dobra")
    else:
        print("lozinka nije dovoljno jaka")

for lozinka in lozinke:
    provjera(lozinka)