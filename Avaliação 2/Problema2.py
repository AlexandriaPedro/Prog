anima = int(input("É de Animação? "))
if anima == 1:
    disney = int(input("É da Disney? "))
    if disney == 1:
        print ("Resposta: Frozen")
    else:
        print ("Resposta: Shrek")
else:
    terror = int(input("É de Terror? "))
    if terror == 1:
        com = int(input("É de Comédia? "))
        if com == 1:
            print("Resposta: Todo Mundo em Pânico")
        else:
            print("Resposta: Halloween")
    else:
        drama = int(input("É de Drama? "))
        if drama == 1:
            print("Resposta: Diário de Uma Paixão")
        else:
            print("Resposta: Como se Fosse a Primeira Vez")
