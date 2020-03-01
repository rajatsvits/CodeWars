Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"

#Best
import java.util.stream.*;
import java.util.Arrays;

public class SpinWords {

  public String spinWords(String sentence) {
    return Arrays.stream(sentence.split(" "))
                 .map(i -> i.length() > 4 ? new StringBuilder(i).reverse().toString() : i)
                 .collect(Collectors.joining(" "));
  }
}

#MIne
import java.util.*;
public class SpinWords {

  public String spinWords(String sentence) {
    //TODO: Code stuff here
    String[] array = sentence.split(" ");
        for (int i = 0; i <= array.length - 1; i++) {
            array[i] = array[i].length() >= 5 ? array[i] = new StringBuffer(array[i]).reverse().toString() : array[i];
        }
    
    String out=Arrays.toString(array);
    return out.substring(1, out.length() - 1).replaceAll(",", "");
  }
}
