#include<iostream>
using namespace std;
int enqueue(int a[],int val);
int dequeue(int a[]);
int peek(int a[]);
int f=-1,r=-1;
int n=5;
int main()
{
	int val,ch,a[n];
	while(1)
		{
			cout<<"Press 1: For Enqueue"<<endl;
			cout<<"Press 2: For Dequeue"<<endl;
			cout<<"Press 3: For Peek"<<endl;
			cout<<"Press 4: For EXit"<<endl;
			cout<<"Tell me ur choice"<<endl;
			cin>>ch;
			switch(ch)
			{
				case 1:		cout<<"Tell me which value u want to insert in the Queue"<<endl;
							cin>>val;
							enqueue(a,val);break;
				case 2:		dequeue(a);break;
				case 3:		peek(a);break;
				case 4:		exit(1);break;
				default:	cout<<"Wrng choice....."<<endl;
			}
		}

}
int enqueue(int a[],int val)
{
	if((f==0 && r==n-1)||(f==r+1))
{
	cout<<"Overflow..."<<endl;
	return 0;
}
else if(f==-1)//this is when queue is empty
{
	f=r=0;
}
else if(r==n-1)//this is when rear reach to last but u have space at front
{
	r=0;
}	
else//else insert the val at rear one by one
{
	r=r+1;
}
	a[r]=val;
}
int dequeue(int a[])
{
	if(f==-1)
{
	cout<<"underflow..."<<endl;
	return 0;
}
int temp=a[f];
if(f==r)
{
f=r=-1;
}
else if(f==n-1)
{
f=0;
}
else
{
f=f+1;
}
cout<<"The deleted elment from front end is "<<temp<<endl;
}
int peek(int a[])
{
int ptr=f;
if((ptr==-1))
{
cout<<"Queue is empty "<<endl;
return 0;
}
cout<<"\n Elements in the queue are "<< endl;
while(ptr!=r)
{
cout<<a[ptr]<< " ";
if(ptr==n-1)
ptr=0;
else
ptr++;
}
cout<<a[ptr]<<endl;//print the last element
}
