//reading file
string filePath="..\\..\\..\\input.txt";
string[] content = File.ReadAllText(filePath).Split("\n");
List<string> warehouse_list = new List<string>();
List<string> command_list = new List<string>();
List<string> warehouse_list_p2 = new List<string>();

int count = 0;
bool change=false;
while (count<content.Length){
    if(content[count].Length==1) {
        change=true;
        count++;
        continue;
    }
    if(change) command_list.Add(content[count]);
    else {
        warehouse_list.Add(content[count]);
        string tmp="";
        for(int x=0;x<content[count].Length;x++){
            if(content[count][x]=='O')tmp+="[]";
            else if(content[count][x]=='@')tmp+="@.";
            else if(content[count][x]=='#')tmp+="##";
            else if(content[count][x]=='.')tmp+="..";
        }
        warehouse_list_p2.Add(tmp);
    }
    count++;
}

//////////////////////// PART 1 /////////////////////////// 
//create warehouse
WareHouse wh =new WareHouse(warehouse_list,warehouse_list.Count,warehouse_list[0].Length -1);

Console.WriteLine(wh.ToString());

//calculate all moves
for(int y=0;y<command_list.Count;y++){
    for(int x=0;x<command_list.ElementAt(y).Length;x++){
        wh.TryMove(command_list.ElementAt(y)[x]);
    }
}

//final output
Console.WriteLine(wh.ToString());
Console.WriteLine(wh.SumCoordinateBox());


//////////////////////// PART 2 /////////////////////////// 

warehouse2 wh2 = new warehouse2(warehouse_list_p2,warehouse_list_p2.Count,warehouse_list_p2[0].Length);

for(int y=0;y<command_list.Count;y++){
    for(int x=0;x<command_list[y].Length;x++){
        //Console.WriteLine(command_list.ElementAt(y)[x]);
        wh2.TryMove(command_list.ElementAt(y)[x]);
        //Console.WriteLine(wh2.ToString());
    }
}

Console.WriteLine(wh2.ToString());
Console.WriteLine(wh2.SumCoordinateBox());