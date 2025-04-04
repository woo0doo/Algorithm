import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.
        BufferedReader buffer = new BufferedReader(new InputStreamReader(System.in));

        int[][] numArr = new int[5][5];
        int[] inputArr = new int[25];
        boolean[][] checkArr = new boolean[5][5];
        // 빙고판입력
        for(int i = 0; i < 5; i++) {
            String[] input = buffer.readLine().split(" ");
            for(int k = 0; k < input.length; k++) {
                numArr[i][k] = Integer.parseInt(input[k]);
            }
        }
        // 입력배열 입력
        for(int i = 0; i < 5; i++) {
            String[] input = buffer.readLine().split(" ");
            for(int k = 0; k < input.length; k++) {
                // 0 1 2 3 4
                // 5 6 7 8 9
                inputArr[(i * 5 + k)] = Integer.parseInt(input[k]);
            }
        }

        int result = 0;

        for (int num : inputArr) {
            result += 1;
            for (int i = 0; i < numArr.length; i++) {
                for (int j = 0; j < numArr[i].length; j++) {
                    if (num == numArr[i][j]) {
                        checkArr[i][j] = true;
                    }
                }
            }
            int bingoCount = checkRow(checkArr) + checkColumn(checkArr) + checkDiagonal(checkArr);
            if(bingoCount >= 3) {
                System.out.println(result);
                return;
            }
        }

    }

    public static int checkRow(boolean[][] checkArr) {
        int bingoCount = 0;
        for(int i = 0; i < checkArr.length; i++) {
            boolean check = true;
            for (int k = 0; k < checkArr[i].length; k++) {
                if(!checkArr[i][k]) {
                    check = false;
                    break;
                }
            }
            if(check) {
                bingoCount++;
            }
        }
        return bingoCount;
    }

    public static int checkColumn(boolean[][] checkArr) {
        int bingoCount = 0;
        for(int i = 0; i < checkArr.length; i++) {
            boolean check = true;
            for (int k = 0; k < checkArr[i].length; k++) {
                if(!checkArr[k][i]) {
                    check = false;
                    break;
                }
            }
            if(check) {
                bingoCount++;
            }
        }
        return bingoCount;
    }

    public static int checkDiagonal(boolean[][] checkArr) {
        int bingoCount = 0;
        boolean rightCheck = true;
        for(int i = 0; i < checkArr.length; i++) {
            if(!checkArr[i][i]) {
                rightCheck = false;
                break;
            }
        }
        if(rightCheck) {
            bingoCount++;
        }

        boolean leftCheck = true;
        for (int j = 0; j < checkArr.length; j++) {
            if(!checkArr[j][checkArr.length - 1 - j]) {
                leftCheck = false;
                break;
            }
        }
        if(leftCheck) {
            bingoCount++;
        }
        return bingoCount;
    }
}