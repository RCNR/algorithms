// 바탕화면 정리
// 왼쪽 위에서 오른쪽 아래로 스크롤 해서 파일을 지워야함 -> 단, 가장 적은 범위 안에서
// 가장 왼쪽의 y, 위쪽의 x, 밑쪽의 x, 오른쪽의 y 를 구하면 된다.

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> wallpaper) {
    vector<int> answer;
    
    int left = 52;
    int up = 52;
    int bottom = -1;
    int right = -1;
    int row = wallpaper.size();
    int col = wallpaper[0].size();
    
    for(int i = 0; i < row; i++) {
        for(int j = 0; j < col; j++) {
            if(wallpaper[i][j] == '#') {
                if(j < left) left = j;
                if(i < up) up = i;
                if(i > bottom) bottom = i;
                if(j > right) right = j;
            }
        }
    }
    
    answer.push_back(up);
    answer.push_back(left);
    answer.push_back(bottom + 1);
    answer.push_back(right + 1);
    return answer;
}