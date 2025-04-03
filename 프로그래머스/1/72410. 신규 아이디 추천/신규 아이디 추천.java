import java.util.*;
import java.io.*;


class Solution {
    public String solution(String new_id) {
        String answer = "";
        String result1 = new_id.toLowerCase();
        System.out.println(result1);
        
        String result2 = result1.replaceAll("[^a-z0-9-_.]",""); // 영문자와 숫자를 제외한 문자를 모두 0으로 치환
        System.out.println(result2);
        
        char before = 'a';
        
        String result3 = "";
        
        for(int i=0;i<result2.length();i++){
            char c = result2.charAt(i);
            if (before == '.' && c == '.') {
                continue;
            } else {
                result3 += c;
            }
            before = c;
        }
        
        System.out.println(result3);
        
        char first = result3.charAt(0); // a
        char last = result3.charAt(result3.length() - 1);
        String result4 = result3;
        if (result4.length() > 0 && last == '.') {
            result4 = result3.substring(0, result3.length() - 1);
            System.out.println(result4);
        }
        if (result4.length() > 0 && first == '.') {
            result4 = result4.substring(1);
        }
            
        System.out.println(result4);
        
        String result5 = result4;
        
        if (result5.length() == 0) {
            result5 = "a";
        }
        
        System.out.println(result5);
        
        String result6 = result5;
        
        if (result6.length() >= 16) {
            result6 = result6.substring(0,15);
            last = result6.charAt(result6.length() - 1);
            if (last == '.') {
                result6 = result6.substring(0, result6.length() - 1);
            }
        }
        
        System.out.println(result6);
        
        String result7 = result6;
        
        if (result7.length() <= 2) {
            while (result7.length() != 3) {
                last = result7.charAt(result7.length() - 1);
                result7 += last;
            }
        }
        
        System.out.println(result7);
        
        return result7;
    }
    
    
}