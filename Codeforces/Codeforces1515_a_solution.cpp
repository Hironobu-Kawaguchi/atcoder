// https://codeforces.com/contest/1515/problem/A
#include <bits/stdc++.h>
using namespace std;

void solve(){
  int n,x;
  int w[101];
  cin>>n>>x;
  int sum=0;
  for (int i=0;i<n;i++){
    cin>>w[i];
    sum+=w[i];
  }
  //if the sum is x, we cannot avoid the explosion
  if (sum==x){
    cout<<"NO"<<endl;
    return;
  }
  cout<<"YES"<<endl;
  //otherwise, the answer always exists
  //we will keep adding elements from left to right
  //if we can't add element i, we add element i+1 first by swapping the two
  for (int i=0;i<n;i++){
    if (x==w[i]){
      //i+1 will always be less than n because otherwise, the total sum would be x
      swap(w[i],w[i+1]);
    }
    cout<<w[i]<<' ';
    x-=w[i];
  }
  cout<<endl;
  return;
}

int main(){
  int T; cin>>T;
  while (T--)
    solve();
  return 0;
}