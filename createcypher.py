import re
import sys

# For countries and products
'''dicty = {"cname":"Country", "pname":"Product", "cid":"Sales"}
file = "C:\\Users\\Martin\\Desktop\\odb\\product.csv"
outputF = "C:\\Users\\Martin\\Desktop\\odb\\product.cypher"
e = open(file, "r", encoding='utf-8')
f = (e.read()).split("\n")
e.close()
headers = f[0].split(",")
data = f[1:]

countries = {}

for x in range(len(data)):
   data[x] = data[x].split(",")

for d in range(len(data)):
   for x in range(len(data[d])):
      if data[d][x] == "":
         data[d][x] = " "
      else:
         data[d][x] = re.sub(r'\s+', '', data[d][x])
         # data[d][x] = re.sub('[^A-ZÆØÅa-zæøå]+', '', data[d][x]) #countries
         data[d][x] = re.sub('[^A-ZÆØÅa-zæøå0-9]+', '', data[d][x]) #products (numbers for pid)

del data[-1]

for f in range(len(headers)):
   headers[f] = re.sub(r'\s+', '', headers[f])
print(headers)

ee = open(outputF, "w")
for d in data[0:]:
   stringy = ("CREATE ({}:{}".format(d[1], dicty[headers[1]]) + "{" + "{} :'{}', {}: '{}'".format(headers[1], d[1], headers[0], d[0]) + "}) \n")
   ee.write(stringy)
ee.close()'''

cfile = "C:\\Users\\Martin\\Desktop\\odb\\country.csv"
file = "C:\\Users\\Martin\\Desktop\\odb\\sales.csv"
outputF = "C:\\Users\\Martin\\Desktop\\odb\\sales.cypher"

ce = open(cfile, "r", encoding='utf-8')
e = open(file, "r", encoding='utf-8')
f = (e.read()).split("\n")
h = ce.read().split("\n")
e.close()
ce.close()
headers = f[0].split(",")
data = f[1:]
cdata = h[1:]
for y in range(len(cdata)):
   cdata[y] = cdata[y].split(",")

for x in range(len(data)):
   data[x] = data[x].split(",")

for d in range(len(data)):
   for x in range(len(data[d])):
      if data[d][x] == "":
         data[d][x] = " "
      else:
         data[d][x] = re.sub(r'\s+', '', data[d][x])

for d in range(len(cdata)):
   for x in range(len(cdata[d])):
      if cdata[d][x] == "":
         cdata[d][x] = " "
      else:
         cdata[d][x] = re.sub(r'\s+', '', cdata[d][x])
         cdata[d][x] = re.sub('[^A-ZÆØÅa-zæøå]+', '', cdata[d][x]) #countries
         # data[d][x] = re.sub('[^A-ZÆØÅa-zæøå0-9]+', '', data[d][x]) #products (numbers for pid)

for d in data: del d[-1]
del data[-1]
del cdata[-1]

for f in range(len(headers)):
   headers[f] = re.sub(r'\s+', '', headers[f])

countries = {}
for c in cdata:
   countries[str(c[0])] = str(c[1])
products = {'1':'Eksportavråolje', '2':'Eksportavnaturgass', '3':'Eksportavkondensater'}

outp = open(outputF, "w", encoding="utf-8")
outp.write("CREATE ")
for d in data:
   outp.write("({})-[:SALE".format(countries[d[1]]) + "{" + "month: {}, year: {}, amountMNOK: {}".format(d[2], d[3], d[4]) + "}" + "]->({}),".format(products[d[0]]) + "\n")
   # outp.write("CREATE ({})")
outp.close()