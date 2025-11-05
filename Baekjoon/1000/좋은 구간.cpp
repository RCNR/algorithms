// 1059, 좋은 구간
// 기준 되는 수보다 작은 수, 큰 수의 개수 사용 -> 경우의 수가 어떻게 이루어지는 확인 필요

#include <bits/stdc++.h>
#define rep(i, a, n) for(auto i = a; i < n; i++)
#define REP(i, a, n) for(auto i = a; i <= n; i++)
#define X first
#define Y second
#define pb push_back
#define pii pair<int, int>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(NULL), cout.tie(NULL)
#define endl '\n'

using namespace std;

int board[55];
int n, num;

int main(void) {
    FAST_IO;

	cin >> n;
	rep(i, 0, n) {
		cin >> board[i];
	}
	sort(board, board + n);
	cin >> num;
	rep(i, 0, n) {
		if (board[i] == num) {
			cout << 0; return 0;
		}
	}

	int min_num = 0;
	int max_num = 0;
	for (int i = 0; i < n; i++) {
		if (board[i] < num) {
			min_num = board[i];
		}
		else if (board[i] > max_num && max_num == 0) {
			max_num = board[i];
		}
	}
	min_num++;
	max_num--;
	//cout << min_num << ' ' << max_num << endl;
	int small_cnt = num - min_num;
	int big_cnt = max_num - num + 1;
	cout << small_cnt * big_cnt + (max_num - num);

	return 0;
}
