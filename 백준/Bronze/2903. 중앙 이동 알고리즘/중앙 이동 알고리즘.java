import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int cnt=3;
        for (int i=1;i<n;i++) {
            cnt+=cnt-1;
        }
        System.out.println(cnt*cnt);
    }
}