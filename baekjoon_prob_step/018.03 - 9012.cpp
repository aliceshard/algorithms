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
	char c;
	bool flag = false;
	char str[100];
	scanf("%d", &n);
	
	for (int i = 0; i < n; i++) {
		memset(str, 0, sizeof(str));
		stack<int> st;
		flag = false;

		scanf("%s", str);
		for (int j = 0; j < strlen(str); j++) {
			char c = str[j];
			if (c == '(') {
				st.push(1);
			}
			else if (c == ')') {
				if (st.size() == 0) {
					flag = true;
					break;
				}
				st.pop();
			}
		}

		if (flag == true || st.size() != 0) {
			printf("NO\n");
		}
		else if (st.size() == 0) {
			printf("YES\n");
		}
	}

	
}