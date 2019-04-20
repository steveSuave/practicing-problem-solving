/*
There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

The function has two input variables:

    customers: an array (list in python) of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
    n: a positive integer, the number of checkout tills.

The function should return an integer, the total time required.
*/


import java.util.Arrays;
public class Solution {

    public static int solveSuperMarketQueue(int[] customers, int n) {
      int[] ret= new int[n];
      for (int i=0;i<customers.length;i++){
        ret[0]+=customers[i];
        Arrays.sort(ret);
      }
      return ret[ret.length-1];
    }    
}
