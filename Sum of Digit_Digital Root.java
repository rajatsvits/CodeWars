In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

Here's how it works:

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6


public class DRoot {
  public static int digital_root(int n) {
    return (n != 0 && n%9 == 0) ? 9 : n % 9;
  }
}




public class DRoot {
  public static int digital_root(int n) {
    // ...
    while(n>9){
      int x=n,y=0;
      while(x>0){
        y+=x%10;
        x/=10;
      }
      n=y;
    }
    return n;
    }
  
}
