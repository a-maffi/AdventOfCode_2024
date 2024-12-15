
const string filePath = "..\\..\\..\\input.txt";
string content = File.ReadAllText(filePath);
string[] garden = content.Split("\n");

Giardino g = new Giardino(garden,garden.Length,garden[0].Length - 1);

Console.WriteLine($"{g.CostoRecinzioni()}");


