#include <bits/stdc++.h>

using namespace std;

string ary[502];
vector<int> cnt(27);
int sum;

int main() {
    int n, m, k;
    cin >> n >> m >> k;
    
    for(int i = 0; i < n; i++) {
        string str; cin >> str;
        ary[i] = str;
    }

    int num = (n * m) / (k*k);

    for(int x = 0; x < k; x++) {
        for(int y = 0; y < k; y++) {

            fill(cnt.begin(), cnt.end(), 0);
            for(int i = 0; i < n - k + 1; i+=k) {
                for(int j = 0; j < m - k + 1; j+=k) {
                    char c = ary[i+x][j+y];
                    cnt[c-'A'] += 1;
                }
            }

            int max_cnt = *max_element(cnt.begin(), cnt.end());
            sum += num - max_cnt; // 젤 많이 나온 알파벳은 그대로 나머지 애들은 바꿔야함
            int max_index = max_element(cnt.begin(), cnt.end()) - cnt.begin();
            char change_char = max_index + 'A';

            for(int i = 0; i < n - k + 1; i += k) {
                for(int j = 0; j < m - k + 1; j += k) {
                    ary[i+x][j+y] = change_char;
                }
            }
        }
    }
    cout << sum << '\n';
    for(int i =0;i<n;i++) {
        cout << ary[i] << endl;
    }
}
