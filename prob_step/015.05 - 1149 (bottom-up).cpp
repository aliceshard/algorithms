#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <cstring>
#define MAX 10000001
using namespace std;

vector<vector<int>> input;
int memo[1001][3];
int glob_min = MAX;
int n;

int main(void) {
	for (int i = 0; i < 1001; i++) {
		for (int j = 0; j < 3; j++) {
			memo[i][j] = MAX;
		}
	}

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		vector<int> t;
		int a, b, c;
		scanf("%d %d %d", &a, &b, &c);
		t.push_back(a);
		t.push_back(b);
		t.push_back(c);
		input.push_back(t);
	}

	memo[0][0] = input[0][0];
	memo[0][1] = input[0][1];
	memo[0][2] = input[0][2];
	for (int i = 1; i < n; i++) {
		memo[i][0] = min(memo[i - 1][1], memo[i - 1][2]) + input[i][0];
		memo[i][1] = min(memo[i - 1][0], memo[i - 1][2]) + input[i][1];
		memo[i][2] = min(memo[i - 1][0], memo[i - 1][1]) + input[i][2];
	}
	for (int i = 0; i < 3; i++) {
		if (memo[n - 1][i] < glob_min)
			glob_min = memo[n - 1][i];
	}

	printf("%d\n", glob_min);
}