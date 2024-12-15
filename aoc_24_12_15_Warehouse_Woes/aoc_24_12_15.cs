//reading file
string filePath="..\\..\\..\\input.txt";
string[] content = File.ReadAllText(filePath).Split("\n");
List<string> warehouse_list = new List<string>();
List<string> command_list = new List<string>();
int count = 0;
bool change=false;
while (count<content.Length){
    if(content[count].Length==1) {
        change=true;
        count++;
        continue;
    }
    if(change) command_list.Add(content[count]);
    else warehouse_list.Add(content[count]);
    count++;
}
//create warehouse
WareHouse wh =new WareHouse(warehouse_list,warehouse_list.Count,warehouse_list[0].Length -1);

//calculate all moves
for(int y=0;y<command_list.Count;y++){
    Console.WriteLine(command_list.ElementAt(y));
    for(int x=0;x<command_list.ElementAt(y).Length;x++){
        wh.TryMove(command_list.ElementAt(y)[x]);
    }
}

//final output
Console.WriteLine(wh.ToString());
Console.WriteLine(wh.SumCoordinateBox());