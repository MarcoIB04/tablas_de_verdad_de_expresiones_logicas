"""El operador conjuncion o "and" nos genera un valor verdadero si y solo si los dos valores comparados son verdaderos."""

valores = [True, False]

def AND():
    print("----------CONJUNCION----------\np          q      p ^ q\n________________________________")
    for a in valores:
        for e in valores:
            print(a,"   ",e,"   ",(a and e))
            print("")

AND()