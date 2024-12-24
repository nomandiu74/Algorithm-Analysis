#include<bits/stdc++.h>
using namespace std;

// Structure to represent an item with profit and weight
struct Item {
    int profit, weight;
};

// Function to compare two items based on their profit-to-weight ratio
bool compare(Item a, Item b) {
    double r1 = (double)a.profit / a.weight;
    double r2 = (double)b.profit / b.weight;
    return r1 > r2; // Sort in descending order
}

// Function to calculate the maximum profit for the fractional knapsack
double fractionalKnapsack(int n, int capacity, Item items[]) {
    // Sort items based on profit-to-weight ratio
    sort(items, items + n, compare);

    double totalProfit = 0.0;
    
    // Loop through each item
    for (int i = 0; i < n; i++) {
        // If the item can be fully taken, take it
        if (items[i].weight <= capacity) {
            capacity -= items[i].weight;
            totalProfit += items[i].profit;
        } 
        // If the item can't be fully taken, take the fractional part
        else {
            totalProfit += items[i].profit * ((double)capacity / items[i].weight);
            break; // Knapsack is full after taking this fraction
        }
    }

    return totalProfit;
}

int main() {
    int n, m;  // 'n' is the number of items, 'm' is the capacity of the knapsack
    
    // Take input for the number of items and knapsack capacity
    cout << "Enter the number of items: ";
    cin >> n;
    
    cout << "Enter the capacity of the knapsack: ";
    cin >> m;

    Item items[n];

    // Input profit and weight for each item
    cout << "Enter the profit and weight of each item:\n";
    for (int i = 0; i < n; i++) {
        cout << "Item " << i + 1 << ": ";
        cin >> items[i].profit >> items[i].weight;
    }

    // Calculate the maximum profit using the fractional knapsack algorithm
    double maxProfit = fractionalKnapsack(n, m, items);

    // Print the maximum profit
    cout << "Maximum profit is: " << fixed << setprecision(2) << maxProfit << endl;

    return 0;
}
