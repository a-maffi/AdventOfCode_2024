import Computer as pc
import sys
import io

#leggo il file di input
file_input = "aoc_24_12_17_Chronospatial_Computer/input.txt"
contenuto=""
with open(file_input, 'r') as file:
        contenuto = file.read()
matrice_input=contenuto.split("\n")

#inizializzo il pc

a = int(matrice_input[0][matrice_input[0].index(":")+1:])
b = int(matrice_input[1][matrice_input[1].index(":")+1:])
c = int(matrice_input[2][matrice_input[2].index(":")+1:])
pc.inizializza(a,b,c)

program_list = matrice_input[4][matrice_input[4].index(":")+2:].split(",")
program_input = []
for num in program_list:
    program_input.append(int(num))

def eseguiProgramma(programma):
    i = 0
    while i<len(programma):
        comando = programma[i]
        operando = programma[i+1]
        i=pc.EseguiIstruzione(comando,operando)

eseguiProgramma(program_input)
print()
############################# PART 2 #####################

def eseguiProgramma_check(programma):
    global output_desiderato
    i = 0
    y = 0
    x = 0
    while i<len(programma):
        comando = programma[i]
        operando = programma[i+1]
        i=pc.EseguiIstruzione(comando,operando)

        output_programma = output_buffer.getvalue()
        #esco in anticipo se vedo che le stringhe non coincidono
        if(x<len(output_programma)):
            if (int(output_programma[x])!=programma[y]): return False
            x+=2
            y+=1

min_a_register = 0

#creo la stringa da controllare
output_desiderato=""
for s in range(len(program_list)):
    if s==0:
        output_desiderato+=program_list[s]
    else:
        output_desiderato+=","+program_list[s]

#creo il buffer in cui salvare temporaneamente l'output
output_buffer = io.StringIO()
sys.stdout = output_buffer

min_a_register = 100000000

while True:
    pc.inizializza(min_a_register,b,c)
    eseguiProgramma_check(program_input)
    
    if output_desiderato == output_buffer.getvalue():
        break
    if(min_a_register%100000000==0):
        sys.stdout = sys.__stdout__
        print(min_a_register)
        sys.stdout=output_buffer
    min_a_register+=1
    output_buffer.truncate(0)
    output_buffer.seek(0)
    
sys.stdout = sys.__stdout__
print("output: "+output_buffer.getvalue(),end="")
print("minimo a =",min_a_register)
output_buffer.close()


#1900000000 too low