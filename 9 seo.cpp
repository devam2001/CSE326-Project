#include<iostream>
using namespace std;
//stack with array
# define SIZE 6
void push();
void pop();
void display();
int stack[SIZE];
int top=-1;//wop points to nothing currently
int main()
{
char ch;
do
{

int option;
cout<<"***welcome to stack array operation***"<<endl;
cout<<"press 1 for insert "<<endl;
cout<<"press 2 for delete "<<endl;
cout<<"press 3 for display "<<endl;
cout<<"press 4 for Exit "<<endl;
cout<<"Tell m ur choice "<<endl;
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
void push()
{
int data;
if(top==SIZE-1)
{
cout<<"sorry no space "<<endl;
}
else
{
cout<<"tel m the data that u want to enter "<<endl;
cin>>data;
top=top+1;
stack[top]=data;
cout<<"value is inserted in the last "<<endl;
}
}
void pop()
{
if(top==-1)
{
cout<<"its already empty "<<endl;
}
else
{
int temp;
temp=stack[top];
top=top-1;
cout<<"the element from top is deleted "<<endl;
}
}
void display()
{
if(top==-1)
{
cout<<"its already empty "<<endl;
}
for(int i=top;i>=0;i--)
{
cout<<"Element in the stack are "<<stack[i]<<endl;
}

}
