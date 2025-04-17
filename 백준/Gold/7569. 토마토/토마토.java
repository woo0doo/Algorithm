import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int H = Integer.parseInt(st.nextToken());

        int[][][] graph = new int[H][N][M];
        int[][][] visited = new int[H][N][M];

        // H, N, M, DAY
        Queue<int[]> q = new LinkedList<>();

        for (int h = 0; h < H; h++) {
            for (int n = 0; n < N; n++) {
                String[] split = bf.readLine().split(" ");
                for (int m = 0; m < M; m++) {
                    int i = Integer.parseInt(split[m]);
                    if (i == 1) {
                        q.add(new int[]{h,n,m,1});
                    }
                    graph[h][n][m] = i;
                }
            }
        }

        int day = 0;

        while (!q.isEmpty()) {
            int[] poll = q.poll();
            int h = poll[0];
            int n = poll[1];
            int m = poll[2];
            int d = poll[3];

            int[] dh = new int[]{1,-1,0,0,0,0};
            int[] dn = new int[]{0,0,1,-1,0,0};
            int[] dm = new int[]{0,0,0,0,1,-1};

            for (int i = 0; i < dh.length; i++) {
                int th = h + dh[i];
                int tn = n + dn[i];
                int tm = m + dm[i];
                if (th >= 0 && th < H &&
                    tn >= 0 && tn < N &&
                    tm >= 0 && tm < M &&
                    graph[th][tn][tm] == 0) {
                    if (day < d) {
                        day = d;
                    }
                    graph[th][tn][tm] = 1;
                    q.add(new int[]{th, tn, tm, d+1});
                }
            }


        }

        boolean flag = true;

        for (int h = 0; h < H; h++) {
            for (int n = 0; n < N; n++) {
                for (int m = 0; m < M; m++) {
                    if (graph[h][n][m] == 0) {
                        flag = false;
                        break;
                    }
                }
            }
        }

        if (flag) {
            System.out.println(day);
        } else {
            System.out.println(-1);
        }

    }

}