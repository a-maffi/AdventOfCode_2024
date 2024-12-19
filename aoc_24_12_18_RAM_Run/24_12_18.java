import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class test{

static Mappa m = new Mappa(71,71);
static int passi = 1024;

public static void main(String[] args){

    String percorsoFile="aoc_24_12_18\\input.txt";
    try(BufferedReader br = new BufferedReader(new FileReader(percorsoFile))){
        int i = 0;
        String linea;
        while ((linea=br.readLine())!=null){
            String[] tmp = linea.split(",");
            int x = Integer.parseInt(tmp[0]);
            int y = Integer.parseInt(tmp[1]);
            m.setMuro(x, y);
            i++;
            if (i>=passi) break;
        }
    } catch (IOException e) {
        System.err.println("Err");
    }
    
    int z = m.findMin(0,0,m.getLunghezza()-1,m.getLunghezza()-1);
    System.out.println("min: "+z);

//////////////////////PART 2////////////////////
    int blocchi_caduti=0;
    boolean finale_raggiunto;

        try(BufferedReader br = new BufferedReader(new FileReader(percorsoFile))){
            String linea;
            while ((linea=br.readLine())!=null){
                if(blocchi_caduti%100==0) System.out.println("i :"+blocchi_caduti);
                String[] tmp = linea.split(",");
                int x = Integer.parseInt(tmp[0]);
                int y = Integer.parseInt(tmp[1]);
                m.setMuro(x, y);
                blocchi_caduti++;
                finale_raggiunto = m.ExistPath(0, 0, m.getLunghezza()-1,m.getLunghezza()-1);
                if (!finale_raggiunto) {
                    System.out.println("coordinate fatali: ("+x+","+y+")");
                    break;
                    }
            }
        } catch (IOException e) {
            System.err.println("Err");
        }

    System.out.println("tempo: "+blocchi_caduti);
    }
}
