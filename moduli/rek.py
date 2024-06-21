def unazad(s):
    if s == "":
        return s
    return unazad(s[1:]) + s[0]
