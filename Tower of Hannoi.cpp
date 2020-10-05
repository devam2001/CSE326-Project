#include<iostream>
using namespace std;
void toh(int n,char src,char aux,char des)
{
	if(n==1)
	{
		cout<<"moved the disk "<<n<<" from "<<src<<" to "<<des<<endl;
		return;
	}
	   toh(n-1,src,des,aux);
       cout<<"moved the disk "<<n<<" from "<<src<<" to "<<des<<endl;
		toh(n-1,aux,src,des);
	}
		int main()
		{
			cout<<"how many disk ";
			int n;
			cin>>n;
			toh(n,'a','b','c');
			return 0;  
		}
