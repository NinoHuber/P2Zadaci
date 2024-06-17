def parNepar(n):
    for i in range(n):
        if i % 2 == 0:
            yield "parni broj: " + str(i)
        else:
            yield "neparni broj: " + str(i)

for broj in parNepar(15):
    print(broj)