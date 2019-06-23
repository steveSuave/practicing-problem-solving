/*
Given a string, return a string where every appearance of the lowercase word "is" has been replaced with "is not". The word "is" should not be immediately preceeded or followed by a letter -- so for example the "is" in "this" does not count. (Note: Character.isLetter(char) tests if a char is a letter.)

notReplace("is test") → "is not test"
notReplace("is-is") → "is not-is not"
notReplace("This is right") → "This is not right"
*/

public String notReplace(String str) {
  
  if (str.length()==0) return str;
  
  str = str.replaceAll(" is ", " is not "); 
  str = str.replaceAll("^is ","is not "); 
  str = str.replaceAll(" is$", " is not");
  str = str.replaceAll("^is$","is not");
  
  String ret = str;
  for (int i=0; i<str.length()-2;i++){
    if (str.substring(i,i+2).equals("is") &&
        !Character.isLetter(str.charAt(i+2)) &&
         str.charAt(i+2)!=' '){ 
      ret=str.substring(0,i+2)+" not"+str.substring(i+2);
    }   
  }
  
  int len=ret.length();
  if (!Character.isLetter(ret.charAt(len-3)) &&
      ret.charAt(len-3)!=' ' &&
      ret.substring(len-2).equals("is")){
  	ret=ret+" not";
  }
	  
  return ret;
}
