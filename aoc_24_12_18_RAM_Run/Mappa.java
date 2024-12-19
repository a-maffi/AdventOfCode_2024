import java.util.HashMap;
import java.util.Map;

public class Mappa{
    final private int lunghezza;
    final private int altezza;
    private Map<String, Integer> punteggi;


    public Mappa(int lunghezza,int altezza){
        this.altezza = altezza;
        this.lunghezza = lunghezza;
        this.punteggi = new HashMap<>();
        //inizializzo l'hashmap
        for (int y=0;y<altezza;y++){
            for (int x=0;x<lunghezza;x++){
                this.punteggi.put(y + "," + x, 0); 
            }
        }
    }

    public int getAltezza() {
        return altezza;
    }

    public int getLunghezza() {
        return lunghezza;
    }

    public int getPunteggio(int y, int x) {
        return punteggi.get(y + "," + x);
    }

    public void setPunteggio(int y, int x, int punteggio) {
        punteggi.put(y + "," + x, punteggio);
    }

    public void setMuro(int x,int y){
        punteggi.put(y + "," + x, -1);
    }

    public int findMin(int start_y,int start_x,int end_y,int end_x){
      
        punteggi.put(start_y+","+start_x, 1); //setto ad 1 la partenza
        //cerca in alto
        if(start_y-1 >=0) creaPercorso(start_y,start_x,start_y-1,start_x,1);        
        //cerca in basso  
        if(start_y+1 <altezza) creaPercorso(start_y,start_x,start_y+1,start_x,1); 
        //cerca a sinistra
        if(start_x-1 >=0) creaPercorso(start_y,start_x,start_y,start_x-1,1);
        //cerca a destra
        if(start_x+1 <lunghezza) creaPercorso(start_y,start_x,start_y,start_x+1,1);
        return punteggi.get(end_y+","+end_x) - 1;

    }


    private void creaPercorso(int s_y,int s_x,int d_y,int d_x,int punti_da_aggiungere){
        int punteggio_start = punteggi.get(s_y+","+s_x);
        int punteggio_dest = punteggi.get(d_y+","+d_x);
        if (punteggio_dest<0) return; //se è un muro torno
        int punteggio_finale = punteggio_start + punti_da_aggiungere;
        if (punteggio_dest!=0 && punteggio_dest<= punteggio_finale) return; //se l'arrivo è gia stato visto con punteggi minori torno
        punteggi.put(d_y+","+d_x,punteggio_finale);  
        //cerca in basso
        if(d_y + 1 < this.altezza) creaPercorso(d_y,d_x,d_y+1,d_x,1);    
        //cerca in alto
        if(d_y - 1 >= 0) creaPercorso(d_y,d_x,d_y-1,d_x,1);
        //cerca a sinistra
        if(d_x - 1 >=0) creaPercorso(d_y,d_x,d_y,d_x-1,1);
        //cerca a destra
        if(d_x + 1 < this.lunghezza) creaPercorso(d_y,d_x,d_y,d_x+1,1);
        
    }

    private boolean  ExistingPath(int s_y,int s_x,int d_y,int d_x,int f_y,int f_x){
        if(d_x<0 || d_x>=lunghezza || d_y<0 || d_y>=altezza) return false;
        if(d_x==f_x && d_y==f_y) return true;
        if(punteggi.get(d_y+","+d_x)==-2) return false; //tolgo i già visitati
        if(punteggi.get(d_y+","+d_x)==-1) return false;
        punteggi.put(d_y+","+d_x, -2);
        return ExistingPath(d_y,d_x,d_y-1,d_x,f_y,f_x) ||
               ExistingPath(d_y,d_x,d_y+1,d_x,f_y,f_x) ||
               ExistingPath(d_y,d_x,d_y,d_x-1,f_y,f_x) ||
               ExistingPath(d_y,d_x,d_y,d_x+1,f_y,f_x);
        
    }

    public boolean ExistPath(int s_y,int s_x,int d_y,int d_x){
        pulisciMappaTranneMuri();
        punteggi.put(s_y+","+s_x, -2); 
        return ExistingPath(s_y,s_x,s_y+1,s_x,d_y,d_x) ||
               ExistingPath(s_y,s_x,s_y-1,s_x,d_y,d_x) ||
               ExistingPath(s_y,s_x,s_y,s_x+1,d_y,d_x) ||
               ExistingPath(s_y,s_x,s_y,s_x-1,d_y,d_x);
    }

    private void pulisciMappaTranneMuri(){
        for (Map.Entry<String, Integer> e : punteggi.entrySet()) {
            if(punteggi.get(e.getKey())!=-1) punteggi.put(e.getKey(), 0);
        }
    }

    
    @Override
    public String toString(){
        String s = "";
        for (int y=0;y<altezza;y++){
            for (int x=0;x<lunghezza;x++){
                s+=punteggi.get(y+","+x).toString()+" ";
            }
            s+="\n";
        }
        return s;
    }

}