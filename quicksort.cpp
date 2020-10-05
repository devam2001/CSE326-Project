#include<iostream>
using namespace std;
void swap(int *a,int *b)
{
int temp=*a;
*a=*b;
*b=temp;
}
int partition(int a[],int s,int l)
{
int pivot=a[l];
int pindex=s;
for(int i=s;i<=l-1;i++)
{
if(a[i]<pivot)
{
swap(&a[pindex],&a[i]);
pindex++;
}
}
swap(&a[pindex],&a[l]);
return pindex;

}
void quickSort(int a[],int s,int l)
{
if(s<l)
{
int p=partition(a,s,l);
quickSort(a,s,p-1);
quickSort(a,p+1,l);
}
}
int main()
{
int a[]={23,66,51,80,13,4};
int n=sizeof(a)/sizeof(a[0]);
quickSort(a,0,n-1);
for(int i=0;i<n;i++)
cout<<a[i]<<" ";
}
