#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#include <math.h>
#define ADD 0
#define SUB 1
#define MUL 2
#define DIV 3
using namespace std;

int n;
int result_min = 1000000001; 
int result_max = -1000000001;
vector<int> numbers;
vector<int> ops;
vector<int> seq;
int ops_var = 0;

int poly_solver() {
	int result = 0;
	vector<int> backup = numbers;

	for (int i = 0; i < seq.size(); i++) {
		switch (seq[i]) {
		case ADD:
			numbers[i + 1] = numbers[i] + numbers[i + 1];
			break;
		case SUB:
			numbers[i + 1] = numbers[i] - numbers[i + 1];
			break;
		case MUL:
			numbers[i + 1] = numbers[i] * numbers[i + 1];
			break;
		case DIV:
			numbers[i + 1] = numbers[i] / numbers[i + 1];
			break;
		}
		result = numbers[i + 1];
	}
	numbers = backup;
	return result;
}

void dfs(int depth) {
	if (depth == ops_var) {
		int result = poly_solver();
		if (result < result_min) result_min = result;
		if (result > result_max) result_max = result;
		return;
	}

	for (int i = 0; i < 4; i++) {
		if (ops[i] == 0)
			continue;
		ops[i]--;
		seq.push_back(i);
		dfs(depth + 1);
		seq.pop_back();
		ops[i]++;
	}
}

int main(void) {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int t;
		scanf("%d", &t);
		numbers.push_back(t);
	}
	for (int i = 0; i < 4; i++) {
		int t;
		scanf("%d", &t);
		ops.push_back(t);
		ops_var += t;
	}

	dfs(0);
	printf("%d\n%d", result_max, result_min);

	return 0;
}