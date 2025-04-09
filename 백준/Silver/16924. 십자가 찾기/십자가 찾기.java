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

        String[][] graph = new String[N][M];
        boolean[][] visited = new boolean[N][M];
        List<int[]> result = new ArrayList<>();


        for (int n = 0; n < N; n++) {
            String[] split = bf.readLine().split("");
            for (int m = 0; m < M; m++) {
                graph[n][m] = split[m];
                if (split[m].equals(".")) {
                    visited[n][m] = true;
                } else {
                    visited[n][m] = false;
                }
            }
        }

        int min = Math.min(N, M);

        for (int n = 0; n < N; n++) {
            for (int m = 0; m < M; m++) {
                if (graph[n][m].equals("*")){
                    for (int l = 1; l < min; l++) {
                        boolean isCross = checkCross(graph, n, m, N, M, l);
                        if (isCross) {
                            visited = visitedCross(visited, n, m, l);
                            int[] arr = {n+1, m+1, l};
                            result.add(arr);
                        } else {
                            break;
                        }
                    }
                }
            }
        }

        boolean flag = true;

        for (int n = 0; n < N; n++) {
            for (int m = 0; m < M; m++) {
                if (!visited[n][m]) {
                    flag = false;
                    break;
                }
            }
        }

        if (flag) {
            System.out.println();
            StringBuilder sb = new StringBuilder();
            sb.append(result.size()).append("\n");
            for (int i=0; i < result.size(); i++) {
                sb.append(result.get(i)[0]).append(" ").append(result.get(i)[1]).append(" ").append(result.get(i)[2]).append("\n");
            }
            System.out.println(sb);
        } else {
            System.out.println("-1");
        }

    }

    public static boolean checkCross(String[][] graph,int n, int m, int N, int M, int length) {
        if (n-length < 0 || m-length < 0 || n + length >= N || m + length >= M) {
            return false;
        }

        if (graph[n-length][m].equals(".") ||
                graph[n][m-length].equals(".") ||
                graph[n][m+length].equals(".") ||
                graph[n+length][m].equals(".")) {
            return false;
        }
        return true;
    }

    public static boolean[][] visitedCross(boolean[][] visited, int n, int m,int length) {
        visited[n-length][m] = true;
        visited[n][m-length] = true;
        visited[n][m+length] = true;
        visited[n+length][m] = true;
        visited[n][m] = true;

        return visited;
    }

}