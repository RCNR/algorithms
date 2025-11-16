/**
 * 완전 탐색을 통해 각 위치에서 가능한 매트 크기를 확인하는 방식으로 문제를 해결한다
 * 1. 매트 크기를 내림차순으로 정렬하여 큰 매트부터 확인한다
 * 2. 공원 배열을 순회하며 빈 공간("-1")을 찾는다
 * 3. 빈 공간을 찾으면 해당 위치에서 매트를 놓을 수 있는지 확인하는 함수를 호출한다
 * 4. 매트를 놓을 수 있으면 해당 매트 크기를 반환한다
 */

import java.util.*;

class Solution {
    public int solution(int[] mats, String[][] park) {
        
        Integer[] new_mats = Arrays.stream(mats).boxed().toArray(Integer[]::new);
        Arrays.sort(new_mats, Collections.reverseOrder());

        
        for(int m : new_mats) {
            for(int i = 0; i < park.length; i++) {
                for(int j = 0; j < park[i].length; j++) {
                    if (park[i][j].equals("-1")) {
                        if(func(i, j, m, park)) {
                            return m;
                        }
                    }
                }
            }
        }
        
        return -1;
    }
    
    public boolean func(int x, int y, int M, String[][] park) {
        
        if (!(x + M - 1 < park.length) || !(y + M - 1 < park[x].length)) return false;
        
          for (int i = 0; i < M; i++) {
              for (int j = 0; j < M; j++) {
                    if (!park[x + i][y + j].equals("-1")) return false;

              } 
          }
          
        return true;
    }
}


