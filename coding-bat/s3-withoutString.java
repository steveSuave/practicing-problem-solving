/*
Given two strings, base and remove, return a version of the base string 
where all instances of the remove string have been removed (not case sensitive). 
You may assume that the remove string is length 1 or more. 
Remove only non-overlapping instances, so with "xxx" removing "xx" leaves "x".

withoutString("Hello there", "llo") → "He there"
withoutString("Hello there", "e") → "Hllo thr"
withoutString("Hello there", "x") → "Hello there"
*/

public String withoutString(String base, String remove) {

  String ret="";
  String smallRes = base.toLowerCase().replace(remove.toLowerCase(),"");
  String tempBase = base.toLowerCase();
  int j=0;
  for (int i=0; i<smallRes.length(); i++){
    while (tempBase.charAt(j) != smallRes.charAt(i)){
      j++;
      if ( j >= tempBase.length()) break;
    }
    if ( j < tempBase.length()){
      ret+=base.charAt(j);
    }
  }
  return ret;
  
}