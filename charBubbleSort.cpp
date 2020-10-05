#include<iostream>                       
using namespace std;					 

int bubbleSort(char[], char);

int main()						
{
	const int NUM_ELE = 20; 			
	char dB[NUM_ELE] = { 'x','b','A','X','w','T','M','e','n','Z','z','d','Q','L','K','j','S','v','q','R'};
	int i, moves;
	char temp;
	cout<< 	"	This program sort the the 20 elements in alphabetic order"<<endl;

	for(int i = 0; i < NUM_ELE; i++)
		for(int j = 0; j < NUM_ELE-1; j++)
		{
			if(dB[j+1] < dB[j])
			{
				temp = dB[j];
				dB[j] = dB[j+1];
				dB[j+1] = temp;
			}
		}

	for(int i = 0; i < NUM_ELE; i++)
		cout<<dB[i] <<" ";

	return 0;
}

