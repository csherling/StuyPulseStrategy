import java.io.*;
import java.util.*;

public class ReadCSV{

    public static List<String[]> read(String filename) {
	List<String[]> info = new ArrayList<String[]>();
	String line = null;

	try {
	    BufferedReader br = new BufferedReader(new FileReader(filename));

	    while((line = br.readLine()) != null) {
		info.add(line.split(","));
            }

	    br.close();
	}

	catch(IOException e) {
	    System.err.print(e);
	}
	return info;
    }

    /*
    public static void main(String[] args){
	long x = System.currentTimeMillis();
	List<String[]> s = read("Book.java");
	System.out.println(s);
	long y = System.currentTimeMillis();
	System.out.println(y - x);
    }
    */

}