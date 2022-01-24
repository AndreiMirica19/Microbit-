from microbit import *
import os
class Variables:
    name=""
    value=0
    def __init__(self,name,value):
        self.name=name
        self.value=value
varList=[]
def checkExist(s):
    for i in varList:
        if(s==i.name):
            return int (i.value)
    return "null"
def getIndex(s):
    for d,i in enumerate(varList):
        if(s==i.name):
            return d
b="true"
while(b=="true"):
   inp=input("cmd: ")
   s=inp.split(" ")
   if s[0]=="quit":
       b="false"
   elif s[0]=="exit":
         b="false"
   elif s[0]=="led":
       if s[1]=="on":
           if ((checkExist(s[2])!="null")and(checkExist(s[2])<=4)and(checkExist(s[3])!="null")and((checkExist(s[3])<=4))):
                display.set_pixel(checkExist(s[2]),checkExist(s[2]), 9)
           elif ((int(s[2])<=4)and(int(s[3])<=4)):
                display.set_pixel(int(s[2]),int (s[3]), 9)
          
           else:       
               print("Invalid LED.")
           
       else:
            if s[1]=="off":
                if ((checkExist(s[2])!="null")and(checkExist(s[2])<=4)and(checkExist(s[3])!="null")and((checkExist(s[3])<=4))):
                        display.set_pixel(checkExist(s[2]),checkExist(s[2]), 0)
                elif ((int(s[2])<=4)and(int(s[3])<=4)):
                    display.set_pixel(int(s[2]),int (s[3]), 0)
                else:
                    print("Invalid LED.")
            else:
                 if s[1]=="blink":
                      if ((checkExist(s[3])!="null")and(checkExist(s[3])<=20)and(checkExist(s[4])!="null")and((checkExist(s[4])<=4)and(checkExist(s[5])!="null")and(checkExist(s[5])<=4))):
                            display.set_pixel(checkExist(s[4]),checkExist(s[5]), 0)
                            
                            c=0
                            while(checkExist(s[3])>c):
                                display.set_pixel(checkExist(s[4]),checkExist(s[5]), 9)
                                sleep(checkExist(s[2]))
                                display.set_pixel(checkExist(s[4]),checkExist(s[5]), 0)
                                sleep(checkExist(s[2]))
                                c=c+1
                      elif ((int(s[3])<=20)and(int(s[4])<=4)and (int(s[5])<=4)):
                         c=0
                         while(int(s[3])>c):
                             display.set_pixel(int(s[4]),int (s[5]), 9)
                             sleep(int(s[2]))
                             display.set_pixel(int(s[4]),int (s[5]), 0)
                             sleep(int(s[2]))
                             c=c+1
                      else:
                           
                           if(int(s[3])>20):
                               print("Invalid count value.")
                           elif((checkExist(s[4])=="null")or(checkExist(s[4])>4)or(checkExist(s[5])=="null")or(checkExist(s[5])>4)):
                               print("Invalid LED.")
                               
                           
                 else:
                      if s[1]=="toggle":
                           if ((checkExist(s[2])!="null")and(checkExist(s[2])<=4)and(checkExist(s[3])!="null")and((checkExist(s[3])<=4))):
                                if display.get_pixel(checkExist(s[2]),checkExist(s[2]))==0:
                                   display.set_pixel(checkExist(s[2]),checkExist(s[2]), 9)
                                else:
                                    display.set_pixel(checkExist(s[2]),checkExist(s[2]), 0)
                           else:
                                if display.get_pixel(int(s[2]), int(s[3]))==0:
                                    display.set_pixel(int(s[2]),int (s[3]), 9)
                                else:
                                    display.set_pixel(int(s[2]),int (s[3]), 0)
                      else:
                           if ((s[1]=="brightness")and(len(s)>3)):
                               if ((s[2]=="set")and(checkExist(s[3])!="null")and(checkExist(s[3])<=9)):
                                    if((checkExist(s[4])!="null")and(checkExist(s[4])<=4)and (checkExist(s[5])!="null")and(checkExist(s[5])<=4)):
                                         
                                         display.set_pixel(checkExist(s[4]),checkExist(s[5]),checkExist(s[3]))  
                               elif ((s[2]=="set")and(int(s[3])<=9)):
                                    display.set_pixel(int(s[4]),int (s[5]), int(s[3]))
                                    print(int(display.get_pixel(int(s[4]), int(s[5]))))
                               else:
                                   if ((s[2]=="set")and(int(s[3])>9)):
                                       print("Invalid brightness.")
                                   else:
                                       if ((int(s[2])<=4)and(int(s[3])<=4)):
                                           print(int(display.get_pixel(int(s[2]), int(s[3]))))
                           else:
                                print("Invalid command.")
   elif s[0]=="button":
       if s[1]=="a":
            if button_a.is_pressed():
                print("True")
            else:
               print("False")
       elif s[1]=="b":
            if button_b.is_pressed():
                print("True")
            else:
               print("False")
       else:
           print("Invalid button.")
   elif s[0]=="light":
       print(display.read_light_level())
       
   elif s[0]=="temperature":
       if s[1]=="c":
           print (temperature())
       elif s[1]=="f":
           print (temperature()*1.8+32)
       elif s[1]=="k":
           print(temperature()+273.15)
       
   elif s[0]=="echo":
       if ((s[1]=="-n")and (s.count('>')==0)and(s.count('>>')==0)):
           for x, ss in enumerate(s):
               if((x>1) and(x<len(s)-1)):
                   print (ss,end=" ") 
               elif((x>1) and(x==len(s)-1)):
                   print (ss,end="") 
                   
       elif ((s[1]!="-n")and (s.count('>')==0)and(s.count('>>')==0)):
           v=""
           for x, ss in enumerate(s):
               if(x>0):
                   v=v+ss+" "
           print (v)
       elif( (s.count('>')==1)and(s.count('>>')==0)and (s[1]!="-n")):
             index=s.index('>')
             file=open(s[index+1],"w")
             v=""
             if(index==1):
                  file.write(v)
                  file.close()
             else:      
                    for x, ss in enumerate(s):
                        if((x>0)and(x<index-1)):
                            v=v+ss+" "
                        elif((x==index-1)and (ss!=" ")):
                            v=v+ss       
                    v=v+"\n"
                    file.write(v)
                    file.close()
       elif( (s.count('>')==1)and(s.count('>>')==0)and (s[1]=="-n")):
             index=s.index('>')
             file=open(s[index+1],"w")
             v=""
             if(index==2):
                  file.write(v)
                  file.close()
             else:     
                    for x, ss in enumerate(s):
                        if((x>1)and(x<index-1)):
                            v=v+ss+" "
                        elif((x==index-1)and (ss!=" ")):
                            v=v+ss          
                 
                    file.write(v)
                    file.close()        
       elif ((s.count('>')==0)and(s.count('>>')==1)and (s[1]!="-n")):
           index=s.index('>>')
           p=os.listdir()
           if p.count(s[index+1])==1:
                  file=open(s[index+1])
                  ss=file.read()
                  file.close()
                  file=open(s[index+1],'w')
                  for x, strin in enumerate(s):
                     if((x>0)and(x<index)):
                        ss=ss+strin+" "
                            
                  ss=ss+"\n"    
                  file.write(ss)
                  file.close()
       elif ((s.count('>')==0)and(s.count('>>')==1)and (s[1]=="-n")):
           index=s.index('>>')
           p=os.listdir()
           if p.count(s[index+1])==1:
                  file=open(s[index+1])
                  ss=file.read()
                  file=open(s[index+1],'w')
                  v=""
                  for x, strin in enumerate(s):
                     if((x>1)and(x<index-1)):
                        ss=ss+strin+" "
                     if x==index-1:
                         ss=ss+strin
                  file.write(ss)
                  file.close()
           else:
                print("Cannot append redirect")      
   elif s[0]=="cat":
        for x, strin in enumerate(s):
                     if x>0:
                        p=os.listdir()
                        if p.count(strin)==1:
                                    file=open(strin)
                                    h=file.read()
                                    if(h[len(h)-1]=="\n"):
                                        print(str(h[:len(h)-1]))
                                    else:
                                        print(h)
                                    file.close()
                        else:
                             print("Cannot print file.")
                        
   elif ((s[0]=="ls")and(len(s)==1)):
       p=os.listdir()
       for ss in p:
           if(ss[0]!='.'):
                print (ss)
   elif((len(s)<4)and(s[0]=="ls")):               
        if ((len(s)==2)and(s[0]=="ls")and(s[1]=="-a")or(s[1]=="--all")):
            p=os.listdir()
            for ss in p:
                print (ss)
            
        elif ((s[0]=="ls")and(len(s)==2)and (s[1]=="-l")or(s[1]=="--long")):
            p=os.listdir()
            for ss in p:
                if(ss[0]!='.'):
                    print (os.size(ss)," ",ss)    
        elif ((s[0]=="ls")and (len(s)==3)and ((s[1]=="-a")or(s[1]=="--all")and(s[2]=="-l")or(s[2]=="--long"))or((s[2]=="-a")or(s[2]=="--all")and(s[1]=="-l")or(s[1]=="--long"))):
            p=os.listdir()
            for ss in p:
                print (os.size(ss)," ",ss)
        elif  ((s[0]=="ls")and(len(s)==2)):
            print(s[1])
        else:
            print("176")
             
   elif ((s[0]=="mv")and (len(s)==3)):
        p=os.listdir()
        if p.count(s[1])==1:
             file=open(s[1])
             bkp=file.read()
             os.remove(s[1])
             file.close()
             files=open(s[2],"w")
             files.write(bkp)
             files.close()
        else:
             print("Cannot move file.")
   elif ((s[0]=="rm")and(s.count('-r')==0)and(s.count('--recursive')==0)and(s.count('-R')==0)):
       p=os.listdir()
       for x, strin in enumerate(s):
           if ((p.count(strin)==1)and(x>0)):
                 file=open(strin)
                 bkp=file.read()
                 if(bkp==""):
                     os.remove(strin)
                     file.close()
                 else:
                     print("Cannot remove file.File not empty.")
           else:
                print("Cannot remove file.") 
   
   elif ((s[0]=="rm")and(s.count('-r')!=0)or(s.count('--recursive')!=0)or(s.count('-R')!=0)):
        p=os.listdir()
        for x, strin in enumerate(s):
            if ((p.count(strin)==1)and(x>1)):
                 file=open(strin)
                 bkp=file.read()
                 os.remove(strin)
                 file.close()
            else:
                if x>1:
                     print("Cannot remove file.")
                     
   elif ((s[0]=="cp") and (len(s)==3)):
       p=os.listdir()
       if (p.count(s[1])==1):
           file=open(s[1])
           bkp=file.read()
           file.close()
           files=open(s[2],"w")
           files.write(bkp)
           files.close()
       else:
           print("Cannot copy file.")
           
   elif ((s[0]=="set")and(len(s)==3)):
       s[1]="$"+s[1]
       if(checkExist(s[1])=="null"):
            varList.append(Variables(s[1],s[2]))
       else:
           varList[getIndex(s[1])].value=s[2]
   else:
       print("Invalid command.")
       
           
           
