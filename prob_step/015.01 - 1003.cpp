#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <cstring>
using namespace std;

// fibonacci(n)�� ȣ��� ���, ����� 0, 1�� �Ҹ����� fibo_call[n]�� ����.
int fibo_call0[41] = { 0, };
int fibo_call1[41] = { 0, };
// �� fibonacci(n) ������ '���� ���α׷����� ���� ���� �� �ֵ��� ����� �Ϸ�� �����ΰ�?' �� ����.
bool fibo_call0_valid[41] = { false, };
bool fibo_call1_valid[41] = { false, };
int n;

void fibonacci(int x, int orig) {
	if (fibo_call0_valid[x] == true && fibo_call1_valid[x] == true) {
		fibo_call0[orig] += fibo_call0[x];
		fibo_call1[orig] += fibo_call1[x];
		return;
	}

	if (x == 0) {
		fibo_call0[orig]++;
	}
	else if (x == 1) {
		fibo_call1[orig]++;
	}
	else {
		fibonacci(x - 1, x);
		fibonacci(x - 2, x);
		fibo_call0_valid[x] = true;
		fibo_call1_valid[x] = true;

		if (x != orig) {
			fibo_call0[orig] += fibo_call0[x];
			fibo_call1[orig] += fibo_call1[x];
		}
		
		return;
	}
}

int main(void) {
	int it;
	scanf("%d", &it);

	for (int i = 0; i < it; i++) {
		scanf("%d", &n);
		fibonacci(n, n);
		fibo_call0[0] = 1;
		fibo_call1[1] = 1;
		printf("%d %d\n", fibo_call0[n], fibo_call1[n]);

		memset(fibo_call0, 0, sizeof(fibo_call0));
		memset(fibo_call1, 0, sizeof(fibo_call1));
		memset(fibo_call0_valid, false, sizeof(fibo_call0_valid));
		memset(fibo_call1_valid, false, sizeof(fibo_call1_valid));
	}
	return 0;
}