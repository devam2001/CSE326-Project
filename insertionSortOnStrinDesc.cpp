#include<iostream>

using namespace std;

void insertionSort(string a[], int n)
{

int i,j;
for(i=0;i<n;i++)
{
string temp=a[i];
j=i-1;
while(j>=0 && a[j]<temp)
{
a[j+1]=a[j];
j--;
}
a[j+1]=temp;

}


cout<<"array after sorting:"<<endl;
for(i=0;i<n;i++)
{
cout<<a[i]<<" ";
}
}
int main()
{

string a[50];
int n=6;
for(int i=0;i<n;i++)
{
getline(cin,a[i]);
}

insertionSort(a,n);
}
