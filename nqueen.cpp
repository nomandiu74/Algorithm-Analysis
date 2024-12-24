#include <bits/stdc++.h>
using namespace std;

bool isSafe(int** arr, int x, int y, int n) {
    // Check the column
    for (int row = 0; row < x; row++) {
        if (arr[row][y] == 1) {
            return false;
        }
    }

    // Check the upper left diagonal
    int row = x, col = y;
    while (row >= 0 && col >= 0) {
        if (arr[row][col] == 1) {
            return false;
        }
        row--;
        col--;
    }

    // Check the upper right diagonal
    row = x, col = y;
    while (row >= 0 && col < n) {
        if (arr[row][col] == 1) {
            return false;
        }
        row--;
        col++;
    }

    return true;
}

bool solvequeen(int** arr, int x, int n) {
    if (x >= n) {
        return true;  // All queens are placed
    }

    for (int col = 0; col < n; col++) {
        if (isSafe(arr, x, col, n)) {
            arr[x][col] = 1;  // Place queen

            if (solvequeen(arr, x + 1, n)) {
                return true;
            }

            arr[x][col] = 0;  // Backtrack
        }
    }
    return false;
}

void print(int** arr, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << (arr[i][j] == 1 ? "Q" : ".") << " ";
        }
        cout << endl;
    }
}

int main() {
    int n;
    cout << "Enter number of n: ";
    cin >> n;

    int** arr = new int*[n];
    for (int i = 0; i < n; i++) {
        arr[i] = new int[n]();
    }

    if (solvequeen(arr, 0, n)) {
        print(arr, n);
    } else {
        cout << "Solution does not exist" << endl;
    }

    // Clean up memory
    for (int i = 0; i < n; i++) {
        delete[] arr[i];
    }
    delete[] arr;

    return 0;
}
