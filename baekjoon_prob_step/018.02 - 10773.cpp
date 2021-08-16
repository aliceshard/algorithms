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
stack<int> st;

int main(void) {
	int t, sum=0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &t);
		if (t == 0) {
			st.pop();
		}
		else {
			st.push(t);
		}
	}
	
	while (!st.empty()) {
		sum += st.top();
		st.pop();
	}
	printf("%d\n",sum);
}