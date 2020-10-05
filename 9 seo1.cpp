#include<iostream>
using namespace std;
struct Node
{
int info;
Node *link;
};
struct Node *top=NULL,*newNode,*ptr;
void push()
{
int val;
newNode=new Node;
cout<<"Tell me the data that u want to store"<<endl;
cin>>val;
newNode->info=val;
newNode->link=top;
top=newNode;
}
void pop()
{
//LIFO last in first Out
if(top==NULL)
{
cout<<"already its empty"<<endl;
}
else
{

top=top->link;//top point to ur next part by looking at address
}
}
/* give input as 100,200,300:-stack
o/p:-300,200,100
*/

void display()
{
ptr=top;
if(top==NULL)
cout<<"Stack is Full"<<endl;
else
{
while(ptr!=NULL)
{
cout<<ptr->info<<endl;
ptr=ptr->link;
}

}

}

int main()
{
char ch;
do
{

int option;
cout<<"***welcome to stack array operation***"<<endl;
cout<<"press 1 for insert"<<endl;
cout<<"press 2 for delete"<<endl;
cout<<"press 3 for display"<<endl;
cout<<"press 4 for Exit"<<endl;
cout<<"Tell m ur choice"<<endl;
cin>>option;
switch(option)
{
case 1:
push();
break;
case 2:
pop();
break;
case 3:
display();
break;
case 4:
exit(0);
}


cout<<"Do u want to continue press y "<<endl;
cin>>ch;
}
while(ch=='y' || ch=='Y');
}
