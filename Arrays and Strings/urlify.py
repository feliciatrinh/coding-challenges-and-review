import re
def urlify (str): 
  //get rid of trailing whitespaces using regex
  str = re.sub("\s+$", "", str)
  //replace single whitespace with "%20"
  str = re.sub("\s", "%20", str)
  return str
