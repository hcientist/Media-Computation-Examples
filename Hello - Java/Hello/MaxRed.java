
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
public class MaxRed
{
    //~ Methods ...............................................................
    public static void main (String[] args)
    {
        Picture p = new Picture(FileChooser.pickAFile());
        p.show();
        Pixel[] pixels = p.getPixels();
        for (int i = 0; i < pixels.length; i++)
        {
            pixels[i].setRed(255);
        }
        p.repaint();
    }

}
