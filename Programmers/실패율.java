/**
 * 이분탐색을 사용한 코드
 * stages 배열(길이 M)을 정렬 - O(MlogM)
 * lower,upperBound - O(logM) -> 이를 N번 하기에 O(NlogM)
 * v 정렬 - O(NlogN)
 * 총 O(MlogM + NlogM)이 된다.
 * 비효율적이며 시간이 오래걸린다.
 *  */

import java.util.*;
import java.io.*;

class Pair<A, B> {
    public A first;
    public B second;

    public Pair(A first, B second) {
        this.first = first;
        this.second = second;
    }
}

class Solution {
    
    public int[] solution(int N, int[] stages) {
        int[] answer = {};
        
        int[] board = new int[N+3];
        for(int i = 0; i < N; i++) {
            board[i] = i + 1;
        }
        
        Arrays.sort(stages);
        ArrayList<Pair<Double, Integer>> v = new ArrayList<>();
        
        for(int i = 0; i < N; i++) {
            int num = board[i];
            int low = lowerBound(num, stages);
            int upper = upperBound(num, stages);
            
            double res = 0.0;
            res = (double)(upper - low) / (stages.length - low);
            if (Double.isNaN(res)) {
                res = 0.0;
            }
            
            System.out.println(num + " " + res + " Low : " + low + " Upper : " + upper);
            
            int index = i+1;
            v.add(new Pair<>(res, index));
        }

        v.sort(Comparator.comparing(p -> p.first, Comparator.reverseOrder()));
        
        
        return v.stream().mapToInt(p -> p.second).toArray();
        
    }
    
    private static int lowerBound(int num, int[] stages) {
        int l = -1;
        int r = stages.length;
        
        while (l + 1 < r) {
            int mid = (l+r) / 2;
            if (stages[mid] < num) l = mid;
            else r = mid;
        }
        
        return r;
    }
    
    private static int upperBound(int num, int[] stages) {
        int l = -1; 
        int r = stages.length;
        
        while (l + 1 < r) {
            int mid = (l+r) / 2;
            if (stages[mid] > num) r = mid;
            else l = mid;
        }
        
        return r;
    }
}


/**
 * board 배열을 순회해 각 스테이지에 머물러 있는 사용자 수 계산 (길이 M의 stages 순회) : O(M)
 * 각 스테이지 실패율 계산 : O(N)
 * 실패율 기준 정렬 : O(NlogN)
 * 큰 항만 고려해서 -> O(M + NlogN)
 * 
 * 카운팅 배열을 이용한 풀이.
 */

import java.util.*;
import java.io.*;

class Solution {
    
    public int[] solution(int N, int[] stages) {
        int[] answer = {};
        
        int[] board = new int[N+3];
        for(int i = 0; i < stages.length; i++) {
            board[stages[i]] += 1; // board는 stages를 도전하고 있는 인원의 수
        }
        
        HashMap<Integer, Double> m = new HashMap<>();
        
        int cnt = stages.length; // 인원
        
        // 실패율 계산
        for(int i = 1; i <= N; i++) {
            if(board[i] == 0) m.put(i, 0.0);
            else {
                m.put(i, (double)board[i] / cnt);
                cnt -= board[i]; // 현재 스테이지 인원을 감소시켜야함
            }
        }
        
        // 실패율(key:value 중 value) 기준 내림차순
       return m.entrySet()
            .stream()
            .sorted((o1, o2) -> Double.compare(o2.getValue(), o1.getValue()))
            .mapToInt(map -> map.getKey())
            .toArray();
    }
    
    
}