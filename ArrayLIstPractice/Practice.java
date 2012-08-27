import java.util.ArrayList;
import student.*;

// -------------------------------------------------------------------------
/**
 *  Write a one-sentence summary of your class here.
 *  Follow it with additional details about its purpose, what abstraction
 *  it represents, and how to use it.
 * 
 *  @author  your-pid (and if in lab, partner's pid on same line)
 *  @version (place the date here, in this format: yyyy.mm.dd)
 */
public class Practice
{
    //~ Instance/static variables .............................................



    //~ Constructor ...........................................................

    // ----------------------------------------------------------
    /**
     * Creates a new Practice object.
     */
    public Practice()
    {
        /*# Do any work to initialize your class here. */
    }


    //~ Methods ...............................................................
    public static void main(String[] args)
    {
        String message = "";
        ArrayList<String> listOfWords = new ArrayList<String>();
        listOfWords.add("hello");
        listOfWords.add("world");
        //System.out.println(listOfWords);
        //System.out.println(listOfWords.size());
        ArrayList<Integer> listOfNumbers = new ArrayList<Integer>();
        listOfNumbers.add(3);
        listOfNumbers.add(97);
        for (Integer num : listOfNumbers)
        {
            System.out.println(num);
        }
//         System.out.println(listOfNumbers.get(0));
        //System.out.println(listOfNumbers);
        ArrayList<ArrayList<Integer>> wordList = new ArrayList<ArrayList<Integer>>();
        wordList.add(listOfNumbers);
//         System.out.println(wordList);
        
        ArrayList<ArrayList<ArrayList<Integer>>> puzzle = new ArrayList<ArrayList<ArrayList<Integer>>>();
        puzzle.add(wordList);
//         System.out.println(puzzle);
    }
    
    
}
