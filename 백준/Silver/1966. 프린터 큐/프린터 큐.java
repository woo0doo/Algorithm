import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(bf.readLine());
        int n = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {

            st = new StringTokenizer(bf.readLine());
            int M = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(bf.readLine());
            Queue<Map<Integer, Boolean>> q = new LinkedList<>();
            List<Integer> numArr = new ArrayList<>();
            for (int j = 0; j < M; j++) {
                int value = Integer.parseInt(st.nextToken());
                numArr.add(value);
                Map<Integer, Boolean> hashMap = new HashMap<>();
                if (j == N) {
                    hashMap.put(value, true);
                } else {
                    hashMap.put(value, false);
                }
                q.add(hashMap);
            }

            int cnt = 0;
            boolean flag = true;

            while (flag) {
                Collections.sort(numArr, Collections.reverseOrder());
                Integer max = numArr.get(0);
                Map<Integer, Boolean> poll = q.poll();
                for (Map.Entry<Integer, Boolean> entry : poll.entrySet()) {
                    if (entry.getKey().equals(max)) {
                        cnt += 1;

                        if (entry.getValue()) {
                            flag = false;
                            break;
                        }
                        numArr.remove(0);
                    } else {
                        q.add(poll);
                    }
                }
            }

            System.out.println(cnt);

        }
    }

}