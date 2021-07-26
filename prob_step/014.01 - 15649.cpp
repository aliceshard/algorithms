#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <vector>
#include <stack>

int n, m;
std::vector<int> nums;
std::vector<bool> visited;
std::vector<int> print_buffer;

void dfs(int depth) {
	if (depth == m) {
		for (int i = 0; i < m; i++) {
			printf("%d ", print_buffer[i]);
		}
		printf("\n");

		return;
	}

	for (int j = 1; j < n + 1; j++) {
		if (visited[j] == true)
			continue;
		visited[j] = true;
		print_buffer.push_back(j);
		dfs(depth + 1);
		visited[j] = false;
		print_buffer.pop_back();
	}
}

int main(void) {
	std::ios::sync_with_stdio(false);
	std::cin.tie(NULL);
	std::cout.tie(NULL);
	
	int depth = 0;
	
	scanf("%d %d", &n, &m);

	// dummy initializtion
	nums.push_back(0);
	visited.push_back(false);
	for (int i = 1; i < n+1; i++) {
		nums.push_back(i);
		visited.push_back(false);
	}

	dfs(0);

	return 0;
}