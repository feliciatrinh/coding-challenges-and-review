/*
Input: array of positive and neg numbers
Output: maximum product of three numbers

Runtime: O(n)

The maximum is either the product of the 3 highest numbers or
the product of the highest number multiplied by the product of the two most negative numbers
*/

import java.util.*;

public class ClassNameHere {
   public static void main(String[] args) {
      List<Integer> arr = new ArrayList<Integer>();
      arr.add(-100);
      arr.add(-200);
      arr.add(0);
      arr.add(1);
      arr.add(2);
      int max1 = Integer.MIN_VALUE;
      int max2 = Integer.MIN_VALUE;
      int max3 = Integer.MIN_VALUE;
      int min1 = Integer.MAX_VALUE;
      int min2 = Integer.MAX_VALUE;
  
      for (int i = 0; i < arr.size(); i++) {
          // update all 3 maximums
          if (arr.get(i) > max1) {
              max3 = max2;
              max2 = max1;
              max1 = arr.get(i);
          } else if (arr.get(i) > max2) { // update second, third maximums
              max3 = max2;
              max2 = arr.get(i);
          } else if (arr.get(i) > max3) {
              max3 = arr.get(i);
          }
          if (arr.get(i) < min1) {
              min2 = min1;
              min1 = arr.get(i);
          } else if (arr.get(i) < min2) {
              min2 = arr.get(i);
          }
      }
      System.out.println(Math.max(max1 * max2 * max3, max1 * min1 * min2));
   }
}
	