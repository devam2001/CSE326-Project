/*INSERTION*SHORT (A,N)
Set A[0] = -8.//-2147483648 or assume first as min infinity
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

void insertionSort(string a[], int n)
{

int i,j;
for(i=1;i<n;i++)
{
string temp=a[i];
j=i-1;
while(j>=0 && a[j]>temp)
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
int n=5;
for(int i=0;i<n;i++)
{
getline(cin,a[i]);
}

insertionSort(a,n);
}
