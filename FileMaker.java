import java.io.*; //BufferedWriter, File, FileWriter, IOException
import java.util.*; // List, ArrayList

public class FileMaker {

    //precond, none
    //postcond, new studentInfo file with basic info
    public static void newStudent(String fname, String lname, String osis, String fourdigit, String year){

	String lowf = fname.toLowerCase();
	String lowl = lname.toLowerCase();
        try{
            File file = new File(lowl + lowf + "Info.txt");
            file.createNewFile();
            FileWriter fw = new FileWriter(file);
            BufferedWriter bw = new BufferedWriter(fw);
            bw.write("Student fname, Student lname studentosis,studentid,studentgradyear\n");
            bw.write(fname + "," + lname + "," + osis + "," + fourdigit + "," + year);
            bw.write("\n");
            bw.flush();
            bw.close();

        }catch(IOException e){
	    e.printStackTrace();
        }
    }


    //preconds, all arrays same length.
    //postconds, creates multiple new studentInfo files with basic info
    public static void newStudents(List<String> fname, List<String> lname, List<String> osis, List<String> fourdigit, List<String> year){

	for(int i = 0; i < fname.size(); i++){//goes through the ArrayLists
	    try{	
		File file = new File(lname.get(i).toLowerCase() + fname.get(i).toLowerCase() + "Info.txt");
		file.createNewFile();
		FileWriter fw = new FileWriter(file);
		BufferedWriter bw = new BufferedWriter(fw);
		bw.write("Student fname, Student lname studentosis,studentid,studentgradyear\n");
		bw.write(fname.get(i) + "," + lname.get(i) + "," + osis.get(i) + "," + fourdigit.get(i) + "," + year.get(i));
		bw.write("\n");
		bw.flush();
		bw.close();
		
	    }catch(IOException e){
		e.printStackTrace();
	    }
	}
    }

    public static void newTeacher(String fname, String lname, String TID, String fdigit, String subject){

	String lowf = fname.toLowerCase();
	String lowl = lname.toLowerCase();
        try{
            File file = new File(lowl + lowf + "TeacherInfo.txt");
            file.createNewFile();
            FileWriter fw = new FileWriter(file);
            BufferedWriter bw = new BufferedWriter(fw);
            bw.write("Teacher fname, Student lname, teacher ID, teacher four digit, subject\n");
            bw.write(fname + "," + lname + "," + TID + "," + fdigit + "," + subject);
            bw.write("\n");
            bw.flush();
            bw.close();

        }catch(IOException e){
	    e.printStackTrace();
        }
    }

    public static void newAP(String fname, String lname, String APID, String fdigit, String subject){

	String lowf = fname.toLowerCase();
	String lowl = lname.toLowerCase();
        try{
            File file = new File(lowl + lowf + "TeacherInfo.txt");
            file.createNewFile();
            FileWriter fw = new FileWriter(file);
            BufferedWriter bw = new BufferedWriter(fw);
            bw.write("Teacher fname, Student lname, AP ID, teacher four digit, subject\n");
            bw.write(fname + "," + lname + "," + APID + "," + fdigit + "," + subject);
            bw.write("\n");
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
	    List<String[]> tempFile = ReadCSV.read(fileName);
	    File newF = new File(fileName);
	    FileWriter fw = new FileWriter(newF);
	    BufferedWriter bw = new BufferedWriter(fw);
	    String[] tempNew = new String[newLine.size()];
	    for(int i = 0; i < newLine.size(); i++){
		tempNew[i] = newLine.get(i);
	    }
	    tempFile.set(lineNum, tempNew);
	    for(int i = 0; i < tempFile.size(); i++){
		String tempLine = "";
		for(int j = 0; j < tempFile.get(i).length; j++){
		    if(j < tempFile.get(i).length - 1){
			tempLine += tempFile.get(i)[j] + ",";
		    }
		    else{
			tempLine += tempFile.get(i)[j] + "\n";
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
	    List<String[]> tempFile = ReadCSV.read(fileName);
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
		for(int j = 0; j < tempFile.get(i).length; j++){
		    if(j < tempFile.get(i).length - 1){
			tempLine += tempFile.get(i)[j] + ",";
		    }
		    else{
			tempLine += tempFile.get(i)[j] + "\n";
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

    public static void writeFile(String fileName, List<String[]> towrite){
	try{
	    File newF = new File(fileName);
	    FileWriter fw = new FileWriter(newF);
	    BufferedWriter bw = new BufferedWriter(fw);
	    for(int i = 0; i < towrite.size(); i++){
		String tempLine = "";
		for(int j = 0; j < towrite.get(i).length; j++){
		    if(j < towrite.get(i).length - 1){
			tempLine += towrite.get(i)[j] + ",";
		    }
		    else{
			tempLine += towrite.get(i)[j] + "\n";
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

    public static void addOsisFdigit(){
	String osis = "";
	String fdigit = "";
	Scanner s = new Scanner(System.in);
	List<String> line = new ArrayList<String>();
	System.out.println("OSIS");
	if(s.hasNext()){
	    osis = (s.nextLine());
	}
	System.out.println("4 digit");
	if(s.hasNext()){
	    fdigit = (s.nextLine());
	}
	line.add(osis);
	line.add(fdigit);
	appendLine("osis_fdigit.txt", line);
    }

    public static void addTID(){
	String tid = "";
	String fdigit = "";
	Scanner s = new Scanner(System.in);
	List<String> line = new ArrayList<String>();
	System.out.println("6 digit TID");
	if(s.hasNext()){
	    tid = (s.nextLine());
	}
	System.out.println("4 digit");
	if(s.hasNext()){
	    fdigit = (s.nextLine());
	}
	line.add(tid);
	line.add(fdigit);
	appendLine("TID.txt", line);
    }

    //working tests

    public static void main(String[] args) {
	/*
	  newStudent("christopher", "sherling", "205704083", "3750", "2017");
	  List<String> fn = new ArrayList<String>();
	  List<String> ln = new ArrayList<String>();
	  List<String> os = new ArrayList<String>();
	  List<String> fd = new ArrayList<String>();
	  List<String> sy = new ArrayList<String>();
	  fn.add("lob");
	  fn.add("lol");
	  fn.add("kek");
	  fn.add("tek");
	  fn.add("lok");
	  ln.add("top");
	  ln.add("top");
	  ln.add("top");	
	  ln.add("top");
	  ln.add("top");

	  for(int i = 0; i < 5; i++){
	  os.add(((int)(Math.random() * 900000000) + 100000000) + "");
	  fd.add(((int)(Math.random() * 9000) + 1000) + "");
	  sy.add(((int)(Math.random() * 4) + 2016) + "");
	  }
	  newStudents(fn, ln, os, fd, sy);
	  changeLine("toplobInfo.txt", 0, fn);
	*/
	List<String> tid = new ArrayList<String>();
	tid.add("000000");
	tid.add("0000");
	appendLine("TID.txt", tid);
    }
    /*
     */
}
