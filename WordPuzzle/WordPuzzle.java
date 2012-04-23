import student.*;
import java.util.ArrayList;
import java.util.Random;
// -------------------------------------------------------------------------
/**
 *  Write a one-sentence summary of your class here.
 *  Follow it with additional details about its purpose, what abstraction
 *  it represents, and how to use it.
 * 
 *  @author  your-pid (and if in lab, partner's pid on same line)
 *  @version (place the date here, in this format: yyyy.mm.dd)
 */
public class WordPuzzle
{
    //~ Instance/static variables .............................................
    private String message;
    private ArrayList<ArrayList<ArrayList<Integer>>> puzzle;

    //~ Constructor ...........................................................

    // ----------------------------------------------------------
    /**
     * Creates a new WordPuzzle object.
     */
    public WordPuzzle()
    {
        //we don't need to do anything for an empty constructor.
    }

    public WordPuzzle(String message)
    {
        
    }
    
    public WordPuzzle(ArrayList<ArrayList<ArrayList<Integer>>> puzzle)
    {
        
    }
    
    public WordPuzzle(String message, ArrayList<ArrayList<ArrayList<Integer>>> puzzle)
    {
        
    }

    public WordPuzzle(ArrayList<ArrayList<ArrayList<Integer>>> puzzle, String message)
    {
        
    }
    
    public String getMessage()
    {
        
    }

    public void setMessage(String message)
    {
        
    }

    public ArrayList<ArrayList<ArrayList<Integer>>> getPuzzle()
    {
        
    }

    public void setPuzzle(ArrayList<ArrayList<ArrayList<Integer>>> puzzle)
    {
        
    }

    public void setFromMessage(String message)
    {
        
    }
    
    public void setFromPuzzle(ArrayList<ArrayList<ArrayList<Integer>>> puzzle)
    {
        
    }

    public static int ord(char chr)
    {
        return (int)chr;
    }
    
    public String messageFromPuzzle(ArrayList<ArrayList<ArrayList<Integer>>> puzzle)
    {
        //create an empty string to hold the letters of the message that you 
        //figure out
       
        
        //loop over all of the words in puzzle
        
            //make an ArrayList<ArrayList<Integer>> to represent the current word
            
            //if this is not the first time through this loop, add a space to message
            //before you add the new characters.
           
            //for each character in the current word
            
                //get the pair of numbers
                
                //add them 
                //convert them to a character using chr
                //add the character to your message
               
        //make sure you return the message
    }

    public ArrayList<ArrayList<ArrayList<Integer>>> puzzleFromMessage(String message)
    {
        //this create a random number generator, if you do 
        //r.nextInt(someNumber)
        //then it will give you an integers from 0-someNumber
        Random r = new Random();

        // this will be an array of Strings with each element being one of the
        //words from your message
        String[] words = message.split(" ");
        
        //create a new ArrayList<ArrayList<ArrayList<Integer>>> to hold your final result
        
        //create a ArrayList<ArrayList<Integer>> to hold the pairs that belong to the current word in the message
        
        //loop over all the words in words
            //set your ArrayList<ArrayList<Integer>> to a new ArrayList<ArrayList<Integer>>
            
            //declare a ArrayList<Integer> to hold the pair of integers for the current letter
            
            //loop over all the letters in the current word
            
                //set your ArrayList<Integer> to a new (empty) ArrayList<Integer>
                
                //calculate the 2 numbers that should be added for the current letter
                //(using r.genNextInt(someNumber))


                //add the first number to your ArrayList<Integer>


                //add the 2nd number to your ArrayList<Integer>

                //add your ArrayList<Integer> to your ArrayList<ArrayList<Integer>> 
            //add your ArrayList<ArrayList<Integer>> to your ArrayList<ArrayList<ArrayList<Integer>>>
        //don't forget to return your results
    }

    public static char chr(int chrVal)
    {
        char r = (char) chrVal;
        return r;
    }
    
    public String toString()
    {
        String prettyPrint = "";
        String topLine;
        String bottomLine;
        String underLine;
        for (ArrayList<ArrayList<Integer>> wordArray : this.puzzle)
        {
            topLine = "";
            bottomLine = "";
            underLine = "";
            for (ArrayList<Integer> pair : wordArray)
            {
                topLine += padLeft(pair.get(0).toString(), 4) + "  ";
                bottomLine += "+" + padLeft(pair.get(1).toString(), 3) + "  ";
                underLine += "----  ";
            }
            prettyPrint += topLine + "\n" + bottomLine + "\n" + underLine + "\n\n\n";
        }
        return prettyPrint;
    }
    
    public static String padLeft(String s, int n) 
    {
        return String.format("%1$#" + n + "s", s);   
    }


    public static void main(String[] args)
    {
        ArrayList<ArrayList<ArrayList<Integer>>> puzzle = new ArrayList<ArrayList<ArrayList<Integer>>>();
        ArrayList<ArrayList<Integer>>word = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer>pair = new ArrayList<Integer>();
        pair.add(61);
        pair.add(11);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(93);
        pair.add(4);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(73);
        pair.add(39);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(78);
        pair.add(34);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(17);
        pair.add(104);
        word.add(pair);
        puzzle.add(word);
        word = new ArrayList<ArrayList<Integer>>();
        pair = new ArrayList<Integer>();
        pair.add(23);
        pair.add(43);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(11);
        pair.add(93);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(65);
        pair.add(52);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(20);
        pair.add(96);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(66);
        pair.add(31);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(86);
        pair.add(24);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(40);
        pair.add(61);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(102);
        pair.add(13);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(50);
        pair.add(51);
        word.add(pair);
        puzzle.add(word);
        word = new ArrayList<ArrayList<Integer>>();
        pair = new ArrayList<Integer>();
        pair.add(73);
        pair.add(43);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(28);
        pair.add(73);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(8);
        pair.add(89);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(31);
        pair.add(68);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(77);
        pair.add(27);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(24);
        pair.add(77);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(42);
        pair.add(72);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(15);
        pair.add(24);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(64);
        pair.add(51);
        word.add(pair);
        puzzle.add(word);
        word = new ArrayList<ArrayList<Integer>>();
        pair = new ArrayList<Integer>();
        pair.add(25);
        pair.add(75);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(7);
        pair.add(90);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(10);
        pair.add(111);
        word.add(pair);
        pair = new ArrayList<Integer>();
        pair.add(17);
        pair.add(16);
        word.add(pair);
        puzzle.add(word);
        WordPuzzle wp = new WordPuzzle();
        
        WordPuzzle wp2 = new WordPuzzle(puzzle);
        System.out.println(wp2);
        System.out.println(wp.messageFromPuzzle(puzzle));

    }
}
