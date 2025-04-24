import java.io.*;
import java.util.*;

public class Main {

    static int[] arr;
    static int[] output;
    static boolean[] visited;
    static int N;
    static int M;

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(bf.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N+1];
        visited = new boolean[N+1];
        output = new int[M+1];

        for (int i = 1 ; i < N+1; i++) {
            arr[i] = i;
        }

        permutation(0, N, M);

    }


    static void permutation(int depth, int n, int r) {
        if (depth == r) {
            for (int i = 0; i < r; i++) {
                System.out.print(output[i] + " ");
            }
            System.out.println();
            return;
        }

        // 0부터 n까지 반복
        for (int i = 1; i < n+1; i++) {
            // 방문하지 않은 값이면 넣기
            if (!visited[i]) {
                visited[i] = true; // 방문 처리
                output[depth] = arr[i]; // 현재 depth를 인덱스로 사용
                permutation(depth + 1, n, r); // depth + 1를 전달
                visited[i] = false; // 다음 순열을 뽑기위해 방문처리 제거
            }
        }
    }

}