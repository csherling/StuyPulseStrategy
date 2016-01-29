import java.util.*; //scanner

public class EScout{

    private static Scanner s = new Scanner(System.in);
    private static List<List<String>> _teams;

    public static void startUp(){
	System.out.println("Welcome!");
	System.out.println("Please wait while the system loads");
	_teams = ReadCSV.read("TEAMS.txt");
	System.out.println("Done!");
    }

    public static void menu(){

    }

    //----------------------UTILITY METHODS-----------------------

    public static void stall(){
	Scanner s = new Scanner(System.in);
	System.out.println("Type anything and press enter to continue");
	if(s.hasNext()){
   
	}
    }
    public static void quit(){
	clear();
	System.exit(1);
    }
    public static void clear(){	
	System.out.print("\033[H\033[2J");
	System.out.flush();
    }

    //----------------------END UTILITY METHODS-----------------------

    public static void main(String[] args){

    }

}