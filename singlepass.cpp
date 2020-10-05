#include<iostream>
using namespace std;

int *singlePassCall(int a[],int n)
{
for(int i=0;i<n-1;i++)
{
if(a[i]>a[i+1])
{
int t=a[i];
a[i]=a[i+1];
a[i+1]=t;
//update the value of i=-1 so after updated for i++in the loop it becomes 0
i=-1;
}
}
return a;
}
int main()
{
int n;
cout<<"Enter the total no of elements: ";
cin>>n;
int a[n];
cout<<"Enter the elements: ";
for(int i=0;i<n;i++)
{
cin>>a[i];
}
int *ar=singlePassCall(a,n);
for(int i=0;i<n;i++)
{
cout<<ar[i]<<" "<<endl;
}
}
