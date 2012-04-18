
import student.*;
import java.awt.Color;

// -------------------------------------------------------------------------
/**
 *  Write a one-sentence summary of your class here.
 *  Follow it with additional details about its purpose, what abstraction
 *  it represents, and how to use it.
 * 
 *  @author  your-pid (and if in lab, partner's pid on same line)
 *  @version (place the date here, in this format: yyyy.mm.dd)
 */
public class TintablePicture extends Picture
{
    //~ Instance/static variables .............................................



    //~ Constructor ...........................................................

    // ----------------------------------------------------------
    /**
     * Creates a new TintablePicture object.
     */
    public TintablePicture()
    {
        /*# Do any work to initialize your class here. */
        this.load(FileChooser.pickAFile());
    }
    
    public void tintPicture()
    {
        this.tintPicture(ColorChooser.pickAColor());
    }
    public void tintPicture(Color tintColor)
    {
        Pixel[] pixels = this.getPixels();
        for (int i = 0; i < pixels.length; i++)
        {
            this.tintPixel(pixels[i], tintColor);
        }
    }
    
    public void tintPixel(Pixel p, Color c)
    {
        double newRed = p.getRed()/2 + c.getRed()/2;
        double newGreen = p.getGreen()/2 + c.getGreen()/2;
        double newBlue = p.getBlue()/2 + c.getBlue()/2;
        //System.out.println(newRed + " " + newGreen + " " + newBlue);
        p.setColor(new Color((int)newRed, (int)newGreen, (int)newBlue));
    }
    
    public void tintPictureConditionally()
    {
        Color replacingColor = ColorChooser.pickAColor();
        Color replacedColor = ColorChooser.pickAColor();
        double diff = SimpleInput.getNumber("what difference in colors do you want to replace?");
        this.tintPictureConditionally(replacingColor, replacedColor, (int)diff);
    }
    public void tintPictureConditionally(Color replacingColor, Color replacedColor, int difference)
    {
        // we want to check the distance of the color of the current pixel to the replaced color
        // if it's smaller than difference then tint the pixel
        Pixel[] pixels = this.getPixels();
        for (int i = 0; i < pixels.length; i++)
        {
            double d = this.distance(pixels[i].getColor(), replacedColor);
            if (d <= difference)
            {
                this.tintPixel(pixels[i], replacingColor);
            }
        }
        this.repaint();
    }

    //~ Methods ...............................................................
    public double distance(Color c1, Color c2)
    {
        double red = Math.pow(c1.getRed()-c2.getRed(),2);
        double green = Math.pow(c1.getGreen()-c2.getGreen(),2);
        double blue = Math.pow(c1.getBlue()-c2.getBlue(),2);
        double radicand = red + green + blue;
        
        return Math.sqrt(radicand);
    }

}
