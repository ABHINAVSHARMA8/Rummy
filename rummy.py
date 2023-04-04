'''
Name:ABHINAV SHARMA
Roll number: 2019006
Section A
Group 06
'''
''' Description: 2 player game.
'''
''' set=3 or more cards of same suit
	run=collection of continous numbered cards of any set'''

from random import shuffle 
import math
import pygame

pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('RUMMY')

def setup(l):
	for i in range(1,11):
		l+=[i]
	l.extend(['J','Q','K'])
	return l

diamonds=[]
hearts=[]
clubs=[]
spades=[]

a=[diamonds,hearts,clubs,spades]

cards=list(map(setup,a))#done till here
for i in range(13):
	diamonds[i]=str(diamonds[i])+'D'
	hearts[i]=str(hearts[i])+'H'
	spades[i]=str(spades[i])+'S'
	clubs[i]=str(clubs[i])+'C'#done till here

class card():
	def __init__(self,name):
		self.name=name
		if self.name[0]!='1' or len(self.name)==3:
			self.image=pygame.image.load(self.name+'.png')
			self.image=pygame.transform.scale(self.image,(100,90))
		else:
			self.image=pygame.image.load('A'+self.name[1]+'.png')
			self.image=pygame.transform.scale(self.image,(100,90))


def remove(l,a):#working
	''' to remove element a from list l'''
	i=l.index(a)
	return l[:i]+l[i+1:]

def distribute():
	global inplay
	r=inplay[:13]
	for i in range(13):
		inplay=remove(inplay,inplay[0])
	return r
		
class player():
	def __init__(self,lcard=None,points=0,run=[],set=[]):
		self.lcard=distribute()
		self.points=0
		self.run=[]
		self.set=[]

def scoreincrease(l,p):
	score=0
	for i in l:
		if len(i.name)==2:
			if (i.name[0]) in '123456789':
				score+=int(i.name[0][0])
			else:
				score+=10
		else:
			score+=10
	p.points+=score



def set(l,p):
	'''to check wether cards in list l form a set or not.If yes, increase the score of player p'''
	if (len(l)>=3):
		a=l[0].name[-1]
		c=0
		for i in l:
			if i.name[-1]==a:
				c+=1
		if c==len(l):
			p.set.extend(l)
			scoreincrease(l,p)
			for i in l:
				p.lcard=remove(p.lcard,i)
			return 1
		else:
			return 0
		
	
def run(l,p):
	''' to check wether cards in list l form a run or not. If yes, then increment points of player p'''
	if len(l)>=3:
		
		a=0
		for i in range(len(l)-1):
			
				
			if len(l[i].name)==3 or l[i].name[:-1] in 'JKQ':
				v=10
			else:
				v=int(l[i].name[:-1])
			if len(l[i+1].name)==3 or l[i+1].name[:-1] in 'KQJ':
				u=10
			else:
				u=int(l[i+1].name[:-1])
			
			if v-u==-1:
				a+=1
			
		if a==len(l)-1:
			p.run.extend(l)
			scoreincrease(l,p)
			for i in l:
				p.lcard=remove(p.lcard,i)
			return 1
		else:
			return 0

inplay=[]
for i in cards:
	for j in i:
		a=card(j)
		inplay+=[a]

shuffle(inplay)
p1=player()
p2=player()#computer
facestack=[inplay[0]]
inplay=remove(inplay,inplay[0])
downstack=inplay[::]
game=True


p=[]
o,k=1,0

