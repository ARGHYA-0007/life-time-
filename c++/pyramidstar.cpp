#include<iostream>
using namespace std;
int main()
{
    int rows,i,j,k;
    cout<<"enter row number:";
    cin>>rows;
    for(i=1;i<=rows;i++)
    {
        for(j=1;j<=rows-i;j++)
        {
            cout<<" ";
        }
        for(k=1;k<=i;k++)
        {
            cout<<"* ";
        }
        cout<<endl;
    }
    return 0;
}