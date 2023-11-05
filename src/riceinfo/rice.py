from enum import Enum
import random
class Pun(Enum):
    SHORT = 1,
    MEDIUM = 2,
    LONG = 3,
    DAD = 4,
    RHYME = 5
    
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
            
    def tellPun(punType: Pun) -> str:
        """
        This function returns a Pun based on the Pun Type User input.

        Parameters:
        param1 (Pun): Pun Type.
      
        Returns:
        str: A Pun.
        """
        match punType:
            case Pun.SHORT:
                return random.choice(punsDict[Pun.SHORT])
            case Pun.MEDIUM:
                return random.choice(punsDict[Pun.MEDIUM])
            case Pun.LONG:
                return random.choice(punsDict[Pun.LONG])
            case Pun.DAD:
                return random.choice(punsDict[Pun.DAD])
            case Pun.RHYME:
                return random.choice(punsDict[Pun.RHYME])
            case default:
                return "not a valid PUN TYPE"
            

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


shortPuns = [
    "Rice to meet you!",
    "You're rice on target!",
    "Rice, rice, baby!",
    "Rice is nice!",
    "Fry it up, that's rice!"
]

mediumPuns = [
    "Why did the rice go to the party? Because it wanted to get fried!",
    "I can't be-leaf how much I love rice!",
    "What did the sushi say to the rice? 'You're my roll model.'",
    "Why did the rice call for help? Because it was stuck in a jam!",
    "What do you call a rice-loving vampire? A grain-pire!",
    "Why was the rice grain feeling lonely? It couldn't find its perfect match.",
    "I told my friend a joke about rice, but it was a bit corny. He said, 'Don't be so grainy!'"
]

longPuns = [
     "The rice cooker wanted to be a stand-up comedian, but it realized it couldn't deliver its punchlines without plug-ging in!",
     "Why did the rice cake go to therapy? Because it had too many complex layers and couldn't find its inner pea-ce!",
     "I asked my friend to buy me some rice, but they couldn't find any. They said, 'I looked everywhere, but there was no grain of truth!'",
     "I told my rice cooker a joke, but it didn't laugh. I guess it just couldn't find the humor in the grains.",
     "You're the soy to my sauce, the rice to my bowl, and the nori to my roll – that's why I love you!",
     "Once upon a time, there was a wise rice farmer who said, 'To succeed, you must plant the seeds of hard work and water them with dedication, but don't forget the seasoning of dreams to make life flavorful!'"
]

dadPuns = [
    "Why did the rice cooker start a band? Because it wanted to be a rock star in the kitchen!",
    "What do you call a grain of rice that plays the guitar? A rice picker!",
    "I couldn't find my rice, but then I realized it was in a paddy state!",
    "I asked the rice if it had any good advice, and it said, 'Stay grainy!'"
]

rhymePuns = [
    "Cooking rice nice and slow, makes your meal the way to go.",
    "In a world so fried and flaky, rice remains the real lifesaver, not some fakey.",
    "Rice on a plate, what a fantastic fate!",
    "Rice is the spice of life, cutting through any strife."
]

punsDict = {
    Pun.SHORT : shortPuns,
    Pun.MEDIUM : mediumPuns,
    Pun.LONG : longPuns,
    Pun.DAD : dadPuns,
    Pun.RHYME : rhymePuns
}


    

