import time
import datetime

def sptor():
 # formatting
 print('------------------------')



def prlst(lst):
 # prints a list in reverse order
 sptor()
 l=len(lst)
 for i in range(l,0,-1):
  print(lst[i-1])



def niy():
 # placeholder
 sptor()
 print("This feature has not been implemented yet.")



def npt ():
 # input expense, date, description

 f=open ('ledger.txt','a')
 am=0

 while (am>=0):
  sptor()
  am=eval (input ("Amount (int): "))
  if am<=0: break
  dt=input ("Date  (mmdd): ")
  if dt=='':
   dt=str(datetime.datetime.now().month * 100 + datetime.datetime.now().day)
  dt=eval(dt)
  if dt<=0: break
  print("\n0: bar\n1: food\n2: pr\n3: booze\n4: exfood\n5: transport\n6: wkfood\n7: home\n8: hardware")
  ds=input ("Description: ")
  if ds=='0': ds='bar'
  elif ds=='1': ds='food'
  elif ds=='2': ds='pr'
  elif ds=='3': ds='booze'
  elif ds=='4': ds='exfood'
  elif ds=='5': ds='transport'
  elif ds=='6' or ds=='y': ds='wkfood'
  elif ds=='7' or ds=='u': ds='home'
  elif ds=='8' or ds=='i': ds='hardware'
  f.write (str(am) + '; ' + str(dt) + '; ' + str(ds) + ';\n')
  
 f.flush() 
 f.close ()



def pctg(lst):
 # adds percentage to list
 
 l=len(lst)
 j=0
 for i in range(0,l):
  j+=lst[i][1]
 for i in range(0,l): 
  lst[i].append(round(100*lst[i][1]/j,1))
 return(lst)



def rdr(lst):
 # list reordering

 for i in range(len(lst)-1):
  for j in range(i+1,len(lst)):
   if lst[i][1]<lst[j][1]:
    t=lst[i]
    lst[i]=lst[j]
    lst[j]=t
 return(lst)



def tt(lst):
 # sums list by description, reorders, and adds percentages

 i=0
 while i <= len(lst):
  j=len(lst)
  while j>(i+1):
   j-=1
   if ((lst[i][0].split(','))[0]).strip() == ((lst[j][0].split(','))[0]).strip():
    lst[i][1] += lst[j][1]
    del(lst[j])
  i+=1
 return(pctg(rdr(lst)))



def ldlst(r,o):
 # loads list from disk

 lst=[]
 f=open('ledger.txt','r')
 r=eval(r)
 o=eval(o)
 
 for ntry in f:
  a=ntry.split(';')
  if len(a)>2:
   if eval(a[1])>=r and eval(a[1])<=o:
    b=eval(a[0])
    c=a[2]
    lst.append([c,b])
 
 f.close()
 return(lst)



def ytt ():
 # year description in decreasing order

 sptor()
 lst=ldlst('0','9999')
 lst=tt(lst)
 prlst(lst)

 t=0
 for i in range (0,len(lst)):
  t+=lst[i][1]
 print('Total: ',t)



def dtt():
 # custom date range description in decreasing order

 sptor()
 print('Dates in MDD format')
 r=input('From date: ')
 if r=='':
  r=str((datetime.datetime.now().month-1)*100+datetime.datetime.now().day)
 o=input('To date: ')
 if o=='':
  o='9999'
 print('From ', r, ' to ', o)
 lst=ldlst(r,o)
 lst=(tt(lst))
 prlst(lst)
 t=0
 for i in range (0,len(lst)):
  t+=lst[i][1]
 print('Total: ',t)



def srccat():
 # search by category and by date

 sptor()
 a=input("Looking for item: ")
 r=input("From date: ")
 if r=='':
  r='0'
 o=input("To date: ")
 if o=='':
  o='9999'
 lst=pctg(ldlst(r,o))

 t=0
 p=0
 sptor()
 for i in range(len(lst)):
  if a in lst[i][0]:
   t+=lst[i][1]
   p+=lst[i][2]

 sptor()
 print(a+" amounts to: "+str(t)+", "+str(round(p,1))+"%")
 print("form "+r+' to '+o)



def srcstr():
 # search by string and by date

 sptor()
 a=input("Looking for string: ")
 r=input("From date: ")
 if r=='':
  r='0'
 o=input("To date: ")
 if o=='':
  o='9999'
 lst=pctg(ldlst(r,o))

 t=0
 p=0
 for i in range(len(lst)):
  if a in lst[i][0]:
   t+=lst[i][1]
   p+=lst[i][2]

 sptor()
 print(a+" amounts to: "+str(t)+", "+str(round(p,1))+"%")
 print("form "+r+' to '+o)



# main 
choice=1
while (eval(str(choice))>=0):
 sptor()
 print(time.asctime(time.localtime(time.time())))
 sptor()
 print ('0 quit')
 print ('1 new entry')
 print ('2 top ten by date')
 print ('3 yearly top ten')
 print ('4 search by category')
 print ('5 search by string')
 choice = input("\nYour choice: ")

 if choice=='0' or choice=='p': exit()
 if choice=='1' or choice=='q': npt()
 if choice=='2' or choice=='w': dtt()
 if choice=='3' or choice=='e': ytt()
 if choice=='4' or choice=='r': srccat()
 if choice=='5' or choice=='y': srcstr()
 choice=1 
