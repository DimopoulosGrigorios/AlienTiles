"""AlienTiles Problem"""

from search import *
import sys
import math
import time
class AlienTilesProblem(Problem) :
      """Subclass of search.Problem"""
      
      def __init__(self, n,start=None,goal=None) :
                        super(AlienTilesProblem, self).__init__(start, goal)
      def actions(self, state) :       
                        n=len(state)
                        act=tuple((i,j)for i in range(0,n) for j in range(0,n))
                        return act
      def result(self, state, action) :
                        x=action[0]
                        y=action[1]
                        n=len(state)
                        for i in range(0,n):
                              for  j in range(0,n):
                                    if i==x or y==j:
                                          if state[i][j]==2:
                                                state=list(state)
                                                state[i]=list(state[i])
                                                state[i][j]=3
                                                state[i]=tuple(state[i])
                                                state=tuple(state)
                                          elif state[i][j]==0:
                                                state=list(state)
                                                state[i]=list(state[i])
                                                state[i][j]=1
                                                state[i]=tuple(state[i])
                                                state=tuple(state)
                                          elif state[i][j]==1:
                                                state=list(state)
                                                state[i]=list(state[i])
                                                state[i][j]=2
                                                state[i]=tuple(state[i])
                                                state=tuple(state)
                                          else:
                                                state=list(state)
                                                state[i]=list(state[i])
                                                state[i][j]=0
                                                state[i]=tuple(state[i])
                                                state=tuple(state)
                        return state

 #---------------------------------------------------------------------------------------------------#           
def h1(t,goal): 
      state=t.state
      n=len(state)
      counter_r=0
      counter_p=0
      counter_g=0
      counter_b=0
      g=goal[0][0]
      for i in range(0,n):
            for j in range(0,n):
                  if state[i][j]==3:
                         counter_p+=1
                  elif state[i][j]==1:
                        counter_g+=1
                  elif state[i][j]==0:
                        counter_r+=1
                  else:
                        counter_b+=1
      if g==2:
            ar=counter_p*3.0+counter_r*2.0+counter_g
      elif g==1:
            ar=counter_p*2.0+counter_r+counter_b*3.0
      elif g==0:
            ar=counter_p+counter_b*2.0+counter_g*3.0
      elif g==3:
            ar=counter_r*3.0+counter_g*2.0+counter_b
      ar=math.ceil(ar/float(2*n-1))
      return int(ar)

def h1_print(t,goal): 
      state=t.state
      n=len(state)
      for i in range (0,n):
            print state[i]
      print "\n ____________________________________________________________ \n"
      counter_r=0
      counter_p=0
      counter_g=0
      counter_b=0
      g=goal[0][0]
      for i in range(0,n):
            for j in range(0,n):
                  if state[i][j]==3:
                         counter_p+=1
                  elif state[i][j]==1:
                        counter_g+=1
                  elif state[i][j]==0:
                        counter_r+=1
                  else:
                        counter_b+=1
      if g==2:
            ar=counter_p*3.0+counter_r*2.0+counter_g
      elif g==1:
            ar=counter_p*2.0+counter_r+counter_b*3.0
      elif g==0:
            ar=counter_p+counter_b*2.0+counter_g*3.0
      elif g==3:
            ar=counter_r*3.0+counter_g*2.0+counter_b
      ar=math.ceil(ar/float(2*n-1))
      return int(ar)  
      
      
#--------------------------------------------------------------------------------------------------------------#
def h2(t,goal) : 
      state=t.state
      counter=0
      n=len(state)
      g=goal[0][0]
      for i in range (0,n):
            for j in range (0,n):
                  if state[i][j]!=g:
                        counter+=1
      r= math.ceil(float(counter)/(2*n-1))
      return int(r)


