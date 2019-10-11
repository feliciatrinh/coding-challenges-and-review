import re

def urlify (str): 
  # get rid of trailing whitespaces using regex
  str = re.sub(r"\s+$", "", str)
  # replace single whitespace with "%20"
  str = re.sub(r"\s", "%20", str)
  return str
