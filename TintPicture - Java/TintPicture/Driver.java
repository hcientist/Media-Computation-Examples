
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
public class Driver
{
    //~ Instance/static variables .............................................



    //~ Constructor ...........................................................

    // ----------------------------------------------------------
    /**
     * Creates a new Driver object.
     */
    public static void main (String [] cheese)
    {
        TintablePicture myPic = new TintablePicture(FileChooser.pickAFile());
        myPic.tintPictureConditionally(ColorChooser.pickAColor(), ColorChooser.pickAColor(), 75);
    }


    //~ Methods ...............................................................

}
