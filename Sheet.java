import java.io.*; //IOException
import java.util.*; //ArrayList, List

public class Sheet{

    private List<List<String>> _sheet;

    public Sheet(String teamNum){
	_sheet = ReadCSV.read(teamNum + ".txt");	    
    }

    public String toString(){
	String info = "";
	for(int i = 0; i < _sheet.size(); i++){
	    for(int j = 0; j < _sheet.get(i).size(); j++){
		if(j == _sheet.get(i).size() - 1){
		    info += _sheet.get(i).get(j) + "\n";
		}
		else{
		    info += _sheet.get(i).get(j) + " ";
		}
	    }
	}
	return info;
    }

}