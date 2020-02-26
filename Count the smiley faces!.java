import java.util.*;

#Best
return (int)arr.stream().filter( x -> x.matches("[:;][-~]?[)D]")).count();   


#mine
public class SmileFaces {
  
  public static int countSmileys(List<String> arr) {
      // Just Smile :)
//       Pattern pattern = pattern.compile("[:;][-~]?[)D]");
//       Matcher m = pattern.matcher(arr);
//       Pattern.matches
//       return ;
    int num = 0;
    for (String i : arr) {
      if (i.length() == 2) {
        if ((i.charAt(0) == ':' || i.charAt(0) == ';')&&(i.charAt(1) == 'D' || i.charAt(1) == ')')) {
          num++;
        }
      }
      if (i.length() == 3) {
        if ((i.charAt(0) == ':' || i.charAt(0) == ';')&&(i.charAt(1) == '-' || i.charAt(1) == '~')&&(i.charAt(2) == 'D' || i.charAt(2) == ')')) {
          num++;
        }
      }
    }
    return num;
  }
}
