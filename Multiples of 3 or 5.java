If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.

Courtesy of ProjectEuler.net



public class Solution {

  private static int getSum(int i) {
    return (i*(i+1))/2;
  }
  
  public int solution(int number) {
    number--;
    return 3*(getSum(number/3))+5*(getSum(number/5))-15*(getSum(number/15));
  }
}
