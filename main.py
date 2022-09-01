print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1.lower()
name2.lower()

#reset letter counter
TrueOccur = 0
LoveOccur = 0
LoveScore = 0

#Finding t.r.u.e letters
TrueOccur += (name1.count('t') + name2.count('t'))
TrueOccur += (name1.count('r') + name2.count('r'))
TrueOccur += (name1.count('u') + name2.count('u'))
TrueOccur += (name1.count('e') + name2.count('e'))

#Finding l.o.v.e letters
LoveOccur += (name1.count('l') + name2.count('l'))
LoveOccur += (name1.count('o') + name2.count('o'))
LoveOccur += (name1.count('v') + name2.count('v'))
LoveOccur += (name1.count('e') + name2.count('e'))

LoveScore = int(str(TrueOccur) + str(LoveOccur))

#results presentation
if LoveScore <10 or LoveScore> 90:
  print(f"Your score is {LoveScore}, you go together like coke and mentos.")
elif LoveScore >40 and LoveScore<50:
  print(f"Your score is {LoveScore}, you are alright together.")
else:
  print(f"Your score is {LoveScore}")