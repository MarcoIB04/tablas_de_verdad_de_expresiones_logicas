
"""Operador negacion o "not" en Python nos permite negar o invertir un valor booleano"""
valores = [True, False]
def NOT():
    print("----------NEGACION----------\np            ¬ q\n________________________________")
    for a in valores:
        print(a,"       ",(not a))
        print("")
    
NOT()