/**
 * 괄호 회전하기
 * 정상적인 괄호가 되려면 여는 괄호가 스택에 들어가고, 닫는 괄호가 보일 때마다
 * 스택 마지막 문자와 매칭이 되는지 확인해야한다.
 * 즉 (, {, [ 이 스택에 들어가면 된다. -> 제대로 된 괄호 배열인지를 알기 위해 ), }, ]가 stack.top()과
 * 매칭이 되지 않아도 그냥 push 하는 방식으로 진행했다.
 * 
 * 닫는 괄호와 매칭이 되는지 확인하기 위해 if문을 여러번 시도해야하기에 이를 HashMap으로 구성해 코드가 짧아질 수 있도록 했다.
 * 
 * 확인한 괄호는 뒤로 넘어가야한다. 이를 위해 그냥 문자를 x2를 하여 2중 for문으로 각 인덱스를 확인할 수 있게 구성했다.
 * 
 */

import java.util.*;

class Solution {
    
    public static HashMap<Character, Character> m = new HashMap<>();
    
    public int solution(String s) {
        int len = s.length();
        int cnt = 0;
        
        m.put(')', '(');        
        m.put('}', '{');
        m.put(']', '[');
        
        s += s;
        
        for(int i = 0; i < len; i++) {
            ArrayDeque<Character> Q = new ArrayDeque<>();
            for(int j = i; j < len + i; j++) {
                // System.out.println(Q.toString());
                
                // s[j] == ), }, ]
                if (!m.containsKey(s.charAt(j))) {
                    Q.add(s.charAt(j));
                }
                
                // s[j] == (, {, [
                else { // s[j] == ), }, ]
                    if(!Q.isEmpty() && Q.peekLast() == m.get(s.charAt(j))) {
                        Q.pollLast();
                    }
                    else Q.add(s.charAt(j));
                }
            }
            
            if (Q.isEmpty())  cnt += 1;
        }
        
        return cnt;
    }
}