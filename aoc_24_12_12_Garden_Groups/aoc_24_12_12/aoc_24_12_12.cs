
const string filePath = ".\\input.txt";
string content = File.ReadAllText(filePath);
string[] garden = content.Split("\n");
/*
Console.WriteLine(linee[0][3]);
char[][] garden = new char[linee.Length][];
for (int i = 0;i<linee.Length;i++){
    garden[i] = new char[linee[i].Length-offset];
    for (int j = 0;j<linee[i].Length-offset;j++){
        garden[i][j] = linee[i][j];
    }
}

Console.WriteLine(garden.Length);
Console.WriteLine(garden[0].Length);
Console.WriteLine(garden[139][138]);
*/
Giardino g = new Giardino(garden,garden.Length,garden[0].Length - 1);
//(int,int) a=g.Esplora(0,2,'d');
//(int,int) b=g.Esplora(0,0,'a');
//Console.WriteLine($"a:{b.Item1},b:{b.Item2}");
Console.WriteLine($"{g.CostoRecinzioni()}");


