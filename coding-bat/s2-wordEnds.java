/*
Given a string and a non-empty word string, return a string made of 
each char just before and just after every appearance of the word 
in the string. Ignore cases where there is no char before or after 
the word, and a char may be included twice if it is between two words.

wordEnds("abcXY123XYijk", "XY") → "c13i"
wordEnds("XY123XY", "XY") → "13"
wordEnds("XY1XY", "XY") → "11"
*/


public String wordEnds(String str, String word) {
  
  String ret = ""; 
  int strlen=str.length();
  int wordlen=word.length();
  if (strlen<wordlen || ((strlen==wordlen) && !str.equals(word))) return "";
  if (str.substring(0,wordlen).equals(word) && strlen>wordlen){
    ret+=str.charAt(wordlen);
  }
  for (int i=1; i<strlen-wordlen; i++){
    if (str.substring(i,i+wordlen).equals(word)){
      ret+=str.charAt(i-1);  
      if (i+wordlen>=strlen){
        break;
      }else{
        ret+=str.charAt(i+wordlen);
      }
    }
  }
  if (str.lastIndexOf(word) == strlen-wordlen && str.lastIndexOf(word)>0){
    ret+=str.charAt(strlen-wordlen-1);
  }
  return ret;
}
