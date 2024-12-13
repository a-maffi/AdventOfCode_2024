public class Coordinata{

    public bool Visitato {get;set;}
    public int X {get; set;}
    public int Y {get; set;}
    public char Valore {get; set;}
    public Coordinata(int y, int x, char v){
        this.X = x;
        this.Y = y;
        this.Valore = v;
        this.Visitato = false;
    }

}