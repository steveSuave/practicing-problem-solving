/*
Given a string, does "xyz" appear in the middle of the string? 
To define middle, we'll say that the number of chars to the 
left and right of the "xyz" must differ by at most one. 
This problem is harder than it looks.

xyzMiddle("AAxyzBB") → true
xyzMiddle("AxyzBB") → true
xyzMiddle("AxyzBBB") → false
*/

public boolean xyzMiddle(String str) {
  
  int len = str.length();
  if (len<3) return false;  
  if (len<=4 && str.contains("xyz")) return true;
  
  int mid=len/2;
  char med = str.charAt(mid);
  
  if (len%2==0){
    if (med=='x'|| med=='y' || med=='z')
      return true;
  }else{
    return str.substring(mid-1,mid+2).equals("xyz");
  }
  return false;
}
