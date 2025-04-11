import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String s1 = bf.readLine();
        int dotCnt = 0;
        for (int i = s1.length() - 1; i >= 0; i--) {
            if (s1.charAt(i) == '.') {
                dotCnt += 1;
            } else {
                break;
            }
        }
        String[] split = s1.split("\\.");

        boolean flag = true;

        List<String> result = new ArrayList<>();

        for (String s : split) {
            String a = "";
            int aCnt = 0;
            int bCnt = 0;
            if (s.length() % 2 == 1) {
                flag = false;
                break;
            } else {
                aCnt += s.length() / 4;
                bCnt += s.length() % 4;
            }
            for (int i = 0; i < aCnt; i++) {
                a += "AAAA";
            }
            for (int j = 0; j < bCnt; j++) {
                a += "B";
            }
            result.add(a);
        }

        if (flag) {
            System.out.print(String.join(".", result));
            for (int i = 0; i < dotCnt; i++) {
                System.out.print(".");
            }
        } else {
            System.out.println(-1);
        }

    }

}