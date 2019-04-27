from os import system
from shift import Shift
from random import randrange

def defineOverlaps(shifts):
    for s in shifts:
        for c in shifts:            
            if (c != s and not(c.start < s.start and c.end < s.start) and not(c.start >= s.end)): 
                s.overlaps.append(c)

def removeConflicts(shifts, added):   
    for s in shifts:
        if added != s:
            if added not in s.overlaps:
                for c in s.overlaps:
                    if c in added.overlaps:
                        s.overlaps = list(filter(lambda x: x != c, s.overlaps))
                        break
            else:
                shifts = list(filter(lambda x: x != s, shifts))
        
    shifts = list(filter(lambda x: x != added, shifts))
    return shifts

def calculateCommittee(shifts):
    committee = []  
    defineOverlaps(shifts)
    #sorteding by overlaps
    overlapsSorted = sorted(shifts, key=lambda x: (-len(x.overlaps), x.start))
    print("Turnos ordenados por conflitos:\n")
    for s in overlapsSorted:
        s.printShift()

    while(len(shifts)):
        added = overlapsSorted[0]  
        committee.append(added)
        shifts = removeConflicts(shifts, added)
        overlapsSorted = sorted(shifts, key=lambda x: (-len(x.overlaps), x.start))    
    return committee

while (True):    
    option = input("Você deseja:\n\n\t1) Turnos aleatórios\n\t2) Selecionar turnos\n\n")
    shifts = []

    if option == '1':
        students = int(input("Digite o número de estudantes: "))
        for i in range(1, students + 1):
            start = randrange(0, 23)
            end = randrange(start + 1, 24)
            shifts.append(Shift(i, start, end))
    elif option == '2':
        students = int(input("Digite o número de estudantes: "))
        for i in range(1, students + 1):
            while(1):
                start = int(input("Insira o tempo inicial do estudante {}:".format(i)))

                end = int(input("Insira o tempo final do estudante {} :".format(i)))

                if((start < 0 or start > 23) or (end < 1 or end > 24)):
                    print("Digite valores entre 0 e 23 para o início e 1 e 24 para o final")
                else:
                    shifts.append(Shift(i, start, end))
                    break     
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