// 6593 - 상범 빌딩

#include <bits/stdc++.h>
#define rep(i, a, n) for(auto i = a; i < n; i++)
#define REP(i, a, n) for(auto i = a; i <= n; i++)
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(NULL), cout.tie(NULL)

using namespace std;

int L, R, C;
int dx[6] = { 1, 0, -1, 0, 0, 0};
int dy[6] = { 0, 1, 0, -1, 0, 0 };
int dz[6] = { 0, 0, 0, 0, 1, -1 };
char board[32][32][32];
int dist[32][32][32];
int end_x, end_y, end_z;

int main() {
	FAST_IO;
	
	while (true) {
		cin >> L >> R >> C;
		if (L == 0 and R == 0 and C == 0) break;
		queue<tuple<int, int, int>> Q;
		fill(&dist[0][0][0], &dist[31][31][32], -1);
		rep(i, 0, L) {
			rep(j, 0, R) {
				string str;
				cin >> str;
				rep(k, 0, str.size()) {
					board[j][k][i] = str[k]; // 행, 열, 층 순서
					if (str[k] == 'S') {
						dist[j][k][i] = 0;
						Q.push({ j, k, i });
					}

					if (str[k] == 'E') { // 탈출구 정보 저장
						end_x = j;
						end_y = k;
						end_z = i;
					}
				}
			}
		}

		while (!Q.empty()) {
			auto cur = Q.front(); Q.pop();
			int curX, curY, curZ;
			tie(curX, curY, curZ) = cur;

			for (int dir = 0; dir < 6; dir++) {
				int nx = curX + dx[dir]; // 행
				int ny = curY + dy[dir]; // 열
				int nz = curZ + dz[dir]; // 층 으로 생각

				if (nx < 0 || nx >= R || ny < 0 || ny >= C || nz < 0 || nz >= L) continue;
				if (board[nx][ny][nz] == '#') continue;
				if (dist[nx][ny][nz] != -1) continue;

				Q.push({ nx, ny, nz });
				dist[nx][ny][nz] = dist[curX][curY][curZ] + 1;
			}

			if (board[curX][curY][curZ] == 'E') {
				cout << "Escaped in " << dist[curX][curY][curZ] << " minute(s)." << '\n';
				break;
			}
		}

		if (dist[end_x][end_y][end_z] == -1) {
			cout << "Trapped!" << '\n';
		}
		
	}
}	