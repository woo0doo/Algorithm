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
        int[][][] visited = new int[2][N][M];
        Queue<int[]> q = new LinkedList<>();

        for (int n = 0; n < N; n++) {
            String[] split = bf.readLine().split("");
            for (int m = 0; m < M; m++) {
                int i = Integer.parseInt(split[m]);
                graph[n][m] = i;
            }
        }

        q.add(new int[]{0,0,0});
        int[] dx = new int[]{1,-1,0,0};
        int[] dy = new int[]{0,0,1,-1};

        visited[0][0][0] = 1;

        while (!q.isEmpty()) {
            int[] poll = q.poll();
            int tn = poll[0];
            int tm = poll[1];
            int breakCnt = poll[2];

            for (int i = 0; i < dx.length; i++) {

                if (tn+dx[i] >= 0 && tn+dx[i] < N &&
                    tm+dy[i] >= 0 && tm+dy[i] < M &&
                    visited[breakCnt][tn+dx[i]][tm+dy[i]] == 0) {

                    if (graph[tn+dx[i]][tm+dy[i]] == 1) {
                        if (breakCnt == 1) {
                        } else {
                            visited[1][tn+dx[i]][tm+dy[i]] = visited[0][tn][tm] + 1;
                            q.add(new int[]{tn+dx[i], tm+dy[i], breakCnt+1});
                        }
                    } else {
                        visited[breakCnt][tn+dx[i]][tm+dy[i]] = visited[breakCnt][tn][tm] + 1;
                        q.add(new int[]{tn+dx[i], tm+dy[i], breakCnt});
                    }
                }
            }
        }

        if (visited[0][N-1][M-1] == 0 && visited[1][N-1][M-1] == 0) {
            System.out.println(-1);
        } else {
            if (visited[0][N-1][M-1] != 0 && visited[1][N-1][M-1] != 0) {
                System.out.println(Math.min(visited[0][N-1][M-1], visited[1][N-1][M-1]));
            } else if (visited[0][N-1][M-1] != 0) {
                System.out.println(visited[0][N-1][M-1]);
            } else {
                System.out.println(visited[1][N-1][M-1]);
            }
        }

    }

}