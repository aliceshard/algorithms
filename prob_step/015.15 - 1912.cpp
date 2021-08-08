#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <cstring>
using namespace std;

// 1-index로 접근/저장
int input[100001];
int dp[100001];
int max_val;
int sum;
int n;

int main(void) {
	memset(dp, -1, sizeof(dp));
	scanf("%d", &n);
	for (int i = 1; i < n + 1; i++) {
		scanf("%d", &input[i]);
	}
	
	// init dp
	dp[1] = input[1];
	max_val = dp[1];
	for (int i = 2; i < n + 1; i++) {
		dp[i] = max(dp[i - 1] + input[i], input[i]);
		max_val = max(dp[i], max_val);
	}

	// debug section
	/*
	printf("dp: ");
	for (int i = 1; i < n + 1; i++) {
		printf("%d ", dp[i]);
	}
	printf("\n");
	*/

	printf("%d", max_val);
}