/*
Given a string, compute recursively a new string w
here all the adjacent chars are now separated by a "*".

allStar("hello") → "h*e*l*l*o"
allStar("abc") → "a*b*c"
allStar("ab") → "a*b"
*/

public String allStar(String str) {
  int len = str.length();
  if (len<=1) return str;
  return str.charAt(0)+"*"+allStar(str.substring(1,len));
}
