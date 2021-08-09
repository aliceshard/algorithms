#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <cstring>
using namespace std;

// 0-index로 접근/저장
char input1[1001];
char input2[1001];
int memo[1002][1002];
int max_val;
int n;

int main(void) {
	memset(memo, 0, sizeof(memo));
	memset(input1, 0, sizeof(input1));
	memset(input2, 0, sizeof(input2));
	scanf("%s", input1);
	scanf("%s", input2);

	int size1 = strlen(input1);
	int size2 = strlen(input2);
	for (int i = 1; i < size2 + 1; i++) {
		for (int j = 1; j < size1 + 1; j++) {
			if (input1[j - 1] == input2[i - 1]) {
				memo[i][j] = memo[i - 1][j - 1] + 1;
				max_val = max(max_val, memo[i][j]);
			}
			else {
				memo[i][j] = memo[i - 1][j] > memo[i][j - 1] ? memo[i - 1][j] : memo[i][j - 1];
			}
		}
	}
	printf("%d\n", max_val);
}