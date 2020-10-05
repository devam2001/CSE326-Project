#include<iostream>
using namespace std;
struct node
{
	string info;
	node *link;
} 
*f=NULL,*r=NULL;
void enqueue(node *n);
void dequeue();
void peek();
int main()
{
	int in,d;
	node *newNode;
	cout<<"How many time do you want to peform insertion "<<endl;
	cin>>in;
	cout<<"How many time do you want to peform deletion "<<endl;
	cin>>d;
	if(in>0)
	{   cout<<"Value you want to hold"<<endl;
		for(int i=0;i<in;i++)
		{
			newNode=new node;
			cin>>newNode->info;
			newNode->link=NULL;
			enqueue(newNode);
		}
	}
	int counter=0;
	node *ptr=f;
	while(ptr!=NULL)
	{
       counter++;
	   ptr=ptr->link;	
	}
	if(counter<d)
	{
		cout<<"Not enough resource "<<endl;
	}
	else
	{
		for(int i=0;i<d;i++)
		{
			dequeue();
		}
	}
	
}
void enqueue(node *newNode)
{
	if(f==NULL)
	{
		f=r=newNode;
	}
	else
	{
		r->link=newNode;
		r=newNode;
	}
}
void dequeue()
{
	if(f==NULL)
	{
		cout<<"Empty "<<endl;
		return;
	}
	else if(f==r)
	{
		node *temp=f;
		f=r=NULL;
		delete temp;
	}
	else 
	{
		node *temp=f;
		f=f->link;
		delete temp;
	}
}
void peek()
{
	node *ptr=f;
	if(ptr==NULL)
	{
		cout<<"Empty Queue  "<<endl;
		return;
	}
	cout<<f->info<<" ";
	cout<<r->info;
}
