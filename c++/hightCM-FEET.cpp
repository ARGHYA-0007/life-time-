#include<iostream>
using namespace std;
int main()
{
    int x,r;
    float y,z,c,a;

    cout<<"enter 1 for cm to feet\nenter2 for feet to cm";
    cin>>x;
    if(x==1)
    {
        cout<<"enter your hight in cm";
        cin>>y;
        // cout<<"your  hight in feet is:"<<y*0.0328084;
        z=y*0.0328084;
        c=z-int(z);
        c=c*12;
        r=z;
        cout<<r<<"feets and"<<c<<"inches";


    }
    else if(x==2)
    {

        cout<<"enter the feet first(with out inches) ";
        cin>>y;
        cout<<"enter the inches now";
        cin>>a;
        a=a/12;
        y=y+a;
        cout<<"your  hight in cm is:"<<y*30.48;
    }
    else
    {
        cout<<"bhag yaha se 2 footia\nthik se 1 or 2 nehi daba sakta\nchala hay calculate karne";
    }

}
