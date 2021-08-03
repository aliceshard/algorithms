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
int n;
int glob_min = MAX;

int opt(int idx, int depth) {
	int cursor = memo[depth][idx];
	// 만약 이미 저장된 값이 존재한다면
	if (cursor != MAX)
		return cursor;
	// 만약 최종 지점에 도달했다면
	if (depth == n)
		return 0;

	for (int i = 0; i < 3; i++) {
		if (idx != i) {
			int opt_result = opt(i, depth + 1);
			memo[depth][idx] = min(memo[depth][idx], opt_result + input[depth][i]);
		}
	}
	return memo[depth][idx];
}

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

	for (int i = 0; i < 3; i++) {
		int t = opt(i, 0);
		if (glob_min > t)
			glob_min = t;
	}

	printf("%d\n", glob_min);
}