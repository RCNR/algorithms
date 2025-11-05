/**
 * HashSet을 이용한 중복처리
 * 
 * 문제는 중복 경로를 제외하고 이동한 길이를 구해야한다.
 * 중복을 포함하지 않는다는 조건이 있으니 해시셋을 생각해본다.
 * A -> B를 갔는데, 후에 A -> B 갔다면 중복 경로이다
 * A -> B를 갔는데, 후에 B -> A 갔다면 중복 경로이다
 * 처음부터 A -> B , B -> A 간 경우를 모두 구하고 마지막에 /2를 해버리면 굳이 중복 경로를 생각하지 않아도 된다.
 */

import java.io.*;
import java.util.*;

class Solution {
    
    public static int cur_x = 5;
    public static int cur_y = 5;
    public static HashSet<String> location = new HashSet<>();
    public static HashMap<String, int[]> dir = new HashMap<>();
    
    
    public int solution(String dirs) {
        
        
        dir.put("L", new int[]{-1, 0});
        dir.put("R", new int[]{1, 0});
        dir.put("U", new int[]{0, 1});
        dir.put("D", new int[]{0, -1});
        
       
                
        for(int i = 0; i < dirs.length(); i++) {
            char c = dirs.charAt(i);
            func(String.valueOf(c));
        }
        
        return location.size() / 2;
    }
                
    public static void func(String c) {
        
        int dx = dir.get(String.valueOf(c))[0];
        int dy = dir.get(String.valueOf(c))[1];
        
        int nx = cur_x + dx;
        int ny = cur_y + dy;
        
        
        if(nx < 0 || nx > 10 || ny < 0 || ny > 10) return;
        
        location.add(cur_x + " "  + cur_y + " " + nx +  " " + ny);
        location.add(nx + " " + ny + " " + cur_x + " " + cur_y);
        
        cur_x = nx; cur_y = ny;
    }
}