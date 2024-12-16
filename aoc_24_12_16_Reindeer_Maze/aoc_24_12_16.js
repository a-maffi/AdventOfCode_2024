//importo il file di input
const fs = require('fs');
const fileContent = fs.readFileSync('aoc_24_12_16_Reindeer_Maze/input.txt', 'utf-8');

let maze = fileContent.split("\n")

//serve per verificare il eprcorso migliore dopo che trovo una strada già incontrata
let maze_point=[]
for(let i=0;i<maze.length;i++){
    tmp=[]
    for (let j=0;j<maze[i].length;j++){
        tmp.push(-1)
    }
    maze_point.push(tmp)
}
const start_point= [maze.length - 2,1] //S
const end_point = [1,maze[1].length - 3] //E

function abs(x){
    if (x<0) x=-x
    return x
}

function replace(index,str,char){
    let s=""
    for(let x=0;x<str.length;x++){
        if (x==index) s+=char
        else s+=str[x] 
    }
    return s
}

function VectorEquals(v1,v2){
    let length = v1.length
    if (length!= v2.length) return false
    for (let x=0;x<length;x++){
        if (v1[x]!=v2[x]) return false
    }
    return true
}

function findPath(source,destination,total_point,point_to_add,victory_point){

    //se ho già visitato la cella in questo percorso controllo i punteggi
    if(maze[destination[0]][destination[1]]=="X") {
        //se la strada già percorsa è migliore lascio stare
        if (maze_point[destination[0]][destination[1]]<total_point+point_to_add) return
        //se no continuo come se nulla fosse(così ricalcolo)
    }
    //se c'è un muro non avanzo
    if(maze[destination[0]][destination[1]]=="#") return
    
    //se sono arrivato al punto finale aggiungo lo score all'array dei percorsi e continuo la ricerca a ritroso
    if(VectorEquals(destination,end_point)){
        victory_point.push(total_point + point_to_add)
        if(maze_point[destination[0]][destination[1]]>total_point+point_to_add)
            maze_point[destination[0]][destination[1]]=total_point + point_to_add
        return
    }

    //se arrivo qui, in destination c'è uno spazio libero!

    //marco la cella come visitata
    maze[destination[0]]=replace(destination[1],maze[destination[0]],'X')
    //incremento il punteggio dello spostamento
    total_point+=point_to_add
    maze_point[destination[0]][destination[1]]=total_point
    //calcolo la direzione
    let x_delta = destination[1] - source[1] //1 > ||| -1 <
    let y_delta = destination[0] - source[0] //1 v ||| -1 ^

    //invoco ricorsivamente le 4 direzioni
    let up=[destination[0]-1,destination[1]] 
    let down=[destination[0]+1,destination[1]] 
    let right=[destination[0],destination[1]+1]
    let left=[destination[0],destination[1]-1] 

    //il primo if serve per NON tornare da dove sono venuto
    if(!VectorEquals(source,up)) findPath(destination,up,total_point,1 + abs(x_delta)*1000 ,victory_point)
    if(!VectorEquals(source,down)) findPath(destination,down,total_point,1 + abs(x_delta)*1000 ,victory_point)
    if(!VectorEquals(source,left)) findPath(destination,left,total_point,1 + abs(y_delta)*1000 ,victory_point)
    if(!VectorEquals(source,right)) findPath(destination,right,total_point,1 + abs(y_delta)*1000 ,victory_point)
    return
}

function getFewestPointPath(){
    let list_point=[]
    maze_point[start_point[0]][start_point[1]]=0
    let up=[start_point[0]-1,start_point[1]]
    let right=[start_point[0],start_point[1]+1]
    findPath(start_point,up,0,1001,list_point)
    findPath(start_point,right,0,1,list_point)

    if(list_point.length==0) return -1
    let min=list_point[0]
    for(let x=1;x<list_point.length;x++){
        if (list_point[x]<min)
            min=list_point[x]
    }
    return min
}
let min=getFewestPointPath()
console.log(`punteggio minimo raggiungibile: ${min}`)

