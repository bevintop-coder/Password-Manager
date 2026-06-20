import java.io.*;


public class Encryption {



static void save(String site,String pass){


try{


FileWriter fw=
new FileWriter("passwords.txt",true);



fw.write(site+" : "+
encrypt(pass)+"\n");



fw.close();


System.out.println("Saved");


}catch(Exception e){}


}



static void read(){


try{


BufferedReader br=
new BufferedReader(
new FileReader("passwords.txt")
);



String line;


while((line=br.readLine())!=null){


System.out.println(line);


}



}catch(Exception e){}


}



static String encrypt(String text){


return new StringBuilder(text)
.reverse()
.toString();


}


}