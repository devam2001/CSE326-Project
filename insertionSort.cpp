/*INSERTION*SHORT (A,N)
Set A[0] = -8.//-2147483648 or assume first as min
Repeat Step 3 to 5 for K = 2, 3, …, N:
Set TEMP = A[K] and PTR = K – 1.
Repeat while TEMP < A[PTR]:
(a) Set A[PTR+1] = A[PTR]
(b) Set PTR = PTR – 1. [End of Loop.]
Set A[PTR+1] = TEMP.
[End of Loop 2.]
Return.
complexity is O(n^2)
best case O(n)
*/
#include<iostream>
using namespace std;
void insertionsort(int a[],int n)
{
	int t,ptr;
	for(int i=1;i<n;i++)
	{
		t=a[i];
		ptr=i;
		while(t>0 && a[ptr-1]>t)
		{
			a[ptr]=a[ptr-1];
			ptr=ptr-1;
		}
		a[ptr]=t;
	}
	for(int i=0;i<n;i++)
	{
		cout<<a[i]<<" "<<endl;
	}
}
int main()
{
	int n;
	cout<<"Enter Total number of element: ";
	cin>>n;
	int a[n];
	cout<<"Enter the Elements: ";
	for(int i=0;i<n;i++)
	{
		cin>>a[i];
	}
	insertionsort(a,n);
}
