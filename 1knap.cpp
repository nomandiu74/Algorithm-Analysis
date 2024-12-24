#include<bits/stdc++.h>
using namespace std;

int main() {
    int n, m;  // 'n' is the number of items, 'm' is the capacity of the knapsack
    
    // Take input for the number of items and knapsack capacity
    cout << "Enter the number of items: ";
    cin
    
    cout << "Enter the capacity of the knapsack: ";
    cin >> m;

    int profit[n+1], weight[n+1];

    // Input profit and weight for each item
    cout << "Enter the profit and weight of each item:\n";
    for (int i = 1; i <= n; i++) {
        cout << "Item " << i << ": ";
        cin >> profit[i] >> weight[i];
    }

    int k[n+1][m+1];

    // Build the table for the 0/1 Knapsack problem
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= m; w++) {
            if (i == 0 || w == 0) {
                k[i][w] = 0;
            } 
            else if (weight[i] <= w) {
                k[i][w] = max(profit[i] + k[i-1][w - weight[i]], k[i-1][w]);
            } 
            else {
                k[i][w] = k[i-1][w];
            }
        }
    }

    // Print the maximum profit
    cout << "Maximum profit is: " << k[n][m] << endl;

    return 0;
}
