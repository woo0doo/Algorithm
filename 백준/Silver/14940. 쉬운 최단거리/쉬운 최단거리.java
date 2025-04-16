import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] graph = new int[N][M];
        int[][] visited = new int[N][M];
        int startIndexN = -1;
        int startIndexM = -1;

        for (int n = 0; n < N; n++) {
            String[] split = bf.readLine().split(" ");
            for (int m = 0; m < M; m++) {
                int value = Integer.parseInt(split[m]);
                graph[n][m] = value;
                if (value == 2) {
                    startIndexN = n;
                    startIndexM = m;
                }
            }
        }

        Queue<int[]> q = new LinkedList<>();
        int[] ints = {startIndexN, startIndexM};
        q.add(ints);
        int[] dN = {0, 0, 1, -1};
        int[] dM = {-1, 1, 0, 0};

        while (!q.isEmpty()) {
            int[] poll = q.poll();
            int y = poll[0];
            int x = poll[1];

            for (int i = 0; i < 4; i++) {
                if (y + dN[i] >= 0 && y + dN[i] < N && x + dM[i] >= 0 && x + dM[i] < M && graph[y + dN[i]][x + dM[i]] != 0) {
                    if (visited[y + dN[i]][x + dM[i]] == 0) {
                        visited[y + dN[i]][x + dM[i]] = visited[y][x] + 1;
                        q.add(new int[]{y + dN[i], x + dM[i]});
                    }
                }
            }
        }

        visited[startIndexN][startIndexM] = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (graph[i][j] == 1 && visited[i][j] < 1) {
                    visited[i][j] = -1;
                }
            }
        }


        for (int i = 0; i < N-1; i++) {
            for (int j = 0; j < M - 1; j++) {
                System.out.print(visited[i][j]+ " ");
            }
            System.out.print(visited[i][M-1]);
            System.out.println();
        }

        for (int j = 0; j < M-1; j++) {
            System.out.print(visited[N-1][j] + " ");
        }
        System.out.print(visited[N-1][M-1]);


    }

}