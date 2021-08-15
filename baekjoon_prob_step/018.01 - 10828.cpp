#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <string>
#include <cstring>
#include <stack>
using namespace std;

int n;
int st[10001];
int cursor = 0;

int main(void) {
	memset(st, 0, sizeof(st));
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		char command[10];
		int num = 0;
	
		scanf("%s", command);
		if (!strcmp("push", command)) {
			scanf("%d", &num);
			st[cursor] = num;
			cursor++;
		}
		else if (!strcmp("pop", command)) {
			int popNum = cursor == 0 ? -1 : st[cursor-1];
			printf("%d\n", popNum);
			if(popNum != -1)
				cursor--;
		}
		else if (!strcmp("size", command)) {
			printf("%d\n", cursor);
		}
		else if (!strcmp("empty", command)) {
			int isEmpty = cursor == 0 ? 1 : 0;
			printf("%d\n", isEmpty);
		}
		else if (!strcmp("top", command)) {
			int top = cursor == 0 ? -1 : st[cursor-1];
			printf("%d\n", top);
		}
	}
}