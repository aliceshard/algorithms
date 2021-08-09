#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <cstring>
using namespace std;

// 0-index로 접근/저장
vector<pair<int, int>> input;
int memo[101];
int n;
int max_val, min_val;

int main(void) {
	memset(memo, 0, sizeof(memo));
	scanf("%d", &n);

	for (int i = 1; i < n + 1; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		input.push_back({ a,b });
	}
	sort(input.begin(), input.end());

	for (int i = 0; i < n; i++) {
		int temp = 0;
		for (int j = 0; j < i + 1; j++) {
			if (input[j].second < input[i].second) {
				temp = max(temp, memo[j]);
			}
		}
		memo[i] = temp + 1;
		max_val = max(max_val, memo[i]);
	}
	printf("%d\n", n - max_val);
}