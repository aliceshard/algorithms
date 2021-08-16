#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <string>
#include <cstring>
#include <stack>
using namespace std;

int r,c;
int mine[751][751];
int dp[751][751];
int max_size = 0;

int mine_checker(int size, int y_base, int x_base) {
	// 다이아몬드 /\ 확인
	for (int i = 1; i < size; i++) {
		int left_hand = x_base - i;
		int right_hand = x_base + i;

		// 제한크기 넘어가면 성립 불가능
		if (left_hand < 1 || right_hand > c) {
			return 0;
		}

		// 하나라도 0이라면 성립 불가능
		if (!(mine[y_base + i][x_base + i] == 1 && 
			mine[y_base + i][x_base - i] == 1)) {
			return 0;
		}
	}
	int y_mid = size;

	// 다이아몬드 \/ 확인
	int j = 1;
	for (int i = size - 2; i > 0; i--) {
		int left_hand = x_base - i;
		int right_hand = x_base + i;

		// 제한크기 넘어가면 성립 불가능
		if (left_hand < 1 || right_hand > c) {
			return 0;
		}

		// 하나라도 0이라면 성립 불가능
		if (!(mine[y_mid + j][x_base + i] == 1 &&
			mine[y_mid + j][x_base - i == 1])) {
			return 0;
		}
		j++;
	}

	// 다이아몬드 꼬다리 체크
	if (!(mine[y_base + (size * 2) - 2][x_base] == 1))
		return 0;

	return size;
}

int main(void) {
	memset(mine, -1, sizeof(mine));
	memset(dp, -1, sizeof(dp));
	scanf("%d %d", &r, &c);
	char buf[760];

	for (int i = 1; i < r + 1; i++) {
		scanf("%s", buf);
		for (int j = 0; j < c; j++) {
			mine[i][j + 1] = buf[j] - '0';
			dp[i][j + 1] = mine[i][j + 1] == 1 ? 1 : 0;
			max_size = max(max_size,mine[i][j + 1] == 1 ? 1 : 0);
		}
	}
	
	for (int size = 2; 2 * size - 1 <= r; size++) {
		for (int y = 1; y <= r - (2 * size - 2); y++) {
			for (int x = size; x <= c - (size - 1); x++) {
				if (dp[y][x] != 0) {
					dp[y][x] = max(mine_checker(size, y, x), dp[y][x]);
					max_size = max(dp[y][x], max_size);
				}
			}
		}
	}
	
	printf("%d\n",max_size);
	return 0;
}