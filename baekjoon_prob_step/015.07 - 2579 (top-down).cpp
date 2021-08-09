#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <math.h>
#include <vector>
#include <cstring>
using namespace std;

// 1-index로 저장/접근
int stairs[302];
int memo[302];
int n;

void debug(int pos, int sum, int prev) {
	printf("current pos: %d, current sum: %d(+%d), prev: %d\n", pos, sum, stairs[pos], prev);
}

int dfs(int pos) {
	if (pos < 1) {
		return 0;
	}

	if(memo[pos] == -1)
		memo[pos] = max(dfs(pos - 2), dfs(pos - 3) + stairs[pos - 1]) + stairs[pos];
	return memo[pos];
}

int main(void) {
	memset(memo, -1, sizeof(memo));
	scanf("%d", &n);
	for (int i = 1; i < n+1; i++) {
		scanf("%d", &stairs[i]);
	}
	
	int max1 = dfs(n);
	printf("%d\n", max1);
	scanf("%d", &n);
	return 0;
}