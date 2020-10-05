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
cout<<"press 3 for Search"<<endl;
cout<<"press 4 for insertion at start or Head"<<endl;
cout<<"press 5 for insertion at specific loc"<<endl;
cout<<"press 6 for Exit"<<endl;
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
search();
break;
case 4:
insertAtStart();
break;
case 5:
insertAtSpecificLoc();
break;
case 6:
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
while(ptr->link!=NULL)//Find out the last node in the list
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
void search()
{
int val,flag=0;
cout<<"Tell me the Value which u r looking ";
cin>>val;
ptr=head;
while(ptr!=NULL )//move ur ptr till end
{
if(ptr->info==val)//meantime match the value with each info part
{
flag=1;//if u got it change the flag value to 1 and break;
break;
}
ptr=ptr->link;//otherwise move ahead by lookibga t address part
}
if(flag==1)
cout<<"Item found";
else
cout<"Item not found";
}
void insertAtStart()
{
newNode=new Node;//allocate memory of Node type means ur structure type which is further int info and link type
cout<<"Enter the Info part ";
cin>>item;
newNode->info=item;
if(head==NULL)
{
newNode->link=NULL;//coz this the only node in the list due to head =null condition so which means it points to nothing
head=newNode;
cout<<"one Item has been inserted to the list when head is empty"<<endl;
}
else
{
newNode->link=head;//this will help to connect the newNodw with the existing first node
head=newNode;//this will help u to change the head towards newnode
cout<"Item inserted at the start or head in the existig list";
}
}
void insertAtSpecificLoc()
{
int s,f=0;
cout<<"enter the node after which u want to get insert";
cin>>s;
ptr=head;//just start ur ptr from the first node
while(ptr!=NULL)//move till end
{
if(ptr->info==s)//this will help u to search the item by comparing with the info part
{
f=1;//u got it change to flag type val to 1
break;//take the break
}
ptr=ptr->link;//move ahead
}
if(f==1)
{
newNode=new Node;
cout<<"tell me the item that u want to insert";
cin>>item;
newNode->info=item;
newNode->link=ptr->link;
ptr->link=newNode;

}
else
{
cout<"not found";
}
}
