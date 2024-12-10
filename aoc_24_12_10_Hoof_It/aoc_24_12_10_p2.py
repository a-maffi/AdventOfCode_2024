def leggiFile():
    file_input = "aoc_24_12_10_Hoof_It/input.txt"
    contenuto=""
    with open(file_input, 'r') as file:
            contenuto = file.read()
    return contenuto

def findPoint(matrice,value_point):
    coordinate_point=[]
    lunghezza = len(matrice[0])
    altezza = len(matrice)
    for y in range(altezza):
        for x in range(lunghezza):
            if int(matrice[y][x]) == value_point: coordinate_point.append((y,x))
    return coordinate_point

def IsCoordinateValid(coor,lun,alt):
    return coor[0]<alt and coor[0]>=0 and coor[1]<lun and coor[1]>=0

def recursive(matrix,start,finish,finish_list):
    if not IsCoordinateValid(start,len(matrix[0]),len(matrix)): return False
    if not IsCoordinateValid(finish,len(matrix[0]),len(matrix)): return False
    level_s = int(matrix[start[0]][start[1]])
    level_f = int(matrix[finish[0]][finish[1]])
    if level_f - level_s != 1: return False
    if level_s == 8 and level_f==9: return True

    #CODE CHANGE HERE
    #no more control on finish_list item
    next = (finish[0],finish[1]+1)
    if recursive(matrix,finish,next,finish_list):
        finish_list.append(next)
    
    next = (finish[0],finish[1]-1)
    if recursive(matrix,finish,next,finish_list):
        finish_list.append(next)
    
    next = (finish[0]-1,finish[1])
    if recursive(matrix,finish,next,finish_list):
        finish_list.append(next)
    
    next = (finish[0]+1,finish[1])
    if recursive(matrix,finish,next,finish_list):
        finish_list.append(next)
    
    return False

def find_number_of_path(matrix,start):
    finish_list = []
    
    recursive(matrix,start,(start[0],start[1]+1),finish_list)

    recursive(matrix,start,(start[0],start[1]-1),finish_list)
    
    recursive(matrix,start,(start[0]-1,start[1]),finish_list)
    
    recursive(matrix,start,(start[0]+1,start[1]),finish_list)
    return len(finish_list)

def main():
    c=leggiFile()
    m=c.split("\n")
    starting_point = findPoint(m,0)
    count = 0 
    for s in starting_point:
        count+=find_number_of_path(m,s)

    print(count)

if __name__ == "__main__":
    main()
