#nothing change on code
#just removing condition of 100 press and adding 10000000000000 at prize position
COST_BUTTON_A = 3
COST_BUTTON_B = 1
MOVEMENT_PRIZE = 10000000000000
#open file
file_input = "aoc_24_12_13_Claw_Contraption/input.txt"
contenuto=""
with open(file_input, 'r') as file:
        contenuto = file.read()
input=contenuto.split("\n")

#setup liste
list_a_x=[]
list_a_y=[]
list_b_x=[]
list_b_y=[]
list_result_x=[]
list_result_y=[]

for i in range(0,len(input),4):
    x=input[i].find("X")+1
    sep=input[i].find(",")
    y=input[i].find("Y")+1
    list_a_x.append(int(input[i][x:sep]))
    list_a_y.append(int(input[i][y:]))

for i in range(1,len(input),4):
    x=input[i].find("X")+1
    sep=input[i].find(",")
    y=input[i].find("Y")+1
    list_b_x.append(int(input[i][x:sep]))
    list_b_y.append(int(input[i][y:]))

for i in range(2,len(input),4):
    x=input[i].find("X")+2
    sep=input[i].find(",")
    y=input[i].find("Y")+2
    list_result_x.append(int(input[i][x:sep]) + MOVEMENT_PRIZE)
    list_result_y.append(int(input[i][y:]) + MOVEMENT_PRIZE)

list_tmp=[]
nope =0
for i in range(len(list_a_x)):

    #1 solution
    movement_b = round((list_result_y[i] - list_a_y[i] * list_result_x[i] / list_a_x[i]) / (list_b_y[i] - (list_b_x[i]*list_a_y[i]/list_a_x[i])),2)
    if movement_b<0 or movement_b%1!=0: 
         continue
    movement_a = round((list_result_x[i] - (list_b_x[i] * movement_b))/list_a_x[i],2)
    if movement_a<0 or movement_a%1!=0: 
         continue
    list_tmp.append((movement_a,movement_b))


cost=0
count = 0
while True:
    if (count==len(list_tmp)): break
    cost+=(list_tmp[count][0]*COST_BUTTON_A + list_tmp[count][1]*COST_BUTTON_B)
    count+=1

print(cost)

