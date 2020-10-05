/*Algorithm: Merging (A, R,B,S,C)
Here A and B be sorted arrays with R and S elements
respectively. This algorithm merges A and B into an array
C with N=R+ S elements
Step 1: Set NA=1, NB=1 and NC=1
Step 2: Repeat while NA = R and NB = S:
		if A[NA] = B[NB], then:
		Set C[NC] = A[NA]
		Set NA = NA +1
		else
			Set C[NC] = B[NB]
			Set NB = NB +1
		[End of if structure]
		Set NC= NC +1
		[End of Loop]
Step 3: If NA >R, then:
	Repeat while NB = S:
	Set C[NC] = B[NB]
	Set NB = NB+1
	Set NC = NC +1
	[End of Loop]
	else
	Repeat while NA = R:
	Set C[NC] = A[NA]
	Set NC = NC + 1
	Set NA = NA +1
		[End of loop]
	[End of if structure]
Step 4: Return C[NC]*/

#include<iostream>
using namespace std;
void callMerge(int A[],int B[],int na,int nb,int C[])
{
	int i=0,j=0,k=0;
	while(i<na && j<nb)
	{
		if(A[i]<B[j])
		   C[k++]=A[i++];
		else
			C[k++]=B[j++];
	}
	while(i<na)
	   C[k++]=A[i++];
	while(j<nb)
		C[k++]=B[j++];
}
int main()
{
	int a[]={44,55,66};
	int na=sizeof(a)/sizeof(a[0]);
	int b[]={34,56,96};
	int nb=sizeof(b)/sizeof(b[0]);
	int c[nb+na];
	callMerge(a,b,na,nb,c);
cout<<"after merge operation"<<endl;
for(int i=0;i<na+nb;i++)
{
cout<<c[i]<<" ";
}
}
