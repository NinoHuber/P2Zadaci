pozdrav = lambda ime: print("Pozdrav " + ime + "!")

def dobrodosao(naziv):
    print("Dobrodosao " + naziv + "!")

def treca(naziv):
    dobrodosao(naziv)

pozdrav("nikola")
dobrodosao("nikola")
treca("nikola")
