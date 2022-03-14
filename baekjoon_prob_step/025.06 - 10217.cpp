#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#define INF 0xFFFFFF
using namespace std;

int n, m, k, T = 0;
vector<int> memo;
vector<vector<vector<int>>> graph;
priority_queue<vector<int>, vector<vector<int>>, less<vector<int>>> pq;


bool operator<(vector<int> e1, vector<int> e2) {
	// compare d
	return e1[2] < e2[2];
}

void dijkstra(int start) {
	// memo init
	for (int i = 0; i < n + 1; i++)
		memo.push_back(INF);

	vector<int> tp_start = { 1, 0, 0 };
	pq.push(tp_start);
	memo[start] = 0;
	while (pq.size() != 0) {
		vector<int> temp = pq.top();
		pq.pop();
		int now = temp[0];
		int cost = temp[1];
		int dist = temp[2];

		if (memo[now] < dist)
			continue;

		for (int i = 0; i < graph[now].size(); i++) {
			vector<int> graph_ptr = graph[now][i];
			int dest = graph_ptr[0];
			int adj_dist = graph_ptr[2];

			int cost = dist + adj_dist;
			if (cost < memo[dest]) {
				memo[dest] = cost;
				vector<int> tp = { dest, 0, cost };
				pq.push(tp);
			}
		}
	}
}

int main(void) {
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> n >> m >> k;

		// init. graph vector
		for (int j = 0; j < n + 1; j++) {
			vector<vector<int>> tp1 = {};
			graph.push_back(tp1);
		}

		// store graph inputs
		for (int j = 0; j < k; j++) {
			int u, v, c, d = 0;
			cin >> u >> v >> c >> d;
			vector<int> tp = { v, c, d };
			graph[u].push_back(tp);
		}

		dijkstra(1);
		printf("%d\n", memo[n]);
	}

	return 0;
}