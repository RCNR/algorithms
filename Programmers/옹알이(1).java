import java.util.*;
// replaceAll을 사용해 공백으로 만들어 버릴 시 생길 수 있는 반례
// "mayaa" -> "aya" 지우고 "ma"가 되어버려서 cnt++ 되어버림
class Solution {
    public int solution(String[] babbling) {

        
        String[] str = {"aya", "ye", "woo", "ma"};

        
        for(int i = 0; i < babbling.length; i++) {
            String c = babbling[i];
            for(int j = 0; j < str.length; j++) {
                if(c.contains(str[j])) {
                    babbling[i] = babbling[i].replaceAll(str[j], "2");
                }
            }
        }
        
        int cnt = 0;
        for(String ba: babbling) {
            if(ba.replaceAll("2", "").isEmpty()) {
                cnt += 1;
            }
        }
        return cnt;
    }
}