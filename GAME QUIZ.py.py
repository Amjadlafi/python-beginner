print("WELCOM TO MY QIZE")
playing = input ("Do you want play?" )
if playing.lower() != "yes":
     qite()
print("OKAY Let is play :")
score = 0
answer = input("What does CPU stand for?")
if answer.lower() == "centeral procwssing unit":
    
    print("correct!")
    score +=1
else :
        print("Incorrect!")
        
answer = input("What does GPU stand for?")
 
if answer.lower() == "graphics procwssing unit":
    
    print("correct!")
    score +=1

else :
  print("Incorrect!")

answer = input("What does RAM stand for?")

if answer.lower() == "Random access  memory":
    
  print("correct!")
  score +=1
else :
 print("Incorrect!")
         
 answer = input("What does PSU stand for?")
 
if answer.lower() == "POWER SUPPLY":
    
    print("correct!")
    score +=1
else :
  print("Incorrect!")
        
print("YOU HAVE GOT"  + str(score)  + " Quetions correct! " )
print("YOU HAVE GOT"  + str((score/4)*100)+ "%.")  

