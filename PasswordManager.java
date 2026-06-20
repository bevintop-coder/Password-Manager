import java.util.Scanner;


public class PasswordManager {


static String password="";


public static void main(String args[]){


Scanner sc=new Scanner(System.in);


System.out.println("SecureVault Password Manager");


System.out.print("Enter Master Password:");

password=sc.nextLine();



while(true){


System.out.println(
"1.Add Password\n2.View Password\n3.Exit"
);


int choice=sc.nextInt();


sc.nextLine();



if(choice==1){


System.out.print("Website:");

String site=sc.nextLine();


System.out.print("Password:");

String pass=sc.nextLine();



Encryption.save(site,pass);



}


else if(choice==2){

Encryption.read();

}


else{

break;

}


}


}

}