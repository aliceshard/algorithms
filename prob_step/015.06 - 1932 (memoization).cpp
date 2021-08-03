#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <cstring>
#define MIN -10000001
using namespace std;

int input[501][501];
int memo[501][501];
int n;

int tree(int depth, int idx) {
	//printf("depth: %d, idx: %d\n", depth, idx);
	if (depth == n)
		return 0;
	if (memo[depth][idx] != MIN)
		return memo[depth][idx];

	int tree_result1 = memo[depth + 1][idx] = tree(depth + 1, idx);
	int tree_result2 = memo[depth + 1][idx + 1] = tree(depth + 1, idx + 1);
	
	memo[depth][idx] = max(tree_result1, tree_result2) + input[depth][idx];
	
	return memo[depth][idx];
}

int main(void) {
	scanf("%d", &n);
	for (int i = 0; i < n+2; i++) {
		for (int j = 0; j < i+2; j++) {
			memo[i][j] = MIN;
			input[i][j] = MIN;
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i + 1; j++) {
			scanf("%d", &input[i][j]);
		}
	}

	printf("%d\n",tree(0, 0));
}