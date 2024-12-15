/// <summary>
/// warehouse for box of 2 dimension
/// </summary>
public class warehouse2 : WareHouse{

    public warehouse2(List<string> blocks,int length,int height) : base(blocks,length,height)
    {

    }

    /// <summary>
    /// check if a pieces can be move in specific direction, no otherwise.
    /// Not moving the pieces, only check the factibility
    /// </summary>
    /// <param name="source">source coordinate (y,x)</param>
    /// <param name="dest">destination coordinate (y,x)</param>
    /// <returns>True if Movement is possible otherwise False</returns>
    protected bool CanMove((int,int) source,(int,int) dest){
        Block dest_block = Map[dest.Item1][dest.Item2];
        if(dest_block == Block.Wall) return false;
        if(dest_block == Block.Space) return true;
        
        if(dest_block == Block.Box_start || dest_block == Block.Box_end){
            int y_direction = dest.Item1 - source.Item1;
            int x_direction = dest.Item2 - source.Item2;
            if(y_direction==0){ //teorically never come here for this type of problem
                return CanMove(dest,(dest.Item1,dest.Item2+x_direction));
            }
            else{ //in vertically need 2 control 
                int x_offset = 1; //if box start check on +1 (])
                if(dest_block==Block.Box_end) x_offset = -1; //else check on -1
                return CanMove(dest,(dest.Item1+y_direction,dest.Item2)) 
                && CanMove((dest.Item1,dest.Item2+x_offset),(dest.Item1+y_direction,dest.Item2+x_offset));
            }
        }
        //never come here
        return false;
    }

    protected override bool TryMove((int,int) source,(int,int) dest){
        Block dest_block = Map[dest.Item1][dest.Item2];
        Block source_block = Map[source.Item1][source.Item2];
        if(dest_block == Block.Wall) return false;
        if(dest_block == Block.Space) {
            Map[dest.Item1][dest.Item2] = source_block;
            Map[source.Item1][source.Item2] = Block.Space;
            return true;
        }
        if(dest_block == Block.Box_start || dest_block == Block.Box_end){
            int y_direction = dest.Item1 - source.Item1;
            int x_direction = dest.Item2 - source.Item2;
            if(y_direction==0){ //nothing change from father
                bool recursive_try = TryMove(dest,(dest.Item1,dest.Item2+x_direction));
                if(recursive_try){
                    Map[dest.Item1][dest.Item2] = source_block;
                    Map[source.Item1][source.Item2] = Block.Space;
                }
                return recursive_try;
            }
            else{
                (int,int) next_dest=(dest.Item1+y_direction,dest.Item2);
                int x_offset=1;
                if(dest_block==Block.Box_end) x_offset=-1;
                if(CanMove(dest,next_dest) && CanMove(dest,(next_dest.Item1,next_dest.Item2+x_offset))){
                    TryMove(dest,next_dest);
                    TryMove((dest.Item1,dest.Item2+x_offset),(next_dest.Item1,next_dest.Item2+x_offset));
                    Map[dest.Item1][dest.Item2] = source_block;
                    Map[source.Item1][source.Item2] = Block.Space;
                    return true;
                }
                else return false;
            }
        }
        //never reachable
        return false;
    }

    public override int SumCoordinateBox(){
        int sum=0;
        for(int y=0;y<Map.Length;y++){
            for(int x=0;x<Map[y].Length;x++){
                if(Map[y][x]==Block.Box_start)
                    sum+= (y*100)+(x*1);
            }
        }
        return sum;
    }

}