#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

int n;
int score_min = 101;
vector<int> team;
vector<vector<int>> game;

void print_team(vector<int> team1, vector<int> team2) {
	printf("team1: ");
	for (int i = 0; i < n / 2; i++) {
		printf("%d ", team1[i]);
	}
	printf("team2: ");
	for (int i = 0; i < n / 2; i++) {
		printf("%d ", team2[i]);
	}
	return;
}

void dfs(int idx, int depth) {
	if (depth == n / 2) {
		int team1_score = 0;
		int team2_score = 0;
		vector<int> team1;
		vector<int> team2;

		for (int i = 0; i < n; i++) {
			if (team[i] == 1)
				team1.push_back(i);
			else if (team[i] == 2)
				team2.push_back(i);
		}

		//print_team(team1, team2);

		for (int i = 0; i < n / 2; i++) {
			for (int j = i + 1; j < n / 2; j++) {
				team1_score += game[team1[i]][team1[j]] + game[team1[j]][team1[i]];
				team2_score += game[team2[i]][team2[j]] + game[team2[j]][team2[i]];
			}
		}
		if (abs(team1_score - team2_score) < score_min)
			score_min = abs(team1_score - team2_score);
		return;
	}

	for (int i = idx; i < n; i++) {
		team[i]++;
		dfs(i + 1, depth + 1);
		team[i]--;
	}
}

int main(void) {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		vector<int> a;
		game.push_back(a);
		for (int j = 0; j < n; j++) {
			int t;
			cin >> t;
			game[i].push_back(t);
		}
	}
	for (int i = 0; i < n; i++) {
		team.push_back(1);
	}
	dfs(0, 0);
	printf("%d\n", score_min);

	return 0;
}