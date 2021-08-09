#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <cstring>
using namespace std;

// 1-index로 접근/저장
vector<pair<int, int>> input;
int dp[101][100001];
int max_val;
int n, k;

bool compare(pair<int,int> a, pair<int,int> b) {
	return a.second > b.second ? true : false;
}

void print_input() {
	for (int i = 1; i < n + 1; i++) {
		printf("%d %d\n", input[i].first, input[i].second);
	}
}


int main(void) {
	memset(dp, 0, sizeof(dp));
	scanf("%d %d", &n, &k);
	input.push_back({ -1,-1 });
	for (int i = 1; i < n + 1; i++) {
		pair<int, int> a;
		scanf("%d %d", &a.first, &a.second);
		input.push_back(a);
	}
	//print_input();

	// init
	max_val = 0;
	for (int i = 1; i < k + 1; i++) {
		if (input[1].first <= i) {
			dp[1][i] = input[1].second;
		}
	}

	// dp는 value를 담는다.
	for (int i = 2; i < n + 1; i++) {
		int weight = input[i].first;
		int value = input[i].second;

		for (int j = 1; j < k + 1; j++) {
			if (j < input[i].first) {
				dp[i][j] = dp[i - 1][j];
			}
			else {
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value);
			}
		}
	}
	
	// dp process
	printf("%d\n", dp[n][k]);
}