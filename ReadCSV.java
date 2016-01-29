import java.io.*;
import java.util.*;

public class ReadCSV{

    public static List<List<String>> read(String filename) {
	List<List<String>> info = new ArrayList<List<String>>();
	String line = null;

	try {
	    BufferedReader br = new BufferedReader(new FileReader(filename));

	    while((line = br.readLine()) != null) {
		String[] lin = line.split(",");
		List<String> e = new ArrayList<String>();
		for(int i = 0; i < lin.length; i++){
		    e.add(lin[i]);
		}
		info.add(e);
            }

	    br.close();
	}

	catch(IOException e) {
	    System.err.print(e);
	    System.out.println("Error in Reading the File");
	}
	return info;
    }


    public static void main(String[] args){
	long x = System.currentTimeMillis();
	List<List<String>> s = read("CSVTEST.txt");
	System.out.println(s);
	long y = System.currentTimeMillis();
	System.out.println(y - x);
    }
    /*
    */

}