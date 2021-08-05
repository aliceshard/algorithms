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
int memo_ascend[1001];
int memo_descend[1001];
int n;
int max_val, min_val;

int main(void) {
	memset(input, -1, sizeof(input));
	memset(memo_ascend, 0, sizeof(memo_ascend));
	memset(memo_descend, 0, sizeof(memo_descend));
	scanf("%d", &n);

	for (int i = 1; i < n + 1; i++) {
		scanf("%d", &input[i]);
	}
	
	// ascending DP from [1]
	for (int i = 1; i < n + 1; i++) {
		int temp = 0;
		for (int j = 1; j < i + 1; j++) {
			if (input[j] < input[i])
				temp = max(temp, memo_ascend[j]);
		}
		memo_ascend[i] = temp + 1;
		max_val = max(max_val, memo_ascend[i]);
	}

	// descending DP from [n]
	for (int i = n; i > 0; i--) {
		int temp = 0;
		for (int j = n; j > i - 1; j--) {
			if (input[j] < input[i])
				temp = max(temp, memo_descend[j]);
		}
		memo_descend[i] = temp + 1;
		min_val = max(min_val, memo_descend[i]);
	}

	int memo_combined[1001];
	int long_bi = -1;
	for (int i = 0; i < n + 1; i++) {
		memo_combined[i] = memo_ascend[i] + memo_descend[i] - 1;
		long_bi = max(long_bi, memo_combined[i]);
	}
	printf("%d\n", long_bi);
}