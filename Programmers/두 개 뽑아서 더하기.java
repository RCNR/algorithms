import java.io.*;
import java.util.*;
import java.util.stream.*;

class Solution {

    // 모든 두 수의 합을 Set을 이용해 구하고 정렬한다

    public int[] solution(int[] numbers) {
        
        HashSet<Integer> s = new HashSet<>();

        for(int i = 0; i < numbers.length; i++) {
            for(int j = i+1; j < numbers.length; j++) {
                s.add(numbers[i] + numbers[j]);
            }
        }

        return s.stream().sorted().mapToInt(Integer::intValue).toArray();
        
    }
}