string = 'marcelo'
def substring (s):
  p = ''
  for x in range (len(s)):
    p += s[x]
    print (p)
  if (len(s)) > 1:
    substring(s[1:])  
    
substring(string)
