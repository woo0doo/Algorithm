import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int[] dl = new int[]{-1,1,0,0,0,0};
        int[] dr = new int[]{0,0,-1,1,0,0};
        int[] dc = new int[]{0,0,0,0,-1,1};

        while (true) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int L = Integer.parseInt(st.nextToken());
            int R = Integer.parseInt(st.nextToken());
            int C = Integer.parseInt(st.nextToken());

            Queue<int[]> q = new LinkedList<>();

            if (L == 0 && R == 0 && C == 0) {
                break;
            }

            String[][][] graph = new String[L][R][C];
            int[][][] visited = new int[L][R][C];

            int[] endPoint = new int[3];

            for (int l = 0; l < L; l++) {
                for (int r = 0; r < R; r++) {
                    String[] split = bf.readLine().split("");
                    for (int c = 0; c < C; c++) {
                        if (split[c].equals("S")) {
                            q.add(new int[]{l, r, c});
                        } else if (split[c].equals("E")) {
                            endPoint = new int[]{l,r,c};
                        }
                        graph[l][r][c] = split[c];
                    }
                }
                bf.readLine();
            }

            while (!q.isEmpty()) {
                int[] poll = q.poll();
                int l = poll[0];
                int r = poll[1];
                int c = poll[2];

                for (int i = 0; i < dl.length; i++) {
                    if (l + dl[i] < L && l + dl[i] >= 0 &&
                        r + dr[i] < R && r + dr[i] >= 0 &&
                        c + dc[i] < C && c + dc[i] >= 0 &&
                        visited[l + dl[i]][r + dr[i]][c + dc[i]] == 0 &&
                        !graph[l + dl[i]][r + dr[i]][c + dc[i]].equals("#")) {
                        visited[l + dl[i]][r + dr[i]][c + dc[i]] = visited[l][r][c] + 1;
                        q.add(new int[]{l + dl[i], r + dr[i], c + dc[i]});
                    }
                }
            }
            if (visited[endPoint[0]][endPoint[1]][endPoint[2]] == 0) {
                System.out.println("Trapped!");
            } else {
                System.out.printf("Escaped in %d minute(s).\n", visited[endPoint[0]][endPoint[1]][endPoint[2]]);
            }

        }

    }

}