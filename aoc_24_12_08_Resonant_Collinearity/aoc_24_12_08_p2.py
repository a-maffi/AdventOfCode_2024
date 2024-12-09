import aoc_24_12_08 as p1

def trovaAntinodi(coor1,coor2):
    lista_antinodi=[coor1,coor2]
    delta_x = abs(coor1[0]-coor2[0])
    passo_x=delta_x
    delta_y = abs(coor1[1]-coor2[1])
    passo_y=delta_y

    while True:
        if (coor1[0]<=coor2[0] and coor1[1] <= coor2[1]) or (coor1[0] >= coor2[0] and coor1[1] >= coor2[1]):
            c1_x = min(coor1[0],coor2[0])-delta_x
            c1_y = min(coor1[1],coor2[1])-delta_y
            c2_x = max(coor1[0],coor2[0])+delta_x
            c2_y = max(coor1[1],coor2[1])+delta_y
        else:
            if (coor1[0]<coor2[0] and coor1[1] > coor2[1]):
                c1_x = coor1[0] - delta_x
                c1_y = coor1[1] + delta_y
                c2_x = coor2[0] + delta_x
                c2_y = coor2[1] - delta_y
            else:
                c1_x = coor1[0] + delta_x
                c1_y = coor1[1] - delta_y
                c2_x = coor2[0] - delta_x
                c2_y = coor2[1] + delta_y
        
        if not p1.valida((c1_x,c1_y)) and not p1.valida((c2_x,c2_y)): break
        if p1.valida((c1_x,c1_y)): lista_antinodi.append((c1_x,c1_y))
        if p1.valida((c2_x,c2_y)): lista_antinodi.append((c2_x,c2_y))

        delta_x+=passo_x
        delta_y+=passo_y

    return lista_antinodi

def setAntinodi(lista_coordinate_antenna):
    c=0
    while c < len(lista_coordinate_antenna) - 1:
        y=c+1
        while y < len(lista_coordinate_antenna):
            coordinate_antinodi=trovaAntinodi(lista_coordinate_antenna[c],lista_coordinate_antenna[y])
            for coordinata in coordinate_antinodi:
                if p1.valida(coordinata): p1.matrice_antinodi[coordinata[1]][coordinata[0]]=True
            y+=1
        c+=1

def main():
    for antenna in p1.lista_antenne:
        lista_coordinate_antenna = p1.trovaCoordinateAntenna(antenna)
        setAntinodi(lista_coordinate_antenna)
    numero_antinodi=p1.contaAntinodi()
    print(numero_antinodi)
    
if __name__ == "__main__":
    main()