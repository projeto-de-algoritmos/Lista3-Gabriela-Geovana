from os import system
from shift import Shift

while (True):
    
    option = input("Você deseja:\n\n\t1) Turnos aleatórios\n\t2) Selecionar turnos\n\n")
    students = int(input("Digite o número de estudantes: "))

    if option == '1':
        pass
    elif option == '2':
        pass
    else:
        print("Opção inválida")

    system('clear')

    # TODO montar shifts
    shifts = []
    shifts.append(Shift(5, 10))
    shifts.append(Shift(7, 15))

    print("Turnos:\n")
    for s in shifts:
        s.printShift()

    # TODO calcular número de estudantes no comitê
    # TODO mostrar número de estudantes no comitê

    end = input("Desja continuar?\n\n\t1) Não\n\t2) Sim\n\n")
    
    if end == '1':
        break