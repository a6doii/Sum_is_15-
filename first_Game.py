import math                       #This game was devolped by :Al-Hussain Abdo
import random                     #In 31 of December 2022
import time                       #Al-Hussain Abdo a student in FCAI 2022-2026
import os                         #version 1.0
import optparse                   #All CopyRight back to The devolper Al-Hussain Abdo 
num = [1,2,3,4,5,6,7,8,9]
p9= [5,1] or [4,2]
p8= [5,2] or [6,1] or [4,3]
p7= [5,3] or [6,2]
p6= [5,4] or [7,2] or [8,1]
p5= [6,4] or [7,3] or [8,2] or [9,1]
p4= [6,5] or [8,3] or [9,2]
p3= [7,5] or [8,4] 
p2= [7,6] or [8,5] or [9,4]
p1= [9,5] or [6,8]
t14=("                           ^^^^^^^^^                          ")
t13=("                       ^^^^^^^^^^^^^/^^^                      ")
t12=("                      ^^^^^\ ^^^^^^/(9)^^^                    ")
t11=("                       ^^(8)\  || /^^^^^^^^^                  ")
t10=("                   ^^^ ^^    \ ||  (7) ^^^^                   ")
t9 =("                ^^^^ (6)\ ^^  \|| / ^^    ^^^^                ")
t8 =("                ^^^^^^   \---\-|| /-----/(5) ^^^^^^           ")
t7 =("                ^^ ^^^^(4)     ||/ ^^^    ^^^ ^^^^^           ")
t6 =("               ^^^ (3)\   \^^^ ||  ^^^^  ^^^   ^^^^ .         ")
t5 =("               ^^^^^^^ \---\---||-------/----(2)^^^           ")
t4 =("                  (1)\         ||                             ")
t3 =("                      \--------||                             ")
t2 =("                               ||                             ")
t1 =("                 _____||_____               ")
t0 =("              ______________          ")
ptotal=[p9,p8,p7,p6,p5,p4,p3,p2,p1]
tree = [t0,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14]
devil= [1,2,3,4,5,6,7,8,9]
player1=str(input("name of player -1:>>  "))
computer = "AI Player "
tree.reverse()
for i in range(15):
    print(tree[i])
print(player1,"your chance :||")
f1 =int(input("pick a number from the above tree,\n"))
if f1 in num:
    num.remove(num[f1-1])
else:
    while f1 not in num:
      print ("please pick from the numbers on the tree",num)
      f1 =int(input("pick a number from the above tree,\n"))
if (4<f1<10) and (f1 != 7):
    f2=devil[0]
    devil.remove(devil[0])
elif (3<f1<10) :
    f2=devil[1]
    devil.remove(devil[1])
elif (3<f1<9) and (f1!=6):
    f2=devil[2]
    devil.remove(devil[2])
elif (1<f1<10) and (4!=f1!=7):
    f2=devil[3]
    devil.remove(devil[3])
elif (0 < f1 < 10) and (f1 != 5) :
    f2=devil[4]
    devil.remove(devil[4])
elif (0<f1<9) and (3!=f1!=6):
    f2=devil[5]
    devil.remove(devil[5])
elif (1<f1<7) and (f1!=4):
    f2=devil[6]
    devil.remove(devil[6])
elif (0<f1<7):
    f2=devil[7]
    devil.remove(devil[7])
elif (0<f1<6) and (f1!=3):
    f2=devil[8]
    devil.remove(devil[8])
else:
    print("Erorr!!")
print (player1,"                                     ",f1)
print ("                                  ---------------------------------")
for i in range(15):
    print(tree[i])
print(computer,"Thinking....")
print("     ")
time.sleep(3)
print (player1,"                                     ",f1)
print ("                                  ---------------------------------")
print (computer,"                                 ",f2)
for i in range(15):
    print(tree[i])
s1 =int(input("pick a number from the above tree,\n"))
if s1 in num and s1!=f2:
    num.remove(num[s1-1])
else:
    while (s1 not in num) or (s1 not in devil):
      print ("please pick from the numbers on the tree",num)
      s1 =int(input("pick a number from the above tree,\n"))
s2=15-(f1+s1)
devil.remove(s2)
print (player1, "                                     ",f1,"   " ,s1 )
print ("                                  ---------------------------------")
print (computer,"                                 ",f2)
for i in range(15):
    print(tree[i])
print(computer,"Thinking....")
print("     ")
time.sleep(3)
print (player1, "                                     ",f1,"   ",s1 )
print ("                                  ---------------------------------")
print (computer,"                                 ",f2,"   ",s2 )
for i in range(15):
    print(tree[i])
th1 =int(input("pick a number from the above tree,\n"))
if th1 in num and th1!=s2:
    th1=th1
else:
    while (th1 not in num) or (th1 not in devil):
      print ("please pick from the numbers on the tree",num)
      th1 =int(input("pick a number from the above tree,\n"))
th2=15-(f2+s2)
if th2 >=10 and th2!=s2 :
    while th2 not in devil or th2==s2:
     th2=random.choice(num)
else:
    th2=th2
print ("                                     ",f1,"   ",s1,"   ",th1)
print("                                  ---------------------------------")
print ("                                     ",f2,"   ",s2 ) 
for i in range(15):
    print(tree[i])
print(computer,"Thinking....")
print("     ")
time.sleep(3)
print ("")
print ("")
print ("")
print ("                                           -------------------")
print (player1,"                                   |",f1," |  ",s1," |  ",th1,"|")
print ("                                           -------------------")
print (computer,"                                  |",f2," |  ",s2," |  ",th2,"|")
print ("                                           -------------------")
if f1+s1+th1 == 15:
  print("")
  print("")
  print("")
  w1=("                                             ")
  w2=("                                             ")
  w3=("                  ",player1,"                ")
  w4=("                    win!!!!!                 ")
  w5=("                                             ")
  w6=("                                             ")
  ws=[w1,w2,w3,w4,w5,w6]
  for i in range(6):
    print(ws[i])     
  time.sleep(5)
elif f2+s2+th2 == 15:
    w1=("                                                    ")
    w2=("                                                    ")
    w3=("                    ",computer,"                    ")
    w4=("                      win!!!!!                      ")
    w5=("                                                    ")
    w6=("                                                    ")
    ws=[w1,w2,w3,w4,w5,w6]
    for i in range(6):
      print(ws[i])     
    time.sleep(5)
    
else:
    w1=("                                                   ")
    w2=("                                                   ")
    w3=("                  ",computer,"                     ")
    w4=("                       &                           ")
    w5=("                  ",player1,"                      ")
    w6=("                                                   ")
    ws=[w1,w2,w3,w4,w5,w6]
    for i in range(6):
      print(ws[i])     
    time.sleep(5)
