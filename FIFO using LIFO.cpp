#include<iostream>
using namespace std;
struct queue1
{
int info1;
queue1 *link1;
}*f1=NULL,*r1=NULL,*newNode1=NULL,*temp1=NULL;
struct queue2
{
int info2;
queue2 *link2;
}*f2=NULL,*r2=NULL,*newNode2=NULL,*temp2=NULL;
void enqueue1(int a)
{
newNode1=new queue1;
newNode1->info1=a;
newNode1->link1=NULL;
if(f1==NULL)//list is empty
{
r1=newNode1;
r1->link1=NULL;
f1=r1;
}
else//u already have the node so the newnode will get insterted at the last means rear end
{
r1->link1=newNode1;
r1=newNode1;
r1->link1=NULL;

}
}
int dequeue1()
{
int a;
if(f1==NULL)
{
cout<<"Already Empty "<<endl;
}
else
{
temp1=f1;
f1=f1->link1;
a=temp1->info1;
delete temp1;
return a;
}
}
void enqueue2(int a)
{
newNode2=new queue2;
newNode2->info2=a;
newNode2->link2=NULL;
if(f2==NULL)//list is empty
{
r2=newNode2;
r2->link2=NULL;
f2=r2;
}
else
{
r2->link2=newNode2;
r2=newNode2;
r2->link2=NULL;
}
}
int dequeue2()
{
int a;
if(f2==NULL)
{
cout<<"Already Empty "<<endl;
}
else
{
temp2=f2;
f2=f2->link2;
a=temp2->info2;
delete temp2;
return a;
}
}
int main()
{
int n;
cout<<"tell me the no of elements u want to insert in this queue"<<endl;
cin>>n;
int i=0,a;
while(i<n)
{
cout<<"Tell me teh val u want to insert"<<endl;
cin>>a;
enqueue1(a);
i++;
}
while(f1!=NULL || f2!=NULL)
{
if(f2==NULL)
{
while(f1->link1!=NULL)
{
enqueue2(dequeue1());
}
cout<<dequeue1()<<endl;
}
else if(f1==NULL)
{
while(f2->link2!=NULL)
{
enqueue1(dequeue2());
}
cout<<dequeue2()<<endl;
}
}
}



