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

int main(void) {
	char str[110];
	memset(str, 0, sizeof(str));

	while (true) {
		stack<int> st1;
		bool flag = false;
		memset(str, 0, sizeof(str));

		fgets(str, sizeof(str), stdin);
		for (int j = 0; j < sizeof(str); j++) {
			if (str[j] == '(') {
				st1.push(1);
			}
			else if (str[j] == ')') {
				if (st1.size() == 0 || st1.top() != 1) {
					flag = true;
					break;
				}
				st1.pop();
			}
			else if (str[j] == '[') {
				st1.push(2);
			}
			else if (str[j] == ']') {
				if (st1.size() == 0 || st1.top() != 2) {
					flag = true;
					break;
				}
				st1.pop();
			}
		}

		if(!strcmp(".\n", str))
			break;
		else if (flag == true || st1.size() != 0) {
			printf("no\n");
		}
		else if (st1.size() == 0) {
			printf("yes\n");
		}
	}
}