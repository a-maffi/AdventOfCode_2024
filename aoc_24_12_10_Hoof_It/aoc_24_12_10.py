#leggo il file di input
def leggiFile():
    file_input = "aoc_24_12_10_Hoof_It/input.txt"
    contenuto=""
    with open(file_input, 'r') as file:
            contenuto = file.read()
    return contenuto

#restituisce tutte le coordinate che hanno un determinato valore
def findPoint(matrice,value_point):
    coordinate_point=[]
    lunghezza = len(matrice[0])
    altezza = len(matrice)
    for y in range(altezza):
        for x in range(lunghezza):
            if int(matrice[y][x]) == value_point: coordinate_point.append((y,x))
    return coordinate_point

#verifica se la coordinata è valida o esce dalla matrice
def IsCoordinateValid(coor,lun,alt):
    return coor[0]<alt and coor[0]>=0 and coor[1]<lun and coor[1]>=0

#funzione ricorsiva per trovare tutte le strade
def recursive(matrix,start,finish,count,finish_list):
    if not IsCoordinateValid(start,len(matrix[0]),len(matrix)): return False
    if not IsCoordinateValid(finish,len(matrix[0]),len(matrix)): return False
    level_s = int(m[start[0]][start[1]])
    level_f = int(m[finish[0]][finish[1]])
    if level_f - level_s != 1: return False
    if level_s == 8 and level_f==9: return True
    
    #let's do the recursion

    #right
    next = (finish[0],finish[1]+1)
    if recursive(matrix,finish,next,count,finish_list):
        if next not in finish_list:
            finish_list.append(next)
            count+=1
    #left
    next = (finish[0],finish[1]-1)
    if recursive(matrix,finish,next,count,finish_list):
        if next not in finish_list:
            finish_list.append(next)
            count+=1
    #up
    next = (finish[0]-1,finish[1])
    if recursive(matrix,finish,next,count,finish_list):
        if next not in finish_list:
            finish_list.append(next)
            count+=1
    #down
    next = (finish[0]+1,finish[1])
    if recursive(matrix,finish,next,count,finish_list):
        if next not in finish_list:
            finish_list.append(next)
            count+=1
    
    return False

#funzione di facciata alla ricorsiva
def find_number_of_path(matrix,start):
    count = 0
    finish_list = []
    #right
    recursive(matrix,start,(start[0],start[1]+1),0,finish_list)
    #left
    recursive(matrix,start,(start[0],start[1]-1),0,finish_list)
    #up
    recursive(matrix,start,(start[0]-1,start[1]),0,finish_list)
    #down
    recursive(matrix,start,(start[0]+1,start[1]),0,finish_list)
    print(start)
    print(count)
    print(finish_list)
    print(len(finish_list))
    return len(finish_list)

c=leggiFile()
m=c.split("\n")
starting_point = findPoint(m,0)
count = 0 
for s in starting_point:
    count+=find_number_of_path(m,s)

print(count)