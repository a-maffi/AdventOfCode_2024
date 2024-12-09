const library = require("./library")

//trova l'indice da cui iniziano n spazi liberi
function Find_n_freeSpace(arr,n,stopIndex=arr.length){
    for (let index = 0; index<arr.length; index++){
        if(index>stopIndex) return -1
        if (arr[index]!='.') continue
        let find=true
        for (let number=index;number<index+n;number++){
            if(arr[number]!='.') {
                find=false;
                index=number
                break
            }
        }
        if (find) return index
    }
    return -1
}

//scambia n posizioni vuote con n posizioni di file
function Swap_n_Position(arr,indexFreeSpace,indexFile,n){
    for (let y=0;y<n;y++){
        arr[indexFreeSpace+y]=arr[indexFile+y]
        arr[indexFile+y]='.'
    }
}

//indexFile deve essere l'indice maggiore
function trovaPesoDaIndiceMaggiore(arr,indexFile){
    let indexOfFile=arr[indexFile]
    peso=1
    for(let x=indexFile-1;x>=0;x--){
        if(arr[x]==indexOfFile) peso++
        else break
    }
    return peso
}

let array_disk = library.CreaArray_ID_dot(library.fileContent)
let file_visti=[]
for (let x=array_disk.length - 1;x>=0;x--){
    if(array_disk[x]=='.' || file_visti.includes(array_disk[x])) continue
    file_visti.push(array_disk[x])
    let peso_file = trovaPesoDaIndiceMaggiore(array_disk,x)
    let index_spazioLibero_necessario = Find_n_freeSpace(array_disk,peso_file,x)
    if (index_spazioLibero_necessario!=-1) Swap_n_Position(array_disk,index_spazioLibero_necessario,x-peso_file + 1,peso_file)
    x -= (peso_file - 1)
}

console.log(array_disk)

checksum = 0

for (let x=0;x<array_disk.length;x++){
    if(array_disk[x]!='.')  checksum+=array_disk[x]*x
}
console.log(checksum)