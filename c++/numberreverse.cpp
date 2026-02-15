#include<iostream>
using namespace std;
int main()
{
    int n,r;
    cout<<"enter number";
    cin>>n;
    while(n>0)
    {
    r=n%10;
    cout<<""<<r;
    n=(n-r)/10;
    }
}