#include<iostream>
using namespace std;
void merge(int a[],int low,int high,int mid);
void mergeSort(int a[],int low,int high)
	{
		int mid;
		if(low<high)
		{
			mid=(low+high)/2;
			mergeSort(a,low,mid);
			mergeSort(a,mid+1,high);
			merge(a,low,high,mid);
		}
	}
		void merge(int a[],int low,int high,int mid)
	{
		int i,j,k,c[50];
		i=low;
		k=low;
		j=mid+1;
		while(i<=mid && j<=high)
		{
			if(a[i]<a[j])
			{
				c[k]=a[i];
				i++;
						k++;
			}
		else
		{
			c[k]=a[j];
			j++;	
			k++;

		}
		}
		while(i<=mid)
		{
			c[k]=a[i];
			i++;
			k++;
		}
		while(j<=high)
		{
			c[k]=a[j];
			j++;
			k++;
		}
			for(i=low;i<k;i++)
		{
			a[i]=c[i];
}

}
int main()
{
int a[10],n;
cout<<"Tell me the number of elements u want to enter ";
cin>>n;
cout<<"Now tell me the values ";
for(int i=0;i<n;i++)
{
cin>>a[i];
}
mergeSort(a,0,n-1);
for(int i=0;i<n;i++)
{
cout<<a[i]<<"\t";
}
}


