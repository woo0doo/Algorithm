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
        int K = Integer.parseInt(st.nextToken());

        Character[][] graph = new Character[N][M];

        for (int n = 0; n < N; n++) {
            String[] split = bf.readLine().split("");
            for (int m = 0; m < M; m++) {
                graph[n][m] = split[m].charAt(0);
            }
        }

        // K X K 로 짜르고 나눴을 때, 가장 많이 존재하는 대문자로 선정하는 식으로 선택하면 될 것 같다.
        Character[][] result = new Character[K][K];

        for (int blockN = 0; blockN < K; blockN++) {
            for (int blockM = 0; blockM < K; blockM++) {
                int[] cnt = new int[26];
                for (int n = 0; n < N/K; n++) {
                    for (int m = 0; m < M/K; m++) {
                        int val = graph[n*K + blockN][m*K + blockM] - 65;
                        cnt[val] += 1;
                    }
                }
                int maxCnt = -1;
                int maxIndex = -1;
                for (int i = 0; i < cnt.length; i++) {
                    if (maxCnt < cnt[i]) {
                        maxIndex = i+17;
                        maxCnt = cnt[i];
                    }
                }

                result[blockN][blockM] = (char)(maxIndex + '0');
            }
        }

        int changedCnt = 0;

        for (int blockN = 0; blockN < K; blockN++) {
            for (int blockM = 0; blockM < K; blockM++) {
                for (int n = 0; n < N/K; n++) {
                    for (int m = 0; m < M/K; m++) {
                        if (graph[n*K + blockN][m*K + blockM] != result[blockN][blockM]) {
                            graph[n*K + blockN][m*K + blockM] = result[blockN][blockM];
                            changedCnt += 1;
                        }
                    }
                }
            }
        }

        System.out.println(changedCnt);

        for (int n = 0; n < N; n++) {
            for (int m = 0; m < M; m++) {
                System.out.print(graph[n][m]);
            }
            System.out.println();
        }

    }

}