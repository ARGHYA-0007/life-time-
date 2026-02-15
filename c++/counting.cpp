#include<iostream>
using namespace std;
int main()
{
    int x,i;
    cout<<"enter your number";
    cin>>x;
    for(i=1;i<=x;i++)
    {
        cout<<" "<<i;
    }
      i=x-1;
    for(i>=x;i>=1;i=i-1)
    {
        cout<<" "<<i; 
    }
}