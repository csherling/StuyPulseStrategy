import java.io.*; //IOException
import java.util.*; //scanner

public class EScout{

    private static Scanner s = new Scanner(System.in);
    private static List<List<String>> _teams;

    public static void startUp(){
	System.out.println("Welcome!");
	System.out.println("Loading teams list");
	_teams = ReadCSV.read("TEAMS.txt");
	System.out.println("Done!");
    }

    //-----------------------MENUS----------------------

    public static void menu(){
	clear();
	System.out.println("What would you like to do?");
	System.out.println("Enter the corresponding number.");
	System.out.println("(1) New Sheet");
	System.out.println("(2) Edit Sheet");
	System.out.println("(3) Load Sheet");
	System.out.println("(4) Quit");
	String x = "";
	while(true){
	    if(s.hasNext()){
		x = (s.nextLine());
	    }   
	    if(x.equals("1")){
		addTeam();
		break;
	    }
	    else if(x.equals("2")){
		editMenu();
		break;
	    }
	    else if(x.equals("3")){
		loadSheet();
		break;
	    }
	    else if(x.equals("4")){
		quit();
	    }
	    else{
		System.out.println("Please re-specify");
	    }
	}

    }

    public static void editMenu(){
	System.out.println("What would you like to edit?");
	System.out.println("(1) Add Match Data");
	String x = "";
	while(true){
	    if(s.hasNext()){
		x = (s.nextLine());
	    }   
	    if(x.equals("1")){
		addMatchData();
		break;
	    }
	    else{
		System.out.println("Please re-specify");
	    }
	}
    }

    //-----------------------END MENUS----------------------

    //----------------------MENU METHODS-----------------------

    public static void addTeam(){
	String team = "";
	String confirm = "";
	String cont = "";
	while(true){
	    while(true){
		clear();
		System.out.println("What is the number of the team?");
		if(s.hasNext()){
		    team = (s.nextLine());
		}   
		System.out.println("Is " + team + " the correct number?");
		System.out.println("y/n");
		if(s.hasNext()){
		    confirm = (s.nextLine());
		}   
		if(confirm.equals("y")){
		    FileMaker.newTeam(team);
		    break;
		}
		else{
		    System.out.println("Please Re-enter!");
		}
	    }
	    System.out.println("Would you like to add another team?");
	    System.out.println("y/n");
	    if(s.hasNext()){
		cont = (s.nextLine());
	    }
	    if(!(cont.equals("y"))){
		break;
	    }
	}
    }

    public static void addMatchData(){
	System.out.println("To Be Written");
    }

    public static void loadSheet(){
	String team = "";
	while(true){
	    clear();
	    System.out.println("What is the number of the team?");
	    if(s.hasNext()){
		team = (s.nextLine());
	    }   
	    Sheet current = new Sheet(team);
	    if(current == null){
		System.out.println("Please re-specify a team");
	    }
	    else{
		clear();
		System.out.println(current);
		stall();
		break;
	    }
	}
    }

    //----------------------END MENU METHODS-----------------------

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

	startUp();
	while(true){
	    menu();
	}

    }

}