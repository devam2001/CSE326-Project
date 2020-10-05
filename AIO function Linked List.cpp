//PROGRAM TO IMPLEMENT THE LINKED LIST OPERATIONS[INSERTION AND DELETION]
#include<iostream>
#include<conio.h>
using namespace std;
struct node
{
int info;
struct node *link;
};

int item;
// Function to be used....
void traverse();
void insert();
void insert_atstart();
void search();
void insertAtSpecificLoc();
void deletelastnode();
void deleteStart();
void deleteAlter();
void delete_duuplicate();
struct node *head=NULL,*nptr,*ptr,*prev;

int main()
{
int ch;

while(1)
{

cout<<"\n1 for Traversal\n";
cout<<"2 for Insertion at end\n";
cout<<"3 for Insertion at start\n";
cout<<"4 for Searching in a list\n";
cout<<"5 for Insert after specific element\n";
cout<<"6 to Delete the last item from the list\n";
cout<<"7 to Delete the first node from the list\n";
cout<<"8 to Delete alternative node form the list\n";
cout<<"9 to Delete Double node from the list\n";
cout<<"10 for Exit"<<endl;
cin>>ch;
switch(ch)
{
case 1:
traverse();
break;
case 2:
insert();
break;
case 3:
insert_atstart();
break;
case 4:
search();
break;
case 5:
insertAtSpecificLoc();
break;
case 6:
deletelastnode();
break;
case 7:
deleteStart();
break;
case 8:
deleteAlter();
break;
case 9:
delete_duuplicate();
break;
case10:
exit(0);
}
}

}
void traverse()
{
if(head==NULL)
{

cout<<"list empty\n";

}
else
{
cout<<"linked list is\n";

ptr=head;


while(ptr!=NULL)
{

cout<<ptr->info<<"\t";

ptr=ptr->link;
}


}


}

void insert()
{

if(head==NULL)
{

nptr=new node;
cout<<"enter the info part ";
cin>>item;
nptr->info=item;
nptr->link=NULL;
head=nptr;
cout<<"item inserted1\n";
}
else
{

nptr=new node;
cout<<"enter the info part ";
cin>>item;

ptr=head;
while(ptr->link!=NULL)
{
ptr=ptr->link;
}
nptr->info=item;
nptr->link=NULL;
ptr->link=nptr;

cout<<"item inserted";
}

}

void insertAtSpecificLoc()//A B L M Q---->A B L S M Q
{
int key,f=0;
cout<<"Enter the node after which u would like to insert ";
cin>>key;
ptr=head;
while(ptr!=NULL)
{
if(ptr->info==key)//by this u ll match ur item that u r looking for
{
f=1;
break;
}
ptr=ptr->link;
}
if(f==1)
{
nptr=new node;//create a new node allocate a memory
cout<<"Tell me the data that u want to add ";//take the input
cin>>item;
nptr->info=item;//fill the info part
nptr->link=ptr->link;//fill the link for the connectivity
ptr->link=nptr;//update the link to the new node
cout<<"Item has been inserted at the specified position "<<endl;
}
else
cout<<"not found "<<endl;
}

void insert_atstart()
{
if(head==NULL)
{

nptr=new node;
cout<<"enter the info part ";
cin>>item;
nptr->info=item;
nptr->link=NULL;
head=nptr;
cout<<"item inserted1\n";
}
else
{

nptr=new node;
cout<<"enter the info part\n";
cin>>item;
nptr->info=item;
nptr->link=head;
head=nptr;
cout<<"Item inserted at start\n";
}
}

void search()
{
int s,f=0;
cout<<"Enter the node to be searched ";
cin>>s;
ptr=head;
while(ptr!=NULL)
{
if(ptr->info==s)
{
f=1;
break;
}
ptr=ptr->link;
}
if(f==1)
cout<<"\nElement is in the list ";
else
cout<<"Element is not in the list ";
}
/*
u have to delete the last element
11->22->55->66->77
o/P=11->22->55->66 means 66 link will be null
*/
/* Delete the last node
11->12->50->60
op:-11->12->50 means 50 will point to null*/
void deletelastnode()
{
if(head==NULL)//check do we have something in the list
{
cout<<"ur list is already empty!!!!"<<endl;
}
else
{
ptr=head->link;//this will point to 2nd node
prev=head;//this will point to the previous one
while(ptr->link!=NULL)
{
prev=ptr;
ptr=ptr->link;
}
prev->link=ptr->link;//which means null
cout<<"The last node has been deleted from the list "<<endl;
}
}

/*
u have to delete the first element
11->22->55->66->77
output= 22->55->66->77 means start/head will point to next node
*/
void deleteStart()
{
	if(head==NULL)  //check the list
	{
		cout<<"ur list is already empty !!!!"<<endl;
	}
	else
	{
		ptr=head;
		head=ptr->link;//head will point to next node in the list
		cout<<"Node has been deleted from the start !!!";
		delete(ptr);
	}
}
void deleteAlter()
{
	if(head==NULL)
	  {
	  cout<<"Your List is Empty !!!!"<<endl;
	  }
	else
	  {
	     node* prev=head;
	   	 node *ptr=prev->link;
			while(prev!=NULL && ptr!=NULL)
	 	 {
			prev->link=ptr->link;
			prev=prev->link;
			if(prev!=NULL)
		 	ptr=prev->link;
	  	 }
	   }
}
/*
*ptr1=head
while(ptr)
*/
void delete_duuplicate()
{
	node *ptr,*ptr2,*dupl;
	ptr=head;  //ptr=0
	while(ptr!=NULL && ptr->link!=NULL)  //ptr<n
	{
		ptr2=ptr;
		while(ptr2->link!=NULL)
		{
			if(ptr->info==ptr2->link->info)
			{
				dupl=ptr2->link;
				ptr2->link=ptr2->link->link;
				delete(dupl);
			}
			else
			   ptr2=ptr2->link;
		}
		ptr=ptr->link;
	}
}