while game:
	print(o,k)
	"""main part of program"""
	for i in pygame.event.get():
		if i.type==pygame.QUIT:
			game=False

	screen.fill((0,255,0))
	
	if len(facestack)!=0:
		screen.blit(facestack[0].image,(250,300))

	if len(p1.run)!=0:
		screen.blit(p1.run[-1].image,(494,350))

	if len(p1.set)!=0:
		screen.blit(p1.set[-1].image,(594,350))

	if len(p2.run)!=0:
		screen.blit(p1.run[-1].image,(494,150))

	if len(p2.set)!=0:
		screen.blit(p2.set[-1].image,(594,150))

	img=pygame.image.load('red_back.png')
	img=pygame.transform.scale(img,(100,90))
	if len(downstack)!=0:
		screen.blit(img,(300,300))
	for i in range(len(p1.lcard)):
		screen.blit(p1.lcard[i].image,(50+i*37,500))

	for i in range(len(p2.lcard)):
		screen.blit(img,(50+i*37,50))
	
		#up or down
		
		for event in pygame.event.get():
			
			if event.type==pygame.MOUSEBUTTONDOWN:
				b=pygame.mouse.get_pos()
				if o==1 and k==0:
					if ((b[0]>=250 and b[0]<=290) and (b[1]>=300 and b[1]<=390)):
						
						p1.lcard+=[facestack[-1]]
						facestack=remove(facestack,facestack[-1])
						o=0
					elif ((b[0]>=300 and b[0]<=400) and (b[1]>=300 and b[1]<=390)):
						
						p1.lcard+=[downstack[-1]]
						downstack=remove(downstack,downstack[-1])
						o=0#working
						
				
				if  o==0 and k==0:
					if b[1]>=500 and b[1]<=590:
						z=(b[0]-50)//37
						print(z)
						p+=[p1.lcard[z]]
						print(p[-1].name)
						
						c=None
						if len(p)==3:
							c=set(p,p1)

							if c==0:

								c=run(p,p1)#do
							for i in p:
								p=remove(p,i)
						if c!=None:
							k=1#working
				if o==0 and k==1:
					if b[1]>=500 and b[1]<=590:
						z=(b[0]-50)//37
						print(z)
						facestack+=[p1.lcard[z]]
						p1.lcard=remove(p1.lcard,p1.lcard[z])
						o,k=1,1#working
					
			
		

		
			if o==1 and k==1:
				print(1)
				x=0
				y=0
				for i in range(len(p2.lcard)):
					if (p2.lcard[i].name[0]) in 'JQK' or len(p2.lcard[i].name[:-1])>1:
						v=10
					else:
						v=int(p2.lcard[i].name[0])

					for j in range(i+1,len(p2.lcard)):
						if (p2.lcard[j].name[0]) in 'JQK' or len(p2.lcard[j].name[:-1])>1:
							u=10
						else:
							u=int(p2.lcard[j].name[0])

						if math.fabs(v-u)==1:
							x+=1
						if p2.lcard[i].name[-1]==p2.lcard[j].name[-1]:
							y+=1

				n=False
				if x>=2 or y>=2:
					n=True

				if n:
					if len(facestack)!=0:
						p2.lcard+=[facestack[-1]]
						facestack=remove(facestack,facestack[-1])
					

				else:
					p2.lcard+=[downstack[-1]]
					downstack=remove(downstack,downstack[-1])
					

				#check for set or run
				rd={}#dict to store count of run cards
				sd={}#dict to store count of cards in set
				for i in range(len(p2.lcard)):
					r=0
					s=0
					rl=[p2.lcard[i]]#list to have cards of run
					sl=[p2.lcard[i]]#list to have cards of set
					
					if (p2.lcard[i].name[0] in 'JQK' or len(p2.lcard[i].name[:-1])==2):
						v=10
					else:
						v=int(p2.lcard[i].name[0])
					for j in range(len(p2.lcard)):
						if i!=j:
							if (p2.lcard[j].name[0] in 'JQK' or len(p2.lcard[j].name[:-1])==2):
								u=10
							else:
								u=int(p2.lcard[j].name[0])
							if math.fabs(v-u)==1+r:
								r+=1
								rl+=[p2.lcard[j]]
							if p2.lcard[i].name[-1]==p2.lcard[j].name[-1]:
								s+=1
								sl+=[p2.lcard[j]]

					if r>=3 and len(rl)>=3:
						rd.update({p2.lcard[i]:[r]+rl})
					if s>=3 and len(sl)>=3:
						sd.update({p2.lcard[i]:[s]+sl})
						
				scores=0
				scorer=0
				if len(rd)!=0:
					maxr=0
					a=None
					for i in rd:
						
						if rd[i][0]>maxr:#check here for same r value
							maxr=rd[i][0]
							a=i

					tempr=rd[a][1:]
					
					
					for i in tempr:
						if i.name[:-1] in '123456789':
							scorer+=int(i.name[:-1])
						elif len(i.name[:-1])==2 or i.name[:-1] in 'JQK':
							scorer+=10

				if len(sd)!=0:
					maxs=0
					
					for i in sd:
						if sd[i][0]>maxs:#check here for same s value
							maxs=sd[i][0]
							b=i

					temps=sd[b][1:]
					
					for i in temps:
						if i.name[:-1] in '123456789':
							scores+=int(i.name[:-1])
						elif len(i.name[:-1])==2 or i.name[:-1] in 'JQK':
							scores+=10
							
				
				if scorer>=scores and (scorer!=0 and scores!=0):
					
					n=run(tempr,p2)
					if n==0:
						for i in rd:
							n=run(rd[i][1:],p2)
							if n==1:
								break
					

				elif scores>scorer :
					
					set(temps,p2)
					


				
				#cpu discarding card,r=0

				discardcpu=[]
				nodicardcpu=[]
				for i in range(len(p2.lcard)):
					a,b=0,0
				
					if (p2.lcard[i].name[0]) in 'JQK' or len(p2.lcard[i].name[:-1])==3:
						v=10
					else:
						v=int(p2.lcard[i].name[0])
					for j in range(i+1,len(p2.lcard)):

						if (p2.lcard[j].name[0]) in 'JQK' or len(p2.lcard[j].name[:-1])==3:
							u=10
						else:
							u=int(p2.lcard[j].name[0])
						if math.fabs(v-u)==1:
							a+=1
						if p2.lcard[i].name[-1]==p2.lcard[i].name[-1]:
							b+=1
					
					if a<2 or b<2:
						discardcpu+=[p2.lcard[i]]
					elif a>=3 or b>=3:
						nodicardcpu+=[p2.lcard[i]]

				if len(discardcpu)!=0:
					facestack+=[discardcpu[0]]
					
					p2.lcard=remove(p2.lcard,discardcpu[0])
					discardcpu=remove(discardcpu,discardcpu[0])
				else:
					for i in p2.lcard:
						if not(i in nodicardcpu):
							facestack+=[i]
							
							p2.lcard=remove(p2.lcard,i)
							discardcpu=remove(discardcpu,i)
							break
				o,k=1,0

			if event.type==pygame.QUIT:#temporary purpose only
				game=False




	if len(p1.lcard)==0 or len(p2.lcard)==0:
		game=False

		if p1.points>p2.points:
			print('YOU WIN!!')
		elif p2.points>p1.points:
			print('Sorry, you lose')
		else:
			print('Draw')
			
	pygame.display.update()#end of loop







