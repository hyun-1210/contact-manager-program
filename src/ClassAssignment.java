import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.PriorityQueue;
import java.util.Arrays;

public class ClassAssignment {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int class_num = Integer.parseInt(br.readLine());


        int[][] time_map= new int[class_num][2];

        for(int i=0; i<class_num; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            time_map[i][0] = Integer.parseInt(st.nextToken());
            time_map[i][1] = Integer.parseInt(st.nextToken());
        }

        System.out.println(AssignAlgorithim.count_class(time_map));

    }


}

class AssignAlgorithim{

    static int count_class(int[][] sorted_map){
        Arrays.sort(sorted_map, (a,b)-> a[0]==b[0]? a[1]-b[1]:a[0]-b[0]);
        PriorityQueue<Integer> end_time_list= new PriorityQueue<>();
        end_time_list.add(sorted_map[0][1]);
        for(int i=1; i<sorted_map.length; i++){
            if (end_time_list.peek()<=sorted_map[i][0]) {
                    end_time_list.poll();
                }

            end_time_list.add(sorted_map[i][1]);
            }


        return(end_time_list.size());
    }

}
