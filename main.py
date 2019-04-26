from os import system
from shift import Shift
from random import randrange

def removeOverlaps(removed, shifts):
    for s in shifts:
        if removed in s.overlaps:
            s.overlaps.remove(removed)

def isAllSupervised(shifts):

    for s in shifts:
        if not s.isSupervised:
            return False

    return True 

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

    while not isAllSupervised(shifts) and overlapsSorted:
        solution.append(overlapsSorted[0])
        removeOverlaps(overlapsSorted[0], shifts)
        del overlapsSorted[0]

    return solution

while (True):
    
    option = input("Você deseja:\n\n\t1) Turnos aleatórios\n\t2) Selecionar turnos\n\n")
    students = int(input("Digite o número de estudantes: "))
    shifts = []

    if option == '1':
        for i in range(1, students):
            start = randrange(0, 23)
            end = start + randrange(start + 1, 24)
            shifts.append(Shift(i, start, end))
        
        ##students = 6
        
        ##shifts.append(Shift(1, 3, 10))
        ##shifts.append(Shift(2, 14, 18))
        ##shifts.append(Shift(3, 10, 12))
        ##shifts.append(Shift(4, 2, 5))
        ##shifts.append(Shift(5, 16, 20))
        ## shifts.append(Shift(6, 11, 15))

    elif option == '2':
        
        for i in range(1, students):
            while(1):
                start = int(input("Insira o tempo inicial do estudante {}:".format(i)))

                end = int(input("Insira o tempo final do estudante {} :".format(i)))

                if((start < 0 or start > 23) or (end < 1 or end > 24)):
                    print("Digite valores entre 0 e 23 para o início e 1 e 24 para o final")
                else:
                    break

            shifts.append(Shift(i, start, end))
        pass
    else:
        print("Opção inválida")
        break

    system('clear')
    
    print("Turnos:\n")
    for s in shifts:
        s.printShift()

    solution = calculateCommittee(shifts)
    print("\n Estudantes no comitê:\n")
    for s in solution:
        print(s.id)

    end = input("Deseja continuar?\n\n\t1) Não\n\t2) Sim\n\n")
    
    if end == '1':
        break