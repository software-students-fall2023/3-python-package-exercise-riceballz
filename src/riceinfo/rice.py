class riceinfo:
    def print_riceball(emotions):
        if emotions.lower() == 'happy':
            print(HappyRiceBall)
        elif emotions.lower() == 'sad':
            print(SadRiceBall)
        elif emotions.lower() == 'angry':
            print(AngryRiceBall)
        elif emotions.lower() == 'nervous':
            print(NervousRiceBall)
        else:
            print("please choose one of the four emotions available: Happy, Sad, Angry, nervous")
            
AngryRiceBall =  r'''
         ##
        /  \
       /    \
      /      \
     /        \
    /  \    /  \
   /    Ò__Ó    \
  /   ________   \          
 /   |########|   \
/____|########|____\
'''


HappyRiceBall =  r'''
         ##
        /  \
       /    \
      /      \
     /  _  _  \
    /   ^  ^   \
   /   \____/   \
  /   ________   \          
 /   |########|   \
/____|########|____\
'''

SadRiceBall =  r'''
          ##
         /  \
        /    \
       /      \
      /        \
     /   v  v   \
    /   .----.   \
   /   '      '   \
  /    ________    \          
 /    |########|    \
/_____|########|_____\
'''

NervousRiceBall = r'''
           ##
          /  \           
         /    \        
        /      \      
       /        \    
      /  __  __  \ 
     /   Ô  O     \
    /      ^       \
   /     ~~~~~~     \
  /     ________     \          
 /     |########|     \
/______|########|______\
'''