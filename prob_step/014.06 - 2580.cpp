#pragma warning(disable: 4996)

#include <stdio.h>
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#include <math.h>
using namespace std;

vector<vector<int>> game;
int area_sheet[10][10] = {
	{ 0,0,0,0,0,0,0,0,0,0 },
	{ 0,1,1,1,2,2,2,3,3,3 },
	{ 0,1,1,1,2,2,2,3,3,3 },
	{ 0,1,1,1,2,2,2,3,3,3 },
	{ 0,4,4,4,5,5,5,6,6,6 },
	{ 0,4,4,4,5,5,5,6,6,6 },
	{ 0,4,4,4,5,5,5,6,6,6 },
	{ 0,7,7,7,8,8,8,9,9,9 },
	{ 0,7,7,7,8,8,8,9,9,9 },
	{ 0,7,7,7,8,8,8,9,9,9 }
};
vector<pair<int, int>> area_to_coord = { {0,0}, {1,1},{1,4},{1,7},{4,1},{4,4},{4,7},{7,1},{7,4},{7,7} };
vector<pair<int, int>> unknown_panels;
bool escape = false;

void print_game(vector<vector<int>> game) {
	for (int i = 1; i < 10; i++) {
		for (int j = 1; j < 10; j++) {
			printf("%d ", game[i][j]);
		}
		printf("\n");
	}
}

void solve_sudoku(int unknown_idx) {
	if (unknown_idx == unknown_panels.size()) {
		print_game(game);
		escape = true;
		return;
	}

	int row = unknown_panels[unknown_idx].first;
	int col = unknown_panels[unknown_idx].second;
	int area = area_sheet[row][col];
	// 0 index true -> it has unknown panel
	bool row_parse[10] = { false, };
	bool col_parse[10] = { false, };
	// 0123 / 456 / 789
	bool area_parse[10] = { false, };
	bool cand[10] = { false };
	vector<int> promising;

	// parse row and col
	for (int i = 1; i < 10; i++) {
		row_parse[game[row][i]] = true;
		col_parse[game[i][col]] = true;
	}
	// parse area
	int y = area_to_coord[area].first;
	int x = area_to_coord[area].second;
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			area_parse[game[(long long)y + i][(long long)x + j]] = true;
		}
	}

	// check candidates
	for (int i = 1; i < 9 + 1; i++) {
		// 'true' means 'not possible'
		if (col_parse[i] == true) cand[i] = true;
		if (row_parse[i] == true) cand[i] = true;
		if (area_parse[i] == true) cand[i] = true;
	}
	for (int i = 1; i < 9 + 1; i++) {
		if (cand[i] == false) promising.push_back(i);
	}

	if (promising.empty() == true)
		return;

	/*
	// print promisings
	for_each(promising.begin(), promising.end(), [](int i) {printf("%d ", i); });
	printf("(%d, %d)", row, col);
	printf("\n");
	*/

	for (int i = 0; i < promising.size(); i++) {
		game[row][col] = promising[i];
		solve_sudoku(unknown_idx + 1);
		if (escape == true) return;
		game[row][col] = 0;
	}
}

int main(void) {
	for (int i = 0; i < 10; i++) {
		vector<int> a;
		game.push_back(a);
		for (int j = 0; j < 10; j++) {
			game[i].push_back(-1);
		}
	}

	for (int i = 1; i < 10; i++) {
		for (int j = 1; j < 10; j++) {
			cin >> game[i][j];
			if (game[i][j] == 0) {
				unknown_panels.push_back({ i,j });
			}
		}
	}

	solve_sudoku(0);

	return 0;
}