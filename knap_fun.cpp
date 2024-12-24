#include<bits/stdc++.h>
using namespace std;

void input(int &n,int &m,int profit[],int weight[])

{
    cout<<"Enter the number of item:";
    cin>>n;
    cout<<"Enter the capacity of knapsack:";
    cin>>m;
    
    //take input profit and weight
    
    for (int i=1;i<=n;i++)
    {
    cout << "Enter profit and weight of item " << i << ": ";
    cin>>profit[i]>>weight[i];
    }
}

int knapsack(int profit[],int weight[],int n, int m)

{
    //create a table to store
    int k[n+1][m+1];
    //solution
    for (int i=0;i<=n;i++)
    {
        for(int w=0;w<=m;w++)
        {
            if (i==0 || w==0)
            {
                k[i][w]=0;
            }
            else if(weight[i]<=w)
            {
                k[i][w]=max(profit[i]+k[i-1][w-weight[i]],k[i-1][w]);
            }
            else
            {
               k[i][w]= k[i-1][w];
            }
        }
    }
   // cout<<"profit for knapsack is:"<<k[n][m]<<endl;
   //return the max profit in the bottom right corner
   return k[n][m];
}

int main()



{
int n,m; 
int profit[100],weight[100];
//take input
input(n,m,profit,weight);
int maxprofit=knapsack(profit,weight,n,m);
cout<<"Maximum profit:"<<maxprofit<<endl;
    
    
    return 0;
}