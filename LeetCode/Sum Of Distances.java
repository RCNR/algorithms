/**
 * Sum Of Distances 2615
 * 배열이 주어지고 각 원소마다 같은 원소와의 거리의 합을 구하는 문제
 * 
 * 완전탐색으로 풀면 최대 길이가 10^5이므로 O(n^2)으로 시간초과가 발생한다.
 * 따라서, 같은 원소끼리의 인덱스들을 모아서 계산하는 방법으로 풀기
 * 1. 같은 원소끼리의 인덱스들을 모은다.
 * 2. 각 원소마다 왼쪽과 오른쪽의 거리의 합을 구한다.
 *   - 왼쪽의 거리의 합은 (targetNum * j) - leftSum으로 구할 수 있다.
 *  - 오른쪽의 거리의 합은 rightSum - (targetNum * (m-j-1))으로 구할 수 있다.
 * 3. 왼쪽과 오른쪽의 거리의 합을 더해서 res에 넣는다.
 * 4. res 반환
 * 
 * nums[i] 값이 10^9까지 가능하므로, long 타입 생각해야한다.
 */

import java.util.*;

class Solution {
    public long[] distance(int[] nums) {

        int n = nums.length;
        long[] res = new long[n];

        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }

        for (List<Integer> idxsNum : map.values()) {
            int m = idxsNum.size();
            long total = 0;
            for (int idx : idxsNum) total += idx;
            long rightSum = total;
            long leftSum = 0;

            for (int j = 0; j < m; j++) {
                int targetNum = idxsNum.get(j);

                // rightSum에서 제외
                rightSum -= targetNum;

                // leftDist 값 구하기
                long leftDist = ((long)targetNum * j) - leftSum;

                // rightDist 값 구하기
                long rightDist = rightSum - ((long)targetNum * (m-j-1));

                // rightDist, leftDist 합치고 res에 넣기
                res[targetNum] = leftDist + rightDist;

                // leftSum 갱신
                leftSum += targetNum;
            }
        }
        return res;
    }
}