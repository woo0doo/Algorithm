import java.io.*;
import java.util.*;

public class Main {
    static class Node implements Comparable<Node> {
        int v, cost;
        public Node(int v, int cost) { this.v = v; this.cost = cost; }
        @Override
        public int compareTo(Node o) { return this.cost - o.cost; }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(bf.readLine());
        int M = Integer.parseInt(bf.readLine());

        List<Node>[] graph = new ArrayList[N+1];
        for (int i = 1; i <= N; i++) graph[i] = new ArrayList<>();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(bf.readLine(), " ");
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph[u].add(new Node(v, w));
        }

        st = new StringTokenizer(bf.readLine(), " ");
        int startCity = Integer.parseInt(st.nextToken());
        int endCity   = Integer.parseInt(st.nextToken());

        // dijkstra
        final int INF = Integer.MAX_VALUE;
        int[] dist = new int[N+1];
        boolean[] visit = new boolean[N+1];
        Arrays.fill(dist, INF);

        PriorityQueue<Node> pq = new PriorityQueue<>();
        dist[startCity] = 0;
        pq.add(new Node(startCity, 0));

        while (!pq.isEmpty()) {
            Node now = pq.poll();
            if (visit[now.v]) continue;       // 중복 건너뛰기
            visit[now.v] = true;

            if (now.v == endCity) break;      // 목표 도달 시 종료

            for (Node nxt : graph[now.v]) {
                if (!visit[nxt.v] && dist[nxt.v] > dist[now.v] + nxt.cost) {
                    dist[nxt.v] = dist[now.v] + nxt.cost;
                    pq.add(new Node(nxt.v, dist[nxt.v]));
                }
            }
        }

        System.out.println(dist[endCity]);
    }
}