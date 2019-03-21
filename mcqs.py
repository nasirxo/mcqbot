from time import sleep
import sqlite3
import sys , os , time 

try:
   conn = sqlite3.connect('dic.db')
   c = conn.cursor()
   conn.commit()
   print "database found"
except:
   print "No database Found"

def search(w):
  c.execute("SELECT defn FROM words WHERE word = '{}'".format(str(w)))
  d = c.fetchall()
  return d[0][0]


#Colours
W  = '\033[1;37m' 
N  = '\033[0m'
R="\033[1;37m\033[31m" 
B  = '\033[1;37m\033[34m' 
G  = '\033[1;32m' 
Y = '\033[1;33;40m'

try:
  os.system("rm a")
  os.system("rm f")
  os.system("rm c")
  os.system("rm i")
  os.system("touch a")
  os.system("touch f")
  os.system("touch c")
  os.system("touch i")
except:
  pass
 
try:
 from fbchat import log, Client
 from fbchat.models import *
 from random import choice
 import requests as rqn
 import aiml
 print Y+" {}Requirement's Available{} \n".format(G,Y)
except:
  print "Installing Requirement's "
  os.system("pip2 install fbchat==1.5.0")
  os.system("pip2 install aiml")
  os.system("pip2 install requests")
  print G+"[~] Requirement's Installed Sucessfully [~]"
  from fbchat import log, Client
  from fbchat.models import *
  from random import choice
  import requests as rqn

class NBot(Client):
 #,"r").read().split("$")
 

 def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
    tim = str(time.ctime())
    welx = """
    Time : {}
    Welcome To TestBoT
    Question will be asked the answer should be a,b,c,d according to question options Correct answer should be given #+4 marks while on incorrect answer #-2 marks will be given\n\n#Type start to begin Test\n#Type Result at Last""".format(tim) 
    
    # dem = str(message_object.text)
    q = open("mcq.txt","r").read().split("$")
    qkey = {
     1:"d",
     2:"b",
     3:"a",
     4:"b",
     5:"a",
     6:"c",
     7:"b",
     8:"c",
     9:"b",
     10:"b",
     11:"0"
     }
    if author_id != self.uid:
      dy = str(message_object.text).lower()
      dx = dy.split()
    # dcyx = dem.split()
    #dlen = len(dx)
    clist = list("abcd")
    student = 1
    sid = str(author_id)
    wi = open(sid+"i","a")
    wc = open(sid+"c","a")
    wf = open(sid+"f","a")
    wm = open(sid+"m","a")
    st = open(sid+"sk","a")
    i = int(len(open(sid+"i","r").read()))
    c = int(len(open(sid+"c","r").read()))
    f = int(len(open(sid+"f","r").read()))
    stop = int(len(open(sid+"sk","r").read()))
    totali = int(c)+int(f)
    marks = int(len(open(sid+"c","r").read())*4) - int(len(open(sid+"f","r").read())*2)

    if i == 0 and author_id != self.uid and dx[0] != "search" and dy != "next":
          self.send(Message(text=welx), thread_id=thread_id, thread_type=thread_type)
          wi = open(sid+"i","a")
          wi.write("1")         
          wi.close()
          
    if author_id >= student and author_id != self.uid and i != 0 and totali != 10 and dx[0] != "search":
        
        if dy == str(qkey[i]) and dy in clist:
          wi.write("1")
          wi.close()
          wm.write("1")
          wm.close()
          print "CORRECT"
          wc.write("1")
          wc.close()
        if dy != str(qkey[i]) and dy in clist:
          wf.write("1")
          wf.close()
          print "INCORRECT"
          wi.write("1")
          wi.close()
        if dy not in clist and dy != "next" and dx[0] != "search" and dy != "start" and len(dy) < 1:   
          self.send(Message(text='Invalid-Choice !\n choose A B C D'), thread_id=thread_id, thread_type=thread_type)
        if dy in clist or dy =="start":
           #if i == 0:
           #  wi.write("1")       
           #  wi.close()
           i = int(len(open(sid+"i","r").read()))
           bmcq = '''{}'''.format(str(q[i]))
           log.info('{} Sending Reply {}'.format(author_id, thread_id))
           self.send(Message(text='[MCQ No #{}/10]\n{}'.format(i,bmcq)), thread_id=thread_id, thread_type=thread_type)

    
    if dx[0] == "search" and author_id != self.uid:
       qsearch = str(dx[1]).lower()
       sresult = search(qsearch)
       self.send(Message(text='Search Result : \n'+sresult), thread_id=thread_id, thread_type=thread_type)
    if int(totali) == int(len(q))-1 and int(stop) == 0:
       log.info('{} Sending Result {}'.format(author_id, thread_id))
       perc  = str(float(float(marks)/float(int(int(i)-1)*4))*100)+"%"
       mar = str(marks)+"/"+str(int(int(i)-1)*4)
       testi = '\n[ RESULT ]\n\nUser : {}\nMarks : {}\nPercentage : {}\nCorrect : {}\nIncorrect : {}\n\n'.format(author_id,mar,perc,c,f)
       self.send(Message(text=str(testi)), thread_id=thread_id, thread_type=thread_type)
       st.write("11")
       st.close()



banner = """ MCQ's Asking Bot \n Developer : Nasir Ali \n
Github: github.com/nasirxo \n Facebook : fb.com/nasir.xo"""


print banner 

email = raw_input("Email : ")
password = raw_input("Password : ")
client = NBot(email,password)
client.listen()               
 
 