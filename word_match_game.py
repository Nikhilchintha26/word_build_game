import random
words=["apple","coder","problems"]
stages=["""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,

"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    H""",

"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    HA""",

"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    HAN""",


"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    HANG""",


"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    HANGM""",



"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    HANGMA""",


"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___      """]
life=0
choo_word=random.choice(words)
display = []
for i in range(0, len(choo_word)):
    display.append("_")
print(display)
end_of_game=False

while not end_of_game:
    guess = input("enter a guess word:").lower()
    for i in range(0, len(choo_word)):
        letter = choo_word[i]
        if letter == guess:
            display[i] = guess
    print(display)
    if "_" not in display:
        print("you win")
        end_of_game = True
    if guess not in choo_word:
        print(stages[life])
        life = life +1
    if life==len(stages):
        print("game over")
        break;