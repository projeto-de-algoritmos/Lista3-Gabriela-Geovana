from os import system
from shift import Shift


def defineOverlaps(shifts):

    for s in shifts:
        for c in shifts:
            
            if c != s and c.end > s.start and c.start < s.start: 
                # c ends before s and overlaps
                s.overlaps.append(c)
            elif c != s and c.start < s.end and c.end > s.end:
                # c ends after s and overlaps
                s.overlaps.append(c)

def calculateCommittee(shifts):
    
    #interval scheduling sorting
    endSorted = sorted(shifts, key=lambda x: x.end)

    defineOverlaps(shifts)

    # print shifts sorted by end time
    print("Turnos ordenados por término:\n")
    for s in endSorted:
        s.printShift()

    # makes interval scheduling
    # add to possible committee if it's not a solution to interval scheduling
    added = endSorted[0]
    del endSorted[0]
    possibleCommittee = []
    for s in endSorted:
        if s.start >= added.end:
           added = s
        else:
            possibleCommittee.append(s) 
    
    overlapsSorted = sorted(possibleCommittee, key=lambda x: len(x.overlaps))
    solution = [] 

    # while not allSupervised(overlapsSorted):
    #     solution.append(overlapsSorted[0])
    #     del overlapsSorted[0]

    return overlapsSorted

while (True):
    
    option = input("Você deseja:\n\n\t1) Turnos aleatórios\n\t2) Selecionar turnos\n\n")
    students = int(input("Digite o número de estudantes: "))
    shifts = []

    if option == '1':
        # TODO montar shifts
        students = 6
        
        shifts.append(Shift(1, 3, 10))
        shifts.append(Shift(2, 14, 18))
        shifts.append(Shift(3, 10, 12))
        shifts.append(Shift(4, 2, 5))
        shifts.append(Shift(5, 16, 20))
        shifts.append(Shift(6, 11, 15))

    elif option == '2':
        # TODO montar shifts
        pass
    else:
        print("Opção inválida")
        break

    system('clear')


    
    print("Turnos:\n")
    for s in shifts:
        s.printShift()

    solution = calculateCommittee(shifts)
    
    # TODO mostrar número de estudantes no comitê

    end = input("Deseja continuar?\n\n\t1) Não\n\t2) Sim\n\n")
    
    if end == '1':
        break