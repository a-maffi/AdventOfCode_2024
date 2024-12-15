using System.ComponentModel;
using System.Data;
using System.Runtime.CompilerServices;

public class WareHouse{

    private int length;
    private int height;

    private (int,int) robot_position;
    private enum Block{
        Robot = '@',       
        Space = '.',
        Box = 'O',
        Wall = '#'
    }


    private Block[][] Map;

    public WareHouse(List<string> blocks, int height, int length){
        this.length = length;
        this.height = height;
        Map = new Block[height][];
        for(int i = 0;i<height;i++){
            Map[i] = new Block[length];
            for(int j = 0;j<length;j++){
                char s = blocks.ElementAt(0)[j];
                Block to_add;
                if(s == (char)Block.Wall) to_add = Block.Wall;
                else if(s==(char)Block.Box) to_add = Block.Box;
                else if(s==(char)Block.Space) to_add = Block.Space;
                else{
                    to_add = Block.Robot;
                    robot_position = (i,j);
                }
                Map[i][j] = to_add;
            }
            blocks.RemoveAt(0);
        }
    }

    /// <summary>
    /// Try to move the pieces.
    ///     -can't move over a wall
    ///     -can move over a free space
    ///     -propagates the move over a box
    /// </summary>
    /// <param name="source">source coordinate (y,x) </param>
    /// <param name="dest">destination coordinate (y,x)</param>
    /// <returns>True if Movement is possible otherwise False</returns>
    private bool TryMove((int,int) source,(int,int) dest){
        Block dest_block = Map[dest.Item1][dest.Item2];
        Block source_block = Map[source.Item1][source.Item2];
        if(dest_block == Block.Wall) return false;
        if(dest_block == Block.Space) {
            Map[dest.Item1][dest.Item2] = source_block;
            Map[source.Item1][source.Item2] =Block.Space;
            return true;
        }
        if(dest_block == Block.Box){
            int y_direction = dest.Item1 - source.Item1;
            int x_direction = dest.Item2 - source.Item2;
            bool recursive_try = TryMove(dest,(dest.Item1+y_direction,dest.Item2+x_direction));
            if(recursive_try){
                Map[dest.Item1][dest.Item2] = source_block;
                Map[source.Item1][source.Item2] =Block.Space;
            }
            return recursive_try;
        }

         
        //never reachable
        return false;
    }

    /// <summary>
    /// try to move the robot:
    ///     -can't move over a wall
    ///     -can move over a free space
    ///     -can move Boxes over other boxes if at the end there is a free space. not if there is a wall
    /// </summary>
    /// <param name="move">character that represent the movement:
    ///     ^ --> up
    ///     > --> right
    ///     v --> down
    ///     < --> left
    ///     </param>
    /// <returns>true if there is a movemente otherwise false</returns>
    public bool TryMove(char move){
        (int,int) movement = robot_position;
        switch (move){
            case '^':
                movement.Item1 -=1;
                break;
            case '>':
                movement.Item2 +=1;
                break;
            case 'v':
                movement.Item1 +=1;
                break;
            case '<':
                movement.Item2 -=1;
                break;
            default:
                return false;
        }
        if(TryMove(robot_position,movement)){
            robot_position = movement;
            return true;
        }
        else return false;
        
    }

    /// <summary>
    /// evaluate the sum of the coordinates of all boxes
    /// a coordinate is the sum of y-position by 100 and x-position by 1
    /// </summary>
    /// <returns>sum of all boxes coordinate</returns>
    public int SumCoordinateBox(){
        int sum=0;
        for(int y=0;y<Map.Length;y++){
            for(int x=0;x<Map[y].Length;x++){
                if(Map[y][x]==Block.Box)
                    sum+= (y*100)+(x*1);
            }
        }
        return sum;
    }

    public override string ToString(){
        string ritorno="";
        for(int y=0;y<height;y++){
            for(int x=0;x<length;x++){
                ritorno+= (char)Map[y][x];
            }
            ritorno+="\n";
        }
        return ritorno;
    }
}
