#include <iostream>
#include <vector>
using namespace std;
int main()
{
   /* int n,k=0;
    vector <int>v(5,10);
    vector <string>v1(5,"Sahu");
    vector <int>:: iterator a;
    for(int i=0;i<5;i++)
    {
        cout<<v1[i]<<endl;
    }
    cout<<v1.front()<<endl;
    cout<<v1.back()<<endl;
    v1.pop_back();
    cout<<v1.size()<<endl;
    cout<<v1.capacity();
    */

    vector <vector<int>>v;
    for(int i=0;i<3;i++)
    {
        vector<int>v1;
        for(int j=0;j<3;j++)
        {
            v1.push_back(i);
        }
        v.push_back(v1);
    }
    for(int i=0;i<v.size();i++)
    {
        for(int j=0;j<v[i].size();j++)
        {
            cout<<v[i][j];
        }
        cout<<'\n';
    }

   /* push_back();
    pop_back();
    capacity();
    size();
    at();// index is passed ...
    clear();
    [];
    front();// returns the first value...
    back();// returns the last value...
    */


}
