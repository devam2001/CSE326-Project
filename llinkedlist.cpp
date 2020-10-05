//Program to implement linklist
#include<iostream>
using namespace std;
struct Node
{
int info;
struct Node *link;
};
int item;
//function to be get used for various operations
void traverse();
void insert();
void search();
void insertAtStart();
void insertAtSpecificLoc();
struct Node *head=NULL,*newNode,*ptr;
int main()
{
int choice;
while(1)
{
cout<<"Press 1 for Traverse"<<endl;
cout<<"press 2 for insert"<<endl;
cout<<"press 3 for Exit"<<endl;
cout<<"enter ur choice"<<endl;
cin>>choice;
switch(choice)
{
case 1:
traverse();
break;
case 2:
insert();
break;
case 3:
exit(0);

}
}
}
void insert()
{
if(head==NULL)
{
newNode=new Node;//allocate memory of Node type means ur structure type which is further int info and link type
cout<<"Enter the Info part ";
cin>>item;
newNode->info=item;
newNode->link=NULL;//coz this the only node in the list due to head =null condition so which means it points to nothing
head=newNode;
cout<<"one Item has been inserted to the list when head is empty"<<endl;
}
else
{
newNode=new Node;//allocate memory of Node type means ur structure type which is further int info and link type
cout<<"Enter the Info part ";
cin>>item;
newNode->info=item;
ptr=head;
while(ptr->link!=NULL)//Find outr the last node in the list
{
ptr=ptr->link;//this logic will help u to move ahead by looking at the address part
}
newNode->link=NULL;//insert as last node so link is null
ptr->link=newNode;//the existing last node will point to the newnodeinserted at last
cout<<"Item Inserted at the last"<<endl;
}
}
void traverse()
{
if(head==NULL)
{
cout<<"list is empty"<<endl;
}
else
{

ptr=head;
while(ptr!=NULL)
{
cout<<ptr->info<<"\t"<<endl;
ptr=ptr->link;
}
}
}
