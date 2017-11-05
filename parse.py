import re
from test import classify
st = open('program.txt', 'r')
s = st.read()
st.close() 
m = []
conditions = []
statements = []
keywords = []
subst = " "
regex = r"(\s)+"
s = re.sub(regex, subst, s, 0)

l = re.findall(r'if\s?\(([^\)]+)\)\s?{([^}]*)}?', s, re.I)
for x in l:
  d = []
  for y in x:
    subst = " "
    regex = r"(\s)+"
    result = re.sub(regex, subst, y, 0)
    d.append(result)

  k = len(d)
  i = 0;
  while i<k:
    if d[i] == ' ' or d[i] == "":
      del d[i]
      k-=1
    i+=1
  for u in d:
      if u == '':
          d.remove('')
  m.append(d)
for x in m:

  if len(x) == 2:
      statements.append(x[1])
      conditions.append(x[0])
  elif len(x) == 1:
      statements.append(x[1])
  else:
      continue

for n in conditions:
  keywrd = n.split(" ")
  keywords.append(keywrd[0])


# print statements
# print conditions
# print keywords

operators = [('>','is greater than'), ('<','is lesser than'), ('>=','is greater than or equal to'), ('<=','is lesser than or equal to'), ('==','is equal to'),('&&','and'),('=','equals'),('*','of'),('-','minus'),('+','plus'),(';','\n')]
count = 1
for i in range(0,len(keywords)):
  x = classify(keywords[i])
  if x:
    condition = conditions[i].split(" ")
    for k in range(0,len(operators)):
      for j in range(0,len(condition)):
        if condition[j] == operators[k][0]:
          condition[j] = operators[k][1]
    condi = " ".join(condition)
    
    statement = statements[i].split(" ")

    for k in range(0,len(operators)):
      for j in range(0,len(statement)):
        if statement[j]== operators[k][0]:
          statement[j] = operators[k][1]
    stati = " ".join(statement)
    print str(count) + ". If " + condi + " then" + stati
    count = count + 1
#niche wale ko uncomment kar dena(triple quotes hata de) file mein conditions aur statements likhne ke liye
"""thefile = open('statement.txt', 'w')
for item in statements:
  thefile.write("%s\n" % item)  
thefile.close()
thefiles = open('condition.txt', 'w')
for item in conditions:
  thefiles.write("%s\n" % item)  
thefiles.close()
"""