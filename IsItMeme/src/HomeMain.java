import java.util.Scanner;


public class HomeMain {
	
	//Our application name
    private static final String appName = "iz it meme?!?";
    
    
	public static void main(String[] args) {
		
		//Print the welcome
        System.out.println("wellcome 2 " + appName + "!");
        System.out.println();
        
        //Print asking for user input
        System.out.println("pls type ur meme beelow...");
        System.out.println();
        
        //Get the meme text
        Scanner scan = new Scanner(System.in);
        String memeInput = scan.nextLine();
        scan.close();
        
        //Create our Sentence detector object
        SentenceDetect sDetect = new SentenceDetect();
        
        //Check meme
        if(sDetect.isSentence(memeInput))  System.out.println("is sentnce");
        else System.out.println("is no sentnce");
        
        
        System.out.println("haz " + sDetect.numSentences(memeInput) + " sentezncez");
        
	}
	
	//Function to exit the app
    public static void exitApp() {

        //Simply print spacing and exit
        System.out.println();
        System.exit(0);
    }

}