def h2_print(t,goal) : 
      state=t.state
      counter=0
      n=len(state)
      for i in range (0,n):
            print state[i]
      print "\n ____________________________________________________________ \n"
      g=goal[0][0]
      for i in range (0,n):
            for j in range (0,n):
                  if state[i][j]!=g:
                        counter+=1
      r= math.ceil(float(counter)/(2*n-1))
      return int(r)
#--------------------------------------------------------------------------------------------------------------#
def h4(t,goal):
      state=t.state
      s=0
      counter_r=0
      counter_p=0
      counter_g=0
      counter_b=0
      g=goal[0][0]
      n=len(state)
      suma=0
      ari=[[0 for i in range (0,n)] for j in range (0,n)]
      max1=[0 for i in range (0,n)]
      for x in range (0,n):
            for y in range (0,n):
                 counter_r=0
                 counter_p=0
                 counter_g=0
                 counter_b=0
                 for i in range (0,n):
                        for j in range (0,n):
                              if x==i or y==j:
                                    if state[i][j]==3:
                                          counter_p+=1
                                    elif state[i][j]==1:
                                          counter_g+=1
                                    elif state[i][j]==0:
                                          counter_r+=1
                                    else:
                                          counter_b+=1                              
                 if g==2:
                              if counter_b!=0: 
                                    ar=counter_p*3.0+counter_r*2.0+counter_g+(2*n-1)
                              else:
                                    ar=counter_p*3.0+counter_r*2.0+counter_g
                 elif g==1:
                              if counter_g!=0:
                                    ar=counter_p*2.0+counter_r+counter_b*3.0+(2*n-1)
                              else:
                                    ar=counter_p*2.0+counter_r+counter_b*3.0
                 elif g==0:
                              if counter_r!=0:
                                    ar=counter_p+counter_b*2.0+counter_g*3.0+(2*n-1)
                              else:
                                    ar=counter_p+counter_b*2.0+counter_g*3.0
                 elif g==3:
                             if counter_p!=0:
                                   ar=counter_r*3.0+counter_g*2.0+counter_b+(2*n-1)
                             else:
                                    ar=counter_r*3.0+counter_g*2.0+counter_b
                 ari[x][y]=math.ceil(float(ar)/(2*n-1))
      for i in range (0,n):
            max1[i]=max(ari[i])
      max2=max(max1)
      suma=int(max2)
      return suma

def h4_print(t,goal):
      state=t.state
      s=0
      counter_r=0
      counter_p=0
      counter_g=0
      counter_b=0
      g=goal[0][0]
      n=len(state)
      for i in range (0,n):
            print state[i]
      print "\n ____________________________________________________________ \n"
      suma=0
      ari=[[0 for i in range (0,n)] for j in range (0,n)]
      max1=[0 for i in range (0,n)]
      for x in range (0,n):
            for y in range (0,n):
                 counter_r=0
                 counter_p=0
                 counter_g=0
                 counter_b=0
                 for i in range (0,n):
                        for j in range (0,n):
                              if x==i or y==j:
                                    if state[i][j]==3:
                                          counter_p+=1
                                    elif state[i][j]==1:
                                          counter_g+=1
                                    elif state[i][j]==0:
                                          counter_r+=1
                                    else:
                                          counter_b+=1                              
                 if g==2:
                              if counter_b!=0: 
                                    ar=counter_p*3.0+counter_r*2.0+counter_g+(2*n-1)
                              else:
                                    ar=counter_p*3.0+counter_r*2.0+counter_g
                 elif g==1:
                              if counter_g!=0:
                                    ar=counter_p*2.0+counter_r+counter_b*3.0+(2*n-1)
                              else:
                                    ar=counter_p*2.0+counter_r+counter_b*3.0
                 elif g==0:
                              if counter_r!=0:
                                    ar=counter_p+counter_b*2.0+counter_g*3.0+(2*n-1)
                              else:
                                    ar=counter_p+counter_b*2.0+counter_g*3.0
                 elif g==3:
                             if counter_p!=0:
                                   ar=counter_r*3.0+counter_g*2.0+counter_b+(2*n-1)
                             else:
                                    ar=counter_r*3.0+counter_g*2.0+counter_b
                 ari[x][y]=math.ceil(float(ar)/(2*n-1))
      for i in range (0,n):
            max1[i]=max(ari[i])
      max2=max(max1)
      suma=int(max2)
      return suma
