import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int max =0, num = 0, row = 1, column=1;

        for (int i=1; i<=81;i++) {
            num = sc.nextInt();
            if (num>max) {
                max = num;
                row = i%9==0? i/9 :i/9+1;
                column = i%9==0? 9 :i%9;
            }
        }

        System.out.println(max);
        System.out.println(row +" " + column);

    }
}