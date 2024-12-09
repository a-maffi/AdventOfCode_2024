const library = require("./library")

let array_disk = library.CreaArray_ID_dot(library.fileContent)
let finish = false
let checkSum = 0
for (i=0; i<array_disk.length; i++){
    if (!finish){
        console.log(i)
        let index_free = library.FindFreeSpaceId(array_disk)
        let index_occupied = library.FindLastOccopiedSpaceId(array_disk)
        if (index_free > index_occupied) finish=true
        else library.SwapPosition(array_disk,index_free,index_occupied)
    }
    if(array_disk[i] == '.') break
    else checkSum += i * array_disk[i]
}
console.log(checkSum)