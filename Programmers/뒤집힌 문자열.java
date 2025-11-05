// String을 이용하기 보단 StringBuilder를 이용하는게 더 낫다.

class Solution {
    public String solution(String my_string) {
        
        return new StringBuilder(my_string).reverse().toString();
    }
}