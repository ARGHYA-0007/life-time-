#include<iostream>
using namespace std;
int main()
{
    int y,Y,M,m;
    cout<<"enter your birth year";
    cin>>y;
    Y=2025-y;
    cout<<"your age is "<<Y;
    cout<<"enter your month";
    cin>>m;
    if(m>=6)
    {
    M=m-6;
    }
    else
    M=6-m; 

    cout<<"month is "<<M;


}