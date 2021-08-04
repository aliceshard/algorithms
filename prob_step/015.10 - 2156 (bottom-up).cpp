#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <cstring>
using namespace std;

// 1-index로 접근/저장
int input[10001];
int memo[10001];
int n;

int main(void) {
	scanf("%d", &n);
	memset(input, 0, sizeof(input));
	memset(memo, 0, sizeof(memo));
	for (int i = 1; i < n + 1; i++) {
		scanf("%d", &input[i]);
	}
	
	memo[1] = input[1];
	memo[2] = memo[1] + input[2];
	
	for (int i = 3; i < n + 1; i++) {
		memo[i] = max(memo[i - 2], memo[i - 3] + input[i - 1]) + input[i];
		memo[i] = max(memo[i], memo[i - 1]);
	}
	printf("%d\n", memo[n]);
}