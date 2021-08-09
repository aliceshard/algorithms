#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#include <math.h>
using namespace std;

int n;
int cnt = 0;
int queen_rows[16] = { 0, };

void print_game(int row) {
	printf("current row: %d\n", row);
	for (int i = 0; i < n + 1; i++) {
		for (int j = 0; j < n + 1; j++) {
			if (queen_rows[i] == 0) {
				printf("0 ");
			}
			else {
				if (j == queen_rows[i]) {
					printf("* ");
				}
				else {
					printf("0 ");
				}
			}
		}
		printf("\n");
	}
	printf("\n");
}

bool isPromising(int row, int col) {
	// 같은 row를 가질 경우
	if (queen_rows[row] != 0) {
		return false;
	}
	
	// 같은 col을 가질 경우
	for (int i = 1; i < n + 1; i++) {
		if (queen_rows[i] == col) {
			return false;
		}
	}

	for (int i = 1; i < n + 1; i++) {
		// 같은 대각선에 있을 경우
		if (queen_rows[i] != 0) {
			int stride = 1;
			int obj_row = i;
			int obj_col = queen_rows[i];

			if (abs(obj_row - row) == abs(obj_col - col)) {
				return false;
			}
		}
	}
	return true;
}

void dfs(int row) {
	if (row == n) {
		for (int i = 1; i < n + 1; i++) {
			if (isPromising(row, i)) {
				cnt++;
			}
		}
		return;
	}
	for (int i = 1; i < n + 1; i++) {
		//print_game(row);
		if (isPromising(row, i)) {
			queen_rows[row] = i;
			dfs(row + 1);
			queen_rows[row] = 0;
		}
	}
}

int main(void) {
	scanf("%d", &n);

	dfs(1);
	printf("%d\n", cnt);

	return 0;
}