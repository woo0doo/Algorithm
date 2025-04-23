import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(bf.readLine());

        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        String[][] graph = new String[R][C];
        int[][] visited = new int[R][C];
        boolean[][] waterVisited = new boolean[R][C];


        int DR=-1, DC=-1, SR=-1, SC=-1;

        Queue<int[]> q = new LinkedList<>();
        Queue<int[]> waterQ = new LinkedList<>();

        for (int r = 0; r < R; r++) {
            String[] split = bf.readLine().split("");
            for (int c = 0; c < C; c++) {
                graph[r][c] = split[c];

                if (split[c].equals("D")) {
                    DR = r;
                    DC = c;
                } else if (split[c].equals("S")) {
                    SR = r;
                    SC = c;
                    q.add(new int[]{SR,SC, 0});
                } else if (split[c].equals("*")) {
                    waterQ.add(new int[]{r,c});
                    waterVisited[r][c] = true;
                }
            }
        }

        // 물 검사해서

        int[] dr = new int[]{1,-1,0,0};
        int[] dc = new int[]{0,0,1,-1};
        int dayCnt = 0;

        while (!q.isEmpty()) {
            int[] poll = q.poll();
            int r = poll[0];
            int c = poll[1];
            int cnt = poll[2];

            if (cnt > dayCnt) {
                int size = waterQ.size();
                for (int j = 0; j < size; j++) {
                    int[] waterPoll = waterQ.poll();
                    int waterR = waterPoll[0];
                    int waterC = waterPoll[1];

                    for (int i = 0; i < dr.length; i++) {
                        if (waterR + dr[i] >= 0 && waterR + dr[i] < R &&
                                waterC + dc[i] >= 0 && waterC + dc[i] < C &&
                                !graph[waterR + dr[i]][waterC + dc[i]].equals("X") &&
                                !graph[waterR + dr[i]][waterC + dc[i]].equals("D") &&
                                !waterVisited[waterR + dr[i]][waterC + dc[i]]) {
                            waterVisited[waterR + dr[i]][waterC + dc[i]] = true;
                            waterQ.add(new int[]{waterR + dr[i], waterC + dc[i]});
                        }
                    }

                }
                dayCnt = cnt;
            }

            if (!waterVisited[r][c]) {
                for (int i = 0; i < dr.length; i++) {
                    if (r + dr[i] >= 0 && r + dr[i] < R &&
                        c + dc[i] >= 0 && c + dc[i] < C &&
                        !graph[r + dr[i]][c + dc[i]].equals("X") &&
                        visited[r + dr[i]][c + dc[i]] == 0) {
                        visited[r + dr[i]][c + dc[i]] = visited[r][c] + 1;
                        q.add(new int[]{r + dr[i], c + dc[i], cnt+1});
                    }
                }
            }



        }

        if (visited[DR][DC] == 0) {
            System.out.println("KAKTUS");
        } else {
            System.out.println(visited[DR][DC]);
        }

    }
}