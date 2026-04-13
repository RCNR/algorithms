/*
  동영상 길이, 현재 위치, 오프닝 구간 시작과 끝, 명령어 배열이 주어질 때, 명령어를 수행한 후의 위치를 구하는 문제
  commands에서 값을 꺼내 명령어가 prev면 10초 전으로 이동, next면 10초 후로 이동
  이동한 위치가 오프닝 구간에 있다면 자동으로 오프닝 구간 끝으로 이동
  이동한 위치가 동영상 길이보다 크면 동영상 길이로 이동, 0보다 작으면 0으로 이동

  문자열로 구성된 시간 형태를 숫자로 변환하여 계산 후 다시 문자열로 변환하는 방식으로 풀이
*/

import java.util.*;
import java.io.*;

class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        String cur = pos;
        
        for (String s : commands) {
             // 오프닝 구간이면 자동으로 끝나는 위치로
            cur = opening(cur, op_start, op_end);
            
            // 간격 조정
            cur = check(cur, s, video_len);
            
            // 오프닝 구간이면 자동으로 끝나는 위치로
            cur = opening(cur, op_start, op_end);
            
        }
        
        return cur;
    }
    
    static String opening(String now, String start, String end) {
        int numNow = toSeconds(now);
        int numStart = toSeconds(start);
        int numEnd = toSeconds(end);

        if (numStart <= numNow && numNow <= numEnd) {
            return toTime(numEnd);
        }
        return now;
    }
    
    static String check(String now, String command, String video_len) {
    
        int numNow = toSeconds(now);
      
        int video_len_num = toSeconds(video_len); 

        if (command.equals("prev")) { // 10초 전으로 이동

            numNow = Math.max(numNow - 10, 0);
        }

        else { // next 10초 후로 이동
            numNow = Math.min(numNow + 10, video_len_num);
        }
        
        String s = toTime(numNow);
        return s;
    
    }
    
    static int toSeconds(String time) {
        String[] times = time.split(":");
        
        return Integer.parseInt(times[0]) * 60 + Integer.parseInt(times[1]);
    }
    
    static String toTime(int seconds) {
        
        return String.format("%02d:%02d", seconds / 60, seconds % 60);
    }
}