#--------------------------------------------------------------------------------------------------------------#
def h5(t,goal):
      state=t.state
      n=len(state)
      counter=0
      counter_2=0
      g=goal[0][0]
      for i in range(0,n):
            dif=goal[i][i]-state[i][i]
            if dif<0:
                  dif=dif+4
            counter+=dif
            dif_2=goal[i][n-i-1]-state[i][n-i-1]
            if dif_2<0:
                  dif_2=dif_2+4
            counter_2+=dif_2
      ar=int(math.ceil(counter/2.0))
      ar_2=int(math.ceil(counter_2/2.0))
      ar=max(ar,ar_2)
      return ar

def h5_print(t,goal):
      state=t.state
      n=len(state)
      for i in range (0,n):
            print state[i]
      print "\n ____________________________________________________________ \n"
      counter=0
      counter_2=0
      g=goal[0][0]
      for i in range(0,n):
            dif=goal[i][i]-state[i][i]
            if dif<0:
                  dif=dif+4
            counter+=dif
            dif_2=goal[i][n-i-1]-state[i][n-i-1]
            if dif_2<0:
                  dif_2=dif_2+4
            counter_2+=dif_2
      ar=int(math.ceil(counter/2.0))
      ar_2=int(math.ceil(counter_2/2.0))
      ar=max(ar,ar_2)
      return ar

#--------------------------------------------------------------------------------------------------------------#
def h7(t,goal):
       state=t.state
       n=len(state)
       counter=[0 for i in range(0,n)]
       counter_2=[0 for i in range(0,n)]
       counter_3=[0 for i in range(0,n)]
       counter_4=[0 for i in range(0,n)]
       for j in range(0,n):
             c=0
             c_2=0
             c_3=0
             c_4=0
             for i in range(n-1,n-2-j,-1):
                  dif=goal[i][j-c]-state[i][j-c]
                  c+=1
                  if dif<0:
                        dif=dif+4
                  counter[j]+=dif
                  #-------------------------------------#
                  dif_2=goal[j-c_2][i]-state[j-c_2][i]
                  c_2+=1
                  if dif_2<0:
                        dif_2=dif_2+4
                  counter_2[j]+=dif_2
            #======================================#
             for i in range(0,j+1):      
                  dif_3=goal[j-c_3][i]-state[j-c_3][i]
                  c_3+=1
                  if dif_3<0:
                        dif_3=dif_3+4
                  
                  counter_3[j]+=dif_3
                  #--------------------------------------#
                  dif_4=goal[n-1-(j-c_4)][n-1-i]-state[n-1-(j-c_4)][n-1-i]
                  c_4+=1
                  if dif_4<0:
                        dif_4=dif_4+4
                  counter_4[j]+=dif_4
       for j in range (0,n):
                  counter[j]=math.ceil(counter[j]/2.0)
                  counter_2[j]=math.ceil(counter_2[j]/2.0)
                  counter_3[j]=math.ceil(counter_3[j]/2.0)
                  counter_4[j]=math.ceil(counter_4[j]/2.0)
       maxi=0
       for j in range (0,n):
            if counter[j]>maxi:
                 maxi=counter[j]
            if counter_2[j]>maxi:
                 maxi=counter_2[j]
            if counter_3[j]>maxi:
                 maxi=counter_3[j]
            if counter_4[j]>maxi:
                 maxi=counter_4[j]
       return int(maxi)

