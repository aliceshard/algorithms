#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#define INF 0xFFFFFF
int n, m = 0;
std::vector<std::vector<int>> memo;

void floyd_warshall() {
	for (int i = 1; i <= n; i++) {            
		for (int j = 1; j <= n; j++) {       
			for (int k = 1; k <= n; k++) {    
				if (memo[j][i] != INF && memo[i][k] != INF) {
					memo[j][k] = std::min(memo[j][k], memo[j][i] + memo[i][k]);
				}
			}
		}
	}
}

int main(void) {
	std::cin >> n;
	std::cin >> m;
	for (int i = 0; i < n + 1; i++) {
		std::vector<int> vec;
		for (int j = 0; j < n + 1; j++) {
			vec.push_back(INF);
		}
		memo.push_back(vec);
	}

	for (int i = 0; i < m; i++) {
		int a, b, c;
		std::cin >> a >> b >> c;
		if (memo[a][b] > c) {
			memo[a][b] = c;
		}
	}

	floyd_warshall();

	for (int i = 1; i < n + 1; i++) {
		for (int j = 1; j < n + 1; j++) {
			if (i == j || memo[i][j] == INF) {
				printf("0 ");
			}
			else {
				printf("%d ", memo[i][j]);
			}
		}
		printf("\n");
	}

	return 0;
}