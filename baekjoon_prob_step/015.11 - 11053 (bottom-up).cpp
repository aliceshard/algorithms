#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <cstring>
using namespace std;

// 1-index로 접근/저장
int input[1001];
int memo[1001];
int n;
int max_val;

int main(void) {
	memset(input, -1, sizeof(input));
	memset(memo, 0, sizeof(memo));
	scanf("%d", &n);

	for (int i = 1; i < n + 1; i++) {
		scanf("%d", &input[i]);
	}
	
	for (int i = 1; i < n + 1; i++) {
		int max_memo = 0;
		for (int j = 1; j < i + 1; j++) {
			if (input[j] < input[i]) {
				max_memo = max(max_memo, memo[j]);
			}
		}
		memo[i] = max_memo + 1;
		max_val = max(max_val, memo[i]);
	}
	printf("%d\n", max_val);
}