def h7_print(t,goal):
       state=t.state
       n=len(state)
       for i in range (0,n):
            print state[i]
       print "\n ____________________________________________________________ \n"
       counter=[0 for i in range(0,n)]
       counter_2=[0 for i in range(0,n)]
       counter_3=[0 for i in range(0,n)]
       counter_4=[0 for i in range(0,n)]
       for j in range(0,n):
             c=0
             c_2=0
             c_3=0
             c_4=0
             for i in range(n-1,n-2-j,-1):
                  dif=goal[i][j-c]-state[i][j-c]
                  c+=1
                  if dif<0:
                        dif=dif+4
                  counter[j]+=dif
                  #-------------------------------------#
                  dif_2=goal[j-c_2][i]-state[j-c_2][i]
                  c_2+=1
                  if dif_2<0:
                        dif_2=dif_2+4
                  counter_2[j]+=dif_2
            #======================================#
             for i in range(0,j+1):      
                  dif_3=goal[j-c_3][i]-state[j-c_3][i]
                  c_3+=1
                  if dif_3<0:
                        dif_3=dif_3+4
                  
                  counter_3[j]+=dif_3
                  #--------------------------------------#
                  dif_4=goal[n-1-(j-c_4)][n-1-i]-state[n-1-(j-c_4)][n-1-i]
                  c_4+=1
                  if dif_4<0:
                        dif_4=dif_4+4
                  counter_4[j]+=dif_4
       for j in range (0,n):
                  counter[j]=math.ceil(counter[j]/2.0)
                  counter_2[j]=math.ceil(counter_2[j]/2.0)
                  counter_3[j]=math.ceil(counter_3[j]/2.0)
                  counter_4[j]=math.ceil(counter_4[j]/2.0)
       maxi=0
       for j in range (0,n):
            if counter[j]>maxi:
                 maxi=counter[j]
            if counter_2[j]>maxi:
                 maxi=counter_2[j]
            if counter_3[j]>maxi:
                 maxi=counter_3[j]
            if counter_4[j]>maxi:
                 maxi=counter_4[j]
       return int(maxi)
#--------------------------------------------------------------------------------------------------------------#
def h8(t,goal):
      state=t.state
      n=len(state)
      g=goal[0][0]
      counter_r=0
      counter_p=0
      counter_g=0
      counter_b=0
      counter_r_2=0
      counter_p_2=0
      counter_g_2=0
      counter_b_2=0
      for i in range(0,n):
            if state[i][i]==3:
                  counter_p+=1
            elif state[i][i]==1:
                  counter_g+=1
            elif state[i][i]==0:
                  counter_r+=1
            elif state[i][i]==2:
                  counter_b+=1
            if state[i][n-1-i]==3:
                  counter_p_2+=1
            elif state[i][n-1-i]==1:
                  counter_g_2+=1
            elif state[i][n-1-i]==0:
                  counter_r_2+=1
            elif state[i][n-1-i]==2:
                  counter_b_2+=1
      if g==2:
            ar=counter_p*3.0+counter_r*2.0+counter_g
            ar_2=counter_p_2*3.0+counter_r_2*2.0+counter_g_2
      elif g==1:
            ar=counter_p*2.0+counter_r+counter_b*3.0
            ar_2=counter_p_2*2.0+counter_r_2+counter_b_2*3.0
      elif g==0:
            ar=counter_p+counter_b*2.0+counter_g*3.0
            ar_2=counter_p_2+counter_b_2*2.0+counter_g_2*3.0
      elif g==3:
            ar=counter_r*3.0+counter_g*2.0+counter_b
            ar_2=counter_r_2*3.0+counter_g_2*2.0+counter_b_2
      ar=int(math.ceil(ar/2.0))
      ar_2=int(math.ceil(ar_2/2.0))
      ar=max(ar,ar_2)
      return ar

