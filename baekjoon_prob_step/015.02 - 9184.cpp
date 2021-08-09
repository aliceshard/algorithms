#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <vector>
#include <math.h>
#include <cstring>
using namespace std;

int memo[21][21][21];

int w(int a, int b, int c) {
	if (a <= 0 || b <= 0 || c <= 0) {
		return 1;
	}
	if (a > 20 || b > 20 || c > 20) {
		return w(20, 20, 20);
	}
	if (memo[a][b][c] != -1) {
		return memo[a][b][c];
	}
	if (a < b && b < c) {
		int w1 = w(a, b, c - 1);
		int w2 = w(a, b - 1, c - 1);
		int w3 = w(a, b - 1, c);

		return memo[a][b][c] = w1 + w2 - w3;
	}

	int w1 = w(a - 1, b, c);
	int w2 = w(a - 1, b - 1, c);
	int w3 = w(a - 1, b, c - 1);
	int w4 = w(a - 1, b - 1, c - 1);

	return memo[a][b][c] = w1 + w2 + w3 - w4;
}

int main(void) {
	int a, b, c;
	memset(memo, -1, sizeof(memo));

	scanf("%d %d %d", &a, &b, &c);
	while(!(a == -1 && b == -1 && c == -1)) {
		printf("w(%d, %d, %d) = %d\n", a, b, c, w(a, b, c));
		scanf("%d %d %d", &a, &b, &c);
	}
}