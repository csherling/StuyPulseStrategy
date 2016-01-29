import java.io.*; //BufferedWriter, File, FileWriter, IOException
import java.util.*; // List, ArrayList

public class FileMaker {

    //precond, none
    //postcond, new studentInfo file with basic info
    public static void newTeam(String teamNum){

        try{
            File file = new File(teamNum + ".txt");
            file.createNewFile();
            FileWriter fw = new FileWriter(file);
            BufferedWriter bw = new BufferedWriter(fw);
            bw.write(teamNum);
            bw.write("\n");
            bw.write("Matches");
            bw.write("\n\n");
            bw.write("High,Low");
            bw.flush();
            bw.close();

        }catch(IOException e){
	    e.printStackTrace();
        }
    }

    //preconds, filename is full, including .txt.
    //postconds, file line changed
    public static void changeLine(String fileName, int lineNum, List<String> newLine){
        try{
	    List<List<String>> tempFile = ReadCSV.read(fileName);
	    File newF = new File(fileName);
	    FileWriter fw = new FileWriter(newF);
	    BufferedWriter bw = new BufferedWriter(fw);
	    tempFile.set(lineNum, newLine);
	    for(int i = 0; i < tempFile.size(); i++){
		String tempLine = "";
		for(int j = 0; j < tempFile.get(i).size(); j++){
		    if(j < tempFile.get(i).size() - 1){
			tempLine += tempFile.get(i).get(j) + ",";
		    }
		    else{
			tempLine += tempFile.get(i).get(j) + "\n";
		    }
		}
		bw.write(tempLine);
	    }
	    bw.flush();
	    bw.close();
	}
        catch(IOException e){
	    e.printStackTrace();
        }
	
    }

    public static void appendLine(String fileName, List<String> newLine){
        try{
	    List<List<String>> tempFile = ReadCSV.read(fileName);
	    File newF = new File(fileName);
	    FileWriter fw = new FileWriter(newF);
	    BufferedWriter bw = new BufferedWriter(fw);
	    String tempNew = "";
	    for(int i = 0; i < newLine.size(); i++){
		if(i < newLine.size() - 1){
		    tempNew += newLine.get(i);
		    tempNew += ",";
		}
		else{
		    tempNew += newLine.get(i);
		}
	    }
	    for(int i = 0; i < tempFile.size(); i++){
		String tempLine = "";
		for(int j = 0; j < tempFile.get(i).size(); j++){
		    if(j < tempFile.get(i).size() - 1){
			tempLine += tempFile.get(i).get(j) + ",";
		    }
		    else{
			tempLine += tempFile.get(i).get(j) + "\n";
		    }
		}
		bw.write(tempLine);
	    }
	    bw.write(tempNew);
	    bw.flush();
	    bw.close();
	}
        catch(IOException e){
	    e.printStackTrace();
        }
	
    }

    public static void writeFile(String fileName, List<List<String>> towrite){
	try{
	    File newF = new File(fileName);
	    FileWriter fw = new FileWriter(newF);
	    BufferedWriter bw = new BufferedWriter(fw);
	    for(int i = 0; i < towrite.size(); i++){
		String tempLine = "";
		for(int j = 0; j < towrite.get(i).size(); j++){
		    if(j < towrite.get(i).size() - 1){
			tempLine += towrite.get(i).get(j) + ",";
		    }
		    else{
			tempLine += towrite.get(i).get(j) + "\n";
		    }
		}
		bw.write(tempLine);
	    }
	    bw.flush();
	    bw.close();
	}
        catch(IOException e){
	    e.printStackTrace();
        }
    }

    public static void main(String[] args) {

	newTeam("694");

	List<String> fn = new ArrayList<String>();

	fn.add("Lol");
	fn.add("Kek");

	changeLine("694.txt", 2, fn);
	
	List<String> tid = new ArrayList<String>();
	tid.add("000000");
	tid.add("0000");
	appendLine("694.txt", tid);
	/*
	 */
    }
    /*
     */
}
