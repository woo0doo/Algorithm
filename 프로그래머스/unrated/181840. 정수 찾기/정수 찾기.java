import java.util.stream.IntStream;

class Solution {
    public int solution(int[] numList, int n) {
        return IntStream.of(numList).anyMatch(num -> num == n) ? 1 : 0;
    }
}
