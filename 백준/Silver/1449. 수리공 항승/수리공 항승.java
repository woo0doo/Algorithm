import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        ArrayList<Integer> arr = new ArrayList<>();

        StringTokenizer st2 = new StringTokenizer(bf.readLine());

        for (int i = 0; i < N; i++) {
            arr.add(Integer.parseInt(st2.nextToken()));
        }

        Collections.sort(arr);

        int cnt = 0;
        int beforeValue = 0;

        for (int i = 0; i < N; i++) {
            Integer value = arr.get(i);
            if (beforeValue == 0) {
                cnt += 1;
                beforeValue = value;
            } else if (value - beforeValue + 1 <= L) {
                continue;
            } else {
                cnt += 1;
                beforeValue = value;
            }
        }

        System.out.println(cnt);


    }

}