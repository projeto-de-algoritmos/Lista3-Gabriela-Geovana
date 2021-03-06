from os import system
from shift import Shift
from random import randrange

def defineOverlaps(shifts):
    for s in shifts:
        for c in shifts:            
            if (c != s and not(c.start < s.start and c.end <= s.start) and not(c.start >= s.end)):
                # c ends before s and overlaps
                s.overlaps.append(c)
    
    for s in shifts:
        print(s, s.overlaps)

def removeConflicts(shifts, added):
    for s in shifts:
        if added != s:
            if added not in s.overlaps:
                for c in s.overlaps:
                    if c in added.overlaps:
                        s.overlaps = list(filter(lambda x: x != c, s.overlaps))
            else:
                shifts = list(filter(lambda x: x != s, shifts))    
    shifts = list(filter(lambda x: x != added, shifts))
    return shifts

def calculateCommittee(shifts):
    committee = []  
    defineOverlaps(shifts)
    shifts = sorted(shifts, key=lambda x: x.end)
    print("Turnos ordenados por término:\n")
    for s in shifts:
        s.printShift()

    while(len(shifts)):
        overlaps = sorted(shifts[0].overlaps, key=lambda x: x.end)
        if (len(overlaps)):
            added = overlaps[-1]  
        else:
            added = shifts[0]
        committee.append(added)
        shifts = removeConflicts(shifts, added)
        shifts = sorted(shifts, key=lambda x: x.end)  
    return committee

def readStudents(students):
    shifts = []

    for i in range(1, students + 1):
        while(1):
            start = int(input("Insira o tempo inicial do estudante {}:".format(i)))

            end = int(input("Insira o tempo final do estudante {} :".format(i)))

            if((start < 0 or start > 23) or (end < 1 or end > 24)):
                print("Digite valores entre 0 e 23 para o início e 1 e 24 para o final")
            else:
                shifts.append(Shift(i, start, end))
                break     

    return shifts

def isOverlaping(start, end, shifts):
    
    if not shifts:
        return True

    for c in shifts:            
        if c.end > start and c.start < start: 
            # c ends before s and overlaps
            return True
        elif c.start < end and c.end > end:
            # c ends after s and overlaps
            return True
        elif c.start == start and c.end == end:
            return True 

    return False

def randomShift(shifts):
    start = randrange(0, 23)
    end = randrange(start + 1, 24)

    while end - start > 10 or not isOverlaping(start, end, shifts):
        start = randrange(0, 23)
        end = randrange(start + 1, 24)
    
    return start, end

def getRandomShifts(students): 
    shifts = []
    
    for i in range(1, students + 1): 
        start, end = randomShift(shifts)
        shifts.append(Shift(i, start, end))
    
    return shifts

################################################# MAIN ##############################################

while (True):    
    option = input("Você deseja:\n\n\t1) Turnos aleatórios\n\t2) Selecionar turnos\n\n")
    shifts = []

    if option == '1':
        students = int(input("Digite o número de estudantes: "))
        shifts = getRandomShifts(students)
    elif option == '2':
        students = int(input("Digite o número de estudantes: "))
        shifts = readStudents(students)       
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

    end = input("Deseja continuar?\n\n\t1) Sim\n\t2) Não\n\n")    
    if end == '2':
        break