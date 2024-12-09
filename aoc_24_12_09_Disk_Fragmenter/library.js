//importo il file di input
const fs = require('fs');
const fileContent = fs.readFileSync('aoc_24_12_09_Disk_Fragmenter/input.txt', 'utf-8');

//creo un array contenente idFile e .
function CreaArray_ID_dot(fileContent){
    let id_file=0
    let spazio_vuoto=false
    let blocchiIndividuali=[]
    for(let s of fileContent){ //s=valore del carattere
        for(let x=0;x<s;x++){ //ciclo tante volte quanto s
            if (spazio_vuoto) blocchiIndividuali.push(".")
            else{
                blocchiIndividuali.push(id_file)
            }
        }
        if (!spazio_vuoto) id_file++ //se era un file incremento il valore per il prossimo file
        spazio_vuoto=!spazio_vuoto //inverto da spazio vuoto a file e viceversa
    }
    return blocchiIndividuali
}

function FindFreeSpaceId(arr){
    for(let indice=0;indice<arr.length;indice++){
        if (arr[indice]=='.') return indice
    }
    return -1
}

function FindLastOccopiedSpaceId(arr){
    for (let indice=arr.length - 1; indice>=0; indice--) {
        if (arr[indice]!='.') return indice
    }
    return -1
}

function SwapPosition(arr,index1,index2){
    tmp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = tmp
}

module.exports = {
    "fileContent" : fileContent,
    "SwapPosition" : SwapPosition,
    "FindLastOccopiedSpaceId" : FindLastOccopiedSpaceId,
    "FindFreeSpaceId" : FindFreeSpaceId,
    "CreaArray_ID_dot" : CreaArray_ID_dot
  };