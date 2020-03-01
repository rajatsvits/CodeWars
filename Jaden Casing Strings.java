aden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

Example:

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"


import java.util.Arrays;
import java.util.stream.Collectors;

public class JadenCase {

  public String toJadenCase(String phrase) {
      if (null == phrase || phrase.length() == 0) {
          return null;
      }

      return Arrays.stream(phrase.split(" "))
                   .map(i -> i.substring(0, 1).toUpperCase() + i.substring(1, i.length()))
                   .collect(Collectors.joining(" "));
  }

}


import java.util.Arrays;
public class JadenCase {

	public String toJadenCase(String phrase) {
		// TODO put your code below this comment
    if(phrase==null||phrase=="")
        return null;
        
    String a[] = phrase.split(" ");
    for(int i=0;i<a.length; i++){
      a[i]=a[i].substring(0,1).toUpperCase()+a[i].substring(1,a[i].length());
    }
    String b=Arrays.toString(a);
    return  b.substring(1, b.length()-1).replaceAll(",","").toString();
	}

}
