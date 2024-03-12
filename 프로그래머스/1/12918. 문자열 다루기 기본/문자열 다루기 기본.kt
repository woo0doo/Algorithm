class Solution {
    fun solution(s: String): Boolean {
        var answer = true
        
        if( (s.length == 4) || (s.length == 6) ) {
            answer = s.all { it -> it.isDigit() }
        }
        else answer = false
        
        return answer
    }
}