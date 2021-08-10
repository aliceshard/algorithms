#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <cstring>
using namespace std;

// 1-index로 접근/저장
int input[11];
int dp[100000001];
int n, k;
int count = 0;

int main(void) {
	memset(input, -1, sizeof(input));
	for (int i = 0; i < 100000001; i++) {
		dp[i] = 0x8FFFFF;
	}
	scanf("%d %d", &n, &k);
	for (int i = 1; i < n + 1; i++) {
		scanf("%d", &input[i]);
	}

	// init dp
	dp[0] = 0;
	for (int i = 1; i < k + 1; i++) {
		if (i % input[1] == 0)
			dp[i] = i / input[1];
	}

	// dp progress
	for (int i = 2; i < n + 1; i++) {
		for (int j = input[i]; j < k + 1; j++) {
			if (j - input[i] >= 0) {
				dp[j] = min(dp[j - input[i]] + 1, dp[j]);
			}
		}
	}

	printf("%d\n", dp[k] == 0x9FFFFF ? -1 : dp[k]);
}