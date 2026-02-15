#include<iostream>
using namespace std;
int main()
{
    float x=100000,y;
    int pin;
    char ch;
    cout<<"enter your pin";
    cin>>pin;
    if(pin==9609)
    {
        cout<<"you have "<< x << " rupees in your account";
        cout<<"\nfor withdraw = w\nfor deposite = d\nfor exit = e";
        cin>>ch;
        while(ch=='w')
        {
            cout<<"enter amount";
            cin>>y;
            x=x-y;
            cout<<"you now have %f rupees in your account"<<x;
            cout<<"\nfor withdraw = w\nfor deposite = d\nfor exit = e";
            cin>>ch;
        }
        while(ch=='d') 
        {
            cout<<"enter amount";
            cin>>y;
            x=x+y; 
            cout<<"you now have %f rupees in your account"<<x;
            cout<<"\nfor withdraw = w\nfor deposite = d\nfor exit = e";
            cin>>ch; 
        }
        if(ch!='w'&&ch!='d')
        {
            cout<<"thanks for using our atm";
            
        }
    }
    else
    {
        cout<<"wrong password try again";
    }
}