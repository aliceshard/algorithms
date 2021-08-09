#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <cstring>
#define MIN -10000001
using namespace std;

int memo[501][501];
int n;

int main(void) {
	scanf("%d", &n);
	for (int i = 0; i < n+2; i++) {
		for (int j = 0; j < i+2; j++) {
			memo[i][j] = 0;
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i + 1; j++) {
			scanf("%d", &memo[i][j]);
		}
	}
	for (int i = 1; i < n; i++) {
		for (int j = 0; j < i + 1; j++) {
			if (j == 0) {
				memo[i][j] += memo[i - 1][j];
			}
			else if (j == i) {
				memo[i][j] += memo[i - 1][j - 1];
			}
			else {
				memo[i][j] += max(memo[i - 1][j], memo[i - 1][j - 1]);
			}
		}
	}

	int max_val = MIN;
	for (int i = 0; i < n; i++) {
		if (max_val < memo[n - 1][i])
			max_val = memo[n - 1][i];
	}

	printf("%d\n", max_val);
}