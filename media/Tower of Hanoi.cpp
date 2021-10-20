#include<iostream>
using namespace std;
int t(int n,char beg,char aux,char ed)
{
    if(n>=1)
    {
        t(n-1,beg,ed,aux);
        cout<<endl<<beg<<" to "<<ed;
        t(n-1,aux,beg,ed);
    }
}
int main()
{
    int n;
    char beg,aux,ed;
    cin>>n>>beg>>aux>>ed;
    t(n,beg,aux,ed);
}
