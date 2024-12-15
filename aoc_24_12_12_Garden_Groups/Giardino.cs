public class Giardino{
    protected Coordinata[][] campo;
    protected int altezza;
    protected int lunghezza;

    public Giardino(string[] s,int altezza,int lunghezza){
        this.lunghezza=lunghezza;
        this.altezza=altezza;
        campo = new Coordinata[lunghezza][];
        for(int y=0;y<altezza;y++){
            campo[y]=new Coordinata[lunghezza];
            for(int x=0;x<lunghezza;x++){
                Coordinata c = new Coordinata(y,x,s[y][x]);
                campo[y][x] = c;
            }
        }
    }

/// <summary>
/// funziona ricorsiva nascosta per inziare ad esplorare un'area di
/// giardino data una coordinata e il fiore che lo popola
/// </summary>
/// <param name="x">coordinata x</param>
/// <param name="y">coordinata y</param>
/// <param name="s">simbolo associato al fiore del grupp0</param>
/// <returns>(area,perimetro) del gruppo</returns>
    public (int,int) Esplora(int y,int x,char s){
        if(x>=lunghezza || x<0 || y>=altezza || y<0) return (0,1);
        Coordinata c = this.campo[y][x];
        if(!c.Valore.Equals(s)) return (0,1);
        if(c.Visitato) return (0,0);
        c.Visitato=true;
        (int,int) area_perimetro = (1,0);
        (int,int) dx = Esplora(y,x+1,s);
        (int,int) sx = Esplora(y,x-1,s);
        (int,int) up = Esplora(y-1,x,s);
        (int,int) down = Esplora(y+1,x,s);
        int area = area_perimetro.Item1 + dx.Item1 + sx.Item1 + up.Item1 + down.Item1; 
        int perimetro = area_perimetro.Item2 + dx.Item2 + sx.Item2 + up.Item2 + down.Item2;
        return (area,perimetro);
    }

    public virtual int CostoRecinzioni(){
        (int,int) result=(0,0);
        int costo = 0;
        for(int y=0;y<altezza;y++){
            for(int x=0;x<lunghezza;x++){
                Coordinata coor =this.campo[y][x];
                if(coor.Visitato) continue;
                result = Esplora(coor.Y,coor.X,coor.Valore);
                costo +=result.Item1 * result.Item2;
            }
        }
        return costo;
    }
}