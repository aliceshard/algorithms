#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <cstring>
#define MAX 10000001
using namespace std;

vector<int> memo;
int n;

int main(void) {
	scanf("%d", &n);

	for (int i = 0; i < 3*n + 3; i++) {
		memo.push_back(MAX);
	}
	memo[1] = 0;
	memo[2] = 1;
	memo[3] = 1;
	for (int i = 2; i < n + 1; i++) {
		memo[i * 3] = i*3 <= n ? min(memo[i * 3], memo[i] + 1):MAX;
		memo[i * 2] = i*2 <= n ? min(memo[i * 2], memo[i] + 1):MAX;
		memo[i + 1] = min(memo[i + 1], memo[i] + 1);
	}

	printf("%d\n", memo[n]);
}