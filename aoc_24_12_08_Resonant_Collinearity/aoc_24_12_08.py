#leggo il file di input
file_input = "aoc_24_12_08_Resonant_Collinearity/input.txt"
contenuto=""
with open(file_input, 'r') as file:
        contenuto = file.read()
matrice_input=contenuto.split("\n")

#LET'S COOK

#creo la matrice in cui segnare gli antinodi e scopro tutti i tipi di antenne esistenti
matrice_antinodi=[]
lista_antenne=[]
for r in range(len(matrice_input)):
    riga=[]
    for c in matrice_input[r]:
        #tipi di antenne
        if c!='.' and lista_antenne.count(c)==0: lista_antenne.append(c)
        #matrice antinodo
        riga.append("."); 
    matrice_antinodi.append(riga)

#date due coordinate (x,y) trova i due punti sulla retta passante per le due coordinate tali
#che la distanza dalla coordinata più vicina sia la metà rispetto quella più lontana
def trovaAntinodi(coordinata_1,coordinata_2):
    delta_x = abs(coordinata_1[0]-coordinata_2[0])
    delta_y = abs(coordinata_1[1]-coordinata_2[1])
    #varia in base ai due punti ( diagonale crescente o discendente)
    if (coordinata_1[0]<=coordinata_2[0] and coordinata_1[1] <= coordinata_2[1]) or (coordinata_1[0] >= coordinata_2[0] and coordinata_1[1] >= coordinata_2[1]):
        c1_x = min(coordinata_1[0],coordinata_2[0])-delta_x
        c1_y = min(coordinata_1[1],coordinata_2[1])-delta_y
        c2_x = max(coordinata_1[0],coordinata_2[0])+delta_x
        c2_y = max(coordinata_1[1],coordinata_2[1])+delta_y
    else:
        if (coordinata_1[0]<coordinata_2[0] and coordinata_1[1] > coordinata_2[1]):
            c1_x = coordinata_1[0] - delta_x
            c1_y = coordinata_1[1] + delta_y
            c2_x = coordinata_2[0] + delta_x
            c2_y = coordinata_2[1] - delta_y
        else:
            c1_x = coordinata_1[0] + delta_x
            c1_y = coordinata_1[1] - delta_y
            c2_x = coordinata_2[0] - delta_x
            c2_y = coordinata_2[1] + delta_y
    
    return [(c1_x,c1_y),(c2_x,c2_y)]

#valida una coordinata (x,y) --> deve stare all'interno della matrice
def valida(coordinata):
    x=coordinata[0]>=0 and coordinata[0]<len(matrice_input[0])
    y=coordinata[1]>=0 and coordinata[1]<len(matrice_input)
    return x and y

#data una lista di coordinate (x,y) trova tutti i punti che rispettino trovaAntiNodi
def setAntinodi(lista_coordinate_antenna):
     c=0
     while c < len(lista_coordinate_antenna) - 1:
        y=c+1
        while y < len(lista_coordinate_antenna):
            coordinate_antinodi=trovaAntinodi(lista_coordinate_antenna[c],lista_coordinate_antenna[y])
            
            for coordinata in coordinate_antinodi:
                if valida(coordinata): matrice_antinodi[coordinata[1]][coordinata[0]]=True
            y+=1
        c+=1

#ciclo le antenne e trovo tutte le coordinate di una determinata antenna, settando 
#alla fine gli antinodi
def trovaCoordinateAntenna(antenna):
    coordinate_antenna=[]
    r=0
    while r<len(matrice_input):
        c=0   
        while c<len(matrice_input[r]):
            if matrice_input[r][c]==antenna:
                coordinate_antenna.append((c,r))
            c+=1
        r+=1
    return coordinate_antenna

def contaAntinodi():
    numero_antinodi=0
    for y in range(len(matrice_antinodi)):
        numero_antinodi+=matrice_antinodi[y].count(True)
    return numero_antinodi

#trovo il numero totale di antinodi
def main():
    for antenna in lista_antenne:
        lista_coordinate_antenna = trovaCoordinateAntenna(antenna)
        setAntinodi(lista_coordinate_antenna)
    numero_antinodi=contaAntinodi()
    print(numero_antinodi)

if __name__ == "__main__":
    main()
