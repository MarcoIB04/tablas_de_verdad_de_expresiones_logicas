"""El operador disyuncion o "or" en python requiere solo que alguno de los dos valores sea verdadero para devolver el valor True"""

valores = [True, False]

def OR():
    print("---DISYUNCION----\np          q      p v q\n________________________________")
    for a in valores:
        for e in valores:
            print(a,"   ",e,"   ",(a or e))
            print("")

OR()