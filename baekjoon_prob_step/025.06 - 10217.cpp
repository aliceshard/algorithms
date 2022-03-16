#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <utility>
#define INF 0xFFFFFF
using namespace std;

class compare {
public:
	bool operator()(const vector<int> e1, const vector<int> e2) {
		// compare d
		return e1[2] > e2[2];
	}
};

int n, m, k, T = 0;
int memo[101][10001];
vector<vector<vector<int>>> graph;
priority_queue<vector<int>, vector<vector<int>>, compare> pq;

void dijkstra(int start) {
	vector<int> tp_start = { 1, 0, 0 };
	pq.push(tp_start);

	while (pq.size() != 0) {
		vector<int> temp = pq.top();
		pq.pop();
		int now = temp[0];
		int fee = temp[1];
		int dist = temp[2];

		// prevent loop
		if (memo[now][fee] < dist)
			continue;

		for (int i = 0; i < graph[now].size(); i++) {
			vector<int> graph_ptr = graph[now][i];
			int dest = graph_ptr[0];
			int fee_next = graph_ptr[1];
			int adj_dist = graph_ptr[2];

			int total_dist = dist + adj_dist;
			int total_fee = fee + fee_next;
			
			if (total_fee > m)
				continue;
			if (memo[dest][total_fee] <= total_dist)
				continue;
			
			for (int j = total_fee; j <= m; j++) {
				if (memo[dest][j] > total_dist)
					memo[dest][j] = total_dist;
			}
			pq.push({ dest, total_fee, total_dist });
		}
	}
}

int main(void) {
	cin >> T;
	for (int i = 0; i < T; i++) {
		int ans = INF;
		cin >> n >> m >> k;

		// init. 
		graph.clear();
		for (int j = 0; j < n + 1; j++) {
			vector<vector<int>> tp1 = {};
			graph.push_back(tp1);
		}
		for (int j = 0; j < 101; j++) 
			for (int l = 0; l < 10001; l++) 
				memo[j][l] = INF;

		// store graph inputs
		for (int j = 0; j < k; j++) {
			int u, v, c, d = 0;
			cin >> u >> v >> c >> d;
			vector<int> tp = { v, c, d };
			graph[u].push_back(tp);
		}

		dijkstra(1);

		for (int j = 0; j <= m; j++) {
			ans = min(ans, memo[n][j]);
		}

		if (ans == INF) {
			printf("Poor KCM\n");
		}
		else {
			printf("%d\n", ans);
		}
	}

	return 0;
}