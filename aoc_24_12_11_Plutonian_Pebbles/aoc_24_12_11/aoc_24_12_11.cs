const string filePath = ".\\input.txt"; //very bad
const int Number_of_blink=75;

string content = File.ReadAllText(filePath);
string[] stones_string = content.Split(" ");
Dictionary<ulong, ulong> stones_start =new Dictionary<ulong, ulong>();
Dictionary<ulong, ulong> stones_end;

for (int i=0;i<stones_string.Length;i++){
    stones_start.Add(ulong.Parse(stones_string[i]),1);
}
ulong total_stone=8;
int Blink(ulong key){
    ulong peso = stones_start[key];
    string cifra_stringa = key.ToString();
    ulong new_stone;
        if(key==0){
            new_stone=1;
            if(stones_end.ContainsKey(new_stone)){
                stones_end[new_stone] = stones_end[new_stone] + peso;
                return 0;
            }
            else{
                stones_end.Add(new_stone, peso);
                return 1;
            }
        }
        else if(cifra_stringa.Length%2==0){
            total_stone+=peso;
            string n_1 ="";
            string n_2="";
            for (int x=0;x<cifra_stringa.Length/2;x++) n_1+=cifra_stringa[x];
            for (int x=cifra_stringa.Length/2;x<cifra_stringa.Length;x++) n_2+=cifra_stringa[x];
            new_stone=ulong.Parse(n_1);
            int valori_aggiunti = 0;
            if(stones_end.ContainsKey(new_stone)) {
                stones_end[new_stone] = stones_end[new_stone] + peso;
            }
            else {
                stones_end.Add(new_stone, peso);
                valori_aggiunti++;
                }

            new_stone=ulong.Parse(n_2);
            if(stones_end.ContainsKey(new_stone)) {
                stones_end[new_stone] = stones_end[new_stone] + peso;
                return 1;
            }
            else {
                stones_end.Add(new_stone, peso);
                valori_aggiunti++;
                return 0;
                }
        }
        else{
            new_stone = key*2024;
            if(stones_end.ContainsKey(new_stone)) {
                stones_end[new_stone] = stones_end[new_stone] + peso;
                return 0;
            }
            else {
                stones_end.Add(new_stone, peso);
                return 1;
                }
            }
}
stones_end = new Dictionary<ulong, ulong>(stones_start);
for(int passo=0;passo<Number_of_blink;passo++){
    stones_start = new Dictionary<ulong, ulong>(stones_end); 
    stones_end.Clear();
    foreach(var key in stones_start.Keys){
        int x=Blink(key);
    }
}

Console.WriteLine(total_stone);
Console.WriteLine("end");
Console.ReadKey();