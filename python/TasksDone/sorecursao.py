string = 'marcelo'
vetor = 0
p = ''
def substring (s, vetor, p):
  if vetor < (len(s)):
    p += s[vetor]
    print (p)
    substring (s, vetor+1, p)
  elif (len(s)) > 1:  
    substring (s[1:], 0, '')

substring(string, vetor, p)


  

    


