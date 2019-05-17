/*
Given a string and a non-empty word string, return a version of the 
original String where all chars have been replaced by pluses ("+"), 
except for appearances of the word string which are preserved unchanged.

plusOut("12xy34", "xy") → "++xy++"
plusOut("12xy34", "1") → "1+++++"
plusOut("12xy34xyabcxy", "xy") → "++xy++xy+++xy"
*/

public String plusOut(String str, String word) {

  String sb = "";
  int lenstr=str.length();
  int lenwrd=word.length();
  for (int i=0;i<lenstr-lenwrd+1; i++){
    if (str.substring(i,i+lenwrd).equals(word)){
      sb+=word;
      i+=lenwrd-1;
    }else{
      sb+="+";
    }
  }
  int rest = str.length()-sb.length();
  for (int i=0; i<rest; i++){
    sb+="+";
  }
  return sb;
}