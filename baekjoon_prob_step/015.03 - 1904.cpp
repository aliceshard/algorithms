#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <vector>
#include <math.h>
#include <cstring>
using namespace std;

int memo[1000001];

int fibo(int x) {
	if (memo[x] != -1) {
		return memo[x];
	}

	if (x == 1) {
		return memo[1];
	}
	else if (x == 2) {
		return memo[2];
	}
	else {
		for (int i = 3; i <= x; i++) {
			memo[i] = (memo[i - 1] + memo[i - 2]) % 15746;
		}

		return memo[x];
	}
}

int main(void) {
	memset(memo, -1, sizeof(memo));
	memo[1] = 1;
	memo[2] = 2;
	int n;
	
	scanf("%d", &n);
	printf("%d", fibo(n));
	return 0;
}