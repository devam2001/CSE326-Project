/*
This algorithm sorts an array A with N elements.
SELECTION(A, N)
Repeat steps 2 and 3 for k=1 to N-1:
Call MIN(A, K, N, LOC).
[Interchange A[k] and A[LOC]]
Set Temp:= A[k], A[k]:= A[LOC] and A[LOC]:=Temp.
[End of step 1 Loop.]
Exit.

MIN(A, K, N, LOC).
Set MIN := A[K] and LOC:= K.
Repeat for j=k+1 to N:
If Min>A[j], then: Set Min:= A[j] and LOC:=J.
[End of if structure]
Return.
complexity :-O(n^2)
*/
#include<iostream>
using namespace std;
display(int a[],int n)
{
	for(int i=0;i<n;i++)
	{
		cout<<a[i]<<" "<<endl;
	}
}
void selectionsort(int a[],int n)
{
	int indexmin;
	for(int i=0;i<n-1;i++)
	{
		indexmin=i;
		for(int j=i+1;j<n;j++)
			if(a[j]<a[indexmin])
				indexmin=j;
				
				swap(a[i],a[indexmin]);
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
	selectionsort(a,n);
	display(a,n);
}
