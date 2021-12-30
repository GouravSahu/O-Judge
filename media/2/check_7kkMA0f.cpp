#include<bits/stdc++.h>
using namespace std;

int rec(int n)
{
    if(n<=0)return 0;
    if(n==1)return 0;
    if(n==2)return 1;
    
    return rec(n-1)+rec(n-2);
}


int main()
{
    int t;
    cin>>t;

    while(t--)
    {
        int n;
        cin>>n;

        cout<<rec(n)<<endl;
    }

}