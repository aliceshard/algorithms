#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <vector>
#include <math.h>
#include <cstring>
using namespace std;

int memo[21][21][21] = { 0, };
bool memo_ready[21][21][21] = { false, };

int w(int a, int b, int c) {
	if (a <= 0 || b <= 0 || c <= 0) {
		return 1;
	}
	if (a > 20 || b > 20 || c > 20) {
		return w(20, 20, 20);
	}
	if (memo_ready[a][b][c] == true) {
		return memo[a][b][c];
	}
	if (a < b && b < c) {
		int w1 = w(a, b, c - 1);
		int w2 = w(a, b - 1, c - 1);
		int w3 = w(a, b - 1, c);

		memo[a][b][c - 1] = w1;
		memo[a][b - 1][c - 1] = w2;
		memo[a][b - 1][c] = w3;
		memo_ready[a][b][c - 1] = true;
		memo_ready[a][b - 1][c - 1] = true;
		memo_ready[a][b - 1][c] = true;

		return w1 + w2 - w3;
	}

	int w1 = w(a - 1, b, c);
	int w2 = w(a - 1, b - 1, c);
	int w3 = w(a - 1, b, c - 1);
	int w4 = w(a - 1, b - 1, c - 1);

	memo[a - 1][b][c] = w1;
	memo[a - 1][b - 1][c] = w2;
	memo[a - 1][b][c - 1] = w3;
	memo[a - 1][b - 1][c - 1] = w4;
	memo_ready[a - 1][b][c] = true;
	memo_ready[a - 1][b - 1][c] = true;
	memo_ready[a - 1][b][c - 1] = true;
	memo_ready[a - 1][b - 1][c - 1] = true;

	return w1 + w2 + w3 - w4;
}

int main(void) {
	int a, b, c;
	while(true) {
		scanf("%d %d %d", &a, &b, &c);
		if (a == -1 && b == -1 && c == -1)
			break;
		printf("w(%d, %d, %d) = %d\n", a, b, c, w(a, b, c));
	}
}