def h8_print(t,goal):
      state=t.state
      n=len(state)
      for i in range (0,n):
            print state[i]
      print "\n ____________________________________________________________ \n"
      g=goal[0][0]
      counter_r=0
      counter_p=0
      counter_g=0
      counter_b=0
      counter_r_2=0
      counter_p_2=0
      counter_g_2=0
      counter_b_2=0
      for i in range(0,n):
            if state[i][i]==3:
                  counter_p+=1
            elif state[i][i]==1:
                  counter_g+=1
            elif state[i][i]==0:
                  counter_r+=1
            elif state[i][i]==2:
                  counter_b+=1
            if state[i][n-1-i]==3:
                  counter_p_2+=1
            elif state[i][n-1-i]==1:
                  counter_g_2+=1
            elif state[i][n-1-i]==0:
                  counter_r_2+=1
            elif state[i][n-1-i]==2:
                  counter_b_2+=1
      if g==2:
            ar=counter_p*3.0+counter_r*2.0+counter_g
            ar_2=counter_p_2*3.0+counter_r_2*2.0+counter_g_2
      elif g==1:
            ar=counter_p*2.0+counter_r+counter_b*3.0
            ar_2=counter_p_2*2.0+counter_r_2+counter_b_2*3.0
      elif g==0:
            ar=counter_p+counter_b*2.0+counter_g*3.0
            ar_2=counter_p_2+counter_b_2*2.0+counter_g_2*3.0
      elif g==3:
            ar=counter_r*3.0+counter_g*2.0+counter_b
            ar_2=counter_r_2*3.0+counter_g_2*2.0+counter_b_2
      ar=int(math.ceil(ar/2.0))
      ar_2=int(math.ceil(ar_2/2.0))
      ar=max(ar,ar_2)
      return ar
#--------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------       
print "Dwse mou to platos/mhkos tou tetragwnikou pinaka.\n"
n=input()
print 'You got to remember that :red=0 ,green=1,blue=2,purple=3.\n'
print 'Dwse mou thn arxikh katastash se morfh tuple(or  just put None for the default start state).\n'
st_st=input()
print'Dwse mou to goal state se morfh tuple(or  just put None for the default goal state)'
g_st=input()
while True==True:
      print 'Give H1 H2  H4  H5 H7 H8 or exit to exit. \n   '
      print 'If you want to print the user interface add _print to each H (example H1_print)'
      print'If your goal state is something else than all the boxes with the same colour use one of the H8 or H7'
      h=raw_input()
      if h=='exit':
            break
      if st_st==None:
            st_st = tuple([tuple([0 for i in range(0,n)]) for i in range(0,n)])
      if g_st==None:
            g_st=tuple([tuple([2 for i in range(0,n)])for i in range(0,n)])
      ac=(1,1)
      ti1=int(round(time.time() * 1000))
      p = AlienTilesProblem(n,st_st,g_st)
      if h=='H2_print':
            print astar_search(p, lambda node:h2_print(node,g_st)).path()
      elif h=='H2':
            print astar_search(p, lambda node:h2(node,g_st)).path()
      elif h=='H1':
            print astar_search(p, lambda node:h1(node,g_st)).path()
      elif h=='H1_print':
            print astar_search(p, lambda node:h1_print(node,g_st)).path()
      elif h=='H4':
            print astar_search(p, lambda node:h4(node,g_st)).path()
      elif h=='H4_print':
            print astar_search(p, lambda node:h4_print(node,g_st)).path()
      elif h=='H5':
            print astar_search(p, lambda node:h5(node,g_st)).path()
      elif h=='H5_print':
            print astar_search(p, lambda node:h5_print(node,g_st)).path()
      elif h=='H7':
            print astar_search(p, lambda node:h7(node,g_st)).path()
      elif h=='H8':
            print astar_search(p, lambda node:h8(node,g_st)).path()
      elif h=='H7_print':
            print astar_search(p, lambda node:h7_print(node,g_st)).path()
      elif h=='H8_print':
            print astar_search(p, lambda node:h8_print(node,g_st)).path()
      ti2=int(round(time.time() * 1000))
      ti_s=ti2-ti1
      print 'Time to find the optimal solution in miliseconds is:' + ' ' ,ti_s ,' .\n'
      print'To take the correct time dont use the print exctansion'
