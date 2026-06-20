#include<iostream>
#include<fstream>

using namespace std;


string encrypt(string p){


for(char &c:p)

c+=3;


return p;

}



int main(){


string site,password;


cout<<"Website:";

cin>>site;



cout<<"Password:";

cin>>password;



ofstream file(
"password.txt",
ios::app
);



file<<site<<" : "
<<encrypt(password)
<<endl;



file.close();


cout<<"Saved";


return 0;

}