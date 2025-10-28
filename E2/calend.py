i=0
j=2
sett=["lunedì", "martedì","mercoledì","giovedì","venerdì","sabato","domenica"]
cal = {}
for i in range(32):
  if (j>6):
    j=0
  cal[i]=sett[j]
  j=j+1
for i in range(31):
  print(i+1)
  print(cal[i])
