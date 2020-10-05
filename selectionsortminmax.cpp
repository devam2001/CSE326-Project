/*23 78 45 8 32 56 1 = min=1 max=78
1|23 45 8 32 56|78 =min=8 max=56
1 8| 45 23 32| 56 78=min=23 max=45
1 8 23|32|45 56 78
*/
#include<iostream>
using namespace std;
void selectionsort_minmax(int a[],int n)
{   int i,j;
	for(i=0,j=n-1;i<j;i++,j--)
	{
		int min=a[i],max=a[i];
		int locmin=1,locmax=i;
		for(int k=i;k<=j;k++)
		  {
		  	 if(a[k]>max)
		    {
				max=a[k];
		    	locmax=k;	
			}
			else if(a[k]<min)
			{
				min=a[k];
				locmin=k;
			}
		  } swap(a[i],a[locmin]);
if(a[locmin]==max)
swap(a[j],a[locmin]);
else
swap(a[j],a[locmax]);
	}

}
int main()
{
	int n;
	cout<<"Enter the total no. of elements: ";
    cin>>n;
    int a[n];
    cout<<"Enter the elements: ";
    for(int i=0;i<n;i++)
    {
    	cin>>a[i];
	}
	selectionsort_minmax(a,n);
	for(int i=0;i<n;i++)
	{
		cout<<a[i]<<" "<<endl;
	}
}
