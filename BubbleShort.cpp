/* bubble short
1. Set I=0,J=0
2.Repeat I=0 to n-1
     Repeat J=0 to n-i-1
     		if A[j] > A[j+1]
     		//swap
     			t=A[j]
     			A[j]=A[j+1]
     			A[j+1]=t
     		n+n-1+n-2
     		
     	*/
#include<iostream>
using namespace std;
void callToBubbleShort(int a[],int n)
{
	int i,j,t;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n-1;j++)
		{
			if(a[j]>a[j+1])
			{
				t=a[j];
				a[j]=a[j+1];
				a[j+1]=t;
			}
		}
	}
	cout<<"Shorted Elements";
	for(i=0;i<n;i++)
	{
		cout<<a[i]<<" ";
	}
}
int main()
{
int a[20],i,n;
cout<<"Enter the elements : ";
cin>>n;
cout<<"Enter the values: \n";
for(i=0;i<n;i++)
{

cin>>a[i];
}
callToBubbleShort(a,n);
}
