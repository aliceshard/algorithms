#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <cstring>
using namespace std;

// 1-index로 접근/저장
int input[101];
int dp[10001];
int n, k;
int count = 0;

int main(void) {
	memset(input, -1, sizeof(input));
	memset(dp, 0, sizeof(dp));
	scanf("%d %d", &n, &k);
	for (int i = 1; i < n + 1; i++) {
		scanf("%d", &input[i]);
	}

	// init dp
	dp[0] = 1;
	for (int i = 1; i < k + 1; i++) {
		if (i % input[1] == 0)
			dp[i]++;
	}

	// dp progress
	for (int i = 2; i < n + 1; i++) {
		for (int j = 1; j < k + 1; j++) {
			if (j - input[i] >= 0) {
				dp[j] = dp[j] + dp[j - input[i]];
			}
		}
	}

	printf("%d\n", dp[k]);
}