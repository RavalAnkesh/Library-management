import re
regex = r"(\d+)"

match = re.search(regex, "I was born on 12 June")
if match != None:
    print ("Match at index %s, %s" % (match.start(), match.end()))
    print ("Full match: %s" % (match.group(0)))
    print ("Month: %s" % (match.group(1)))
    
  

else:
    print ("The regex pattern does not match.")