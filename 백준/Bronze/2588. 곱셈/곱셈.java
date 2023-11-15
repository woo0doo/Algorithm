import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String lineA = bf.readLine();
        String lineB = bf.readLine();
        int a = Integer.parseInt(lineA);
        int b = Integer.parseInt(lineB);

        System.out.println(a * (b % 10));
        System.out.println(a * (b % 100 / 10));
        System.out.println(a * (b / 100));
        System.out.println(a * b);
    }
}