#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <cstring>
#define MAX 10000001
#define DIV 1000000000
using namespace std;

int table[10][2] = { {-1,1}, {0,2}, {1,3}, {2,4}, {3,5},
					{4,6}, {5,7}, {6,8}, {7,9}, {8,-1} };
int table_num[10] = { 1,2,2,2,2,2,2,2,2,1 };

// 메모이제이션은 1-index
int memo[101][10];
int n;

void dfs(int depth, int node) {
	if (depth == n) {
		memo[depth][node] = 1;
		return;
	}
	if (memo[depth][node] != 0) {
		return;
	}

	// 끄트머리 경우 제외시키기
	if (table[node][0] != -1)
		dfs(depth + 1, table[node][0]);
	if(table[node][1] != -1)
		dfs(depth + 1, table[node][1]);

	// 하위 노드에서 얻어온 정보로 초기화
	int res1 = table[node][0] != -1 ? memo[depth + 1][table[node][0]] + memo[depth][node] : 0;
	int res2 = table[node][1] != -1 ? memo[depth + 1][table[node][1]] + memo[depth][node] : 0;
	memo[depth][node] = (res1 + res2) % DIV;
}

int main(void) {
	scanf("%d", &n);
	memset(memo, 0, sizeof(memo));
	int sum = 0;

	for (int i = 1; i < 10; i++) {
		dfs(1, i);
		sum = (sum + memo[1][i]) % DIV;
	}

	printf("%d\n", sum);
}