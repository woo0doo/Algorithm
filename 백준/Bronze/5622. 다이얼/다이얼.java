import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        char[] chars = s.toCharArray();

        int sum = 0;

        for (char c : chars) {
            if (c >= 'A' && c <= 'C') {
                sum += 3;
            } else if (c >= 'D' && c <= 'F'){
                sum +=4;
            } else if (c >= 'G' && c <= 'I'){
                sum +=5;
            }else if (c >= 'J' && c <= 'L'){
                sum +=6;
            }else if (c >= 'M' && c <= 'O'){
                sum +=7;
            }else if (c >= 'P' && c <= 'S'){
                sum +=8;
            }else if (c >= 'T' && c <= 'V'){
                sum +=9;
            }else if (c >= 'W' && c <= 'Z'){
                sum +=10;
            }
        }
        System.out.println(sum);
    }
}