#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    // 그리디 관점 : 현 시점에서 핀 꽃 중 가장 마지막에 지는 꽃
    // 수가 적어서 정렬하지 않아도 OK
    int n; cin >> n;

    vector<pair<int,int>> v;

    for(int i=0; i<n; i++) {
        int st_m, st_d, en_m, en_d;
        cin >> st_m >> st_d >> en_m >> en_d;
        v.push_back({st_m*100+st_d, en_m*100+en_d}); // 시작, 지는 날 (실제 피는 날 : 시작 ~ 지는 날 - 1)
    }

    int time = 301;
    int cnt = 0;

    while(time < 1201) {
        int goodBye_flower = time;
        for(int i = 0 ; i<n; i++) {
            if(v[i].first <= time && v[i].second > goodBye_flower) {
                goodBye_flower = v[i].second;
            }
        }

        if(goodBye_flower == time) {
            cout << 0;
            return 0;
        }

        time = goodBye_flower;
        cnt++;
    }
    cout << cnt;

}