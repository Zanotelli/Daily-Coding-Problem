import java.io.IOException;

import java.util.Objects;
import java.util.Scanner;
import java.util.Vector;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);

        Vector<Integer> vec = new Vector<>();

        while (true){
            try {
                vec.add(sc.nextInt());
            }catch (Exception e){
                break;
            }
        }
        System.out.println(vec);

        Vector<Integer> vec2 = new Vector<>();

        for(int i = 0; i < vec.size(); i++){
            Integer item = null;
            for (int j = 0; j < vec.size(); j++){
                if(i != j){
                    if(item == null){
                        item = vec.get(j);
                    } else {
                        item *= vec.get(j);
                    }
                }
            }
            vec2.add(item);
        }
        System.out.println(vec2);
    }

}