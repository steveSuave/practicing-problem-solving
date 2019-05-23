/*
Given a string, return the longest substring 
that appears at both the beginning and end 
of the string without overlapping. 
For example, sameEnds("abXab") is "ab".

sameEnds("abXYab") → "ab"
sameEnds("xx") → "x"
sameEnds("xxx") → "x"
*/


public String sameEnds(String string) {
  int len = string.length();
  String ret="";
  for (int i=1; i<len; i++){
    String head = string.substring(0,i);
    String tail = string.substring(len-i, len);
    if (head.equals(tail) && head.length()+tail.length()<=len) {
      ret=string.substring(0,i);
    }
  }
  return ret;
}

