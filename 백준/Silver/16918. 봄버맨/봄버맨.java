import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(bf.readLine());

        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        String[][] graph = new String[R][C];

        for (int i = 0 ; i < R; i++) {
            String[] arr = bf.readLine().split("");
            graph[i] = arr;
        }

        String[][] changedGraph = new String[R][C];

        for (int r=0; r<R; r++) {
            changedGraph[r] = graph[r].clone();
        }

        for (int j = 1; j < N+1; j++) {
            if (j == 1) {
                continue;
            } else if (j%2 == 0) {
                for (int r=0; r<R; r++) {
                    graph[r] = changedGraph[r].clone();
                }

                for (int r = 0; r < R; r++) {
                    for (int c = 0; c < C; c++) {
                        changedGraph[r][c] = "O";
                    }
                }
            } else {
                for (int r = 0; r < R; r++) {
                    for (int c = 0; c < C; c++) {
                        if (graph[r][c].equals("O")) {
                            changedGraph = bomb(changedGraph, r, c, R, C);
                        }
                    }
                }
            }
        }

        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                System.out.print(changedGraph[r][c]);
            }
            System.out.println();
        }
    }

    public static String[][] bomb(String[][] changedGraph, int r, int c, int R, int C) {
        if (r == 0 && R != 1) {
            changedGraph[r+1][c] = ".";
        } else if (r == R-1) {
            changedGraph[r-1][c] = ".";
        } else {
            changedGraph[r+1][c] = ".";
            changedGraph[r-1][c] = ".";
        }

        if (c == 0 && C != 1) {
            changedGraph[r][c+1] = ".";
        } else if (c == C-1) {
            changedGraph[r][c-1] = ".";
        } else {
            changedGraph[r][c+1] = ".";
            changedGraph[r][c-1] = ".";
        }

        changedGraph[r][c] = ".";

        return changedGraph;
    }

}