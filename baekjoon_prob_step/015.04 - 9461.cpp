#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <vector>
#include <math.h>
#include <cstring>
using namespace std;

int memo[13];

int main(void) {
	memset(memo, -1, sizeof(memo));
	memo[1] = 1;
	memo[2] = 1;
	memo[3] = 1;
	memo[4] = 2;
	memo[5] = 2;
	memo[6] = 3;
	memo[7] = 4;
	memo[8] = 5;
	int n, m;
	
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &m);
		if (m <= 8) {
			printf("%d\n", memo[m]);
			continue;
		}
		for (int i = 9; i <= m; i++) {
			memo[9] = memo[4] + memo[8];
			memo[4] = memo[5];
			memo[5] = memo[6];
			memo[6] = memo[7];
			memo[7] = memo[8];
			memo[8] = memo[9];
		}
		printf("%d\n", memo[9]);
		memo[4] = 2;
		memo[5] = 2;
		memo[6] = 3;
		memo[7] = 4;
		memo[8] = 5;
	}
}