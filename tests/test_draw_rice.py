from src.riceinfo.rice import riceinfo
import pytest

## python -m pytest
def test_rice_happy(capsys):
   expected = r'''
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
   riceinfo.print_riceball("happy")
   testOutput = capsys.readouterr()
   actual = testOutput.out.strip()
   assert expected.strip() == actual

def test_rice_sad(capsys):
   expected = r'''
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
   riceinfo.print_riceball("SAD")
   testOutput = capsys.readouterr()
   actual = testOutput.out.strip()
   assert expected.strip() == actual

def test_rice_angry(capsys):
   expected = r'''
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
   riceinfo.print_riceball("angry")
   testOutput = capsys.readouterr()
   actual = testOutput.out.strip()
   assert expected.strip() == actual

def test_rice_confused(capsys):
   expected = r'''
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
   riceinfo.print_riceball("nervous")
   testOutput = capsys.readouterr()
   actual = testOutput.out.strip()
   assert expected.strip() == actual

def test_rice_happy_error(capsys):
   expected = r'''
         ##
        /  \
       /    \
      /      \
     /  _  _  \
    /   <  >   \
   /   \____\   \
  /   ________   \          
 /   |########|   \
/____|########|____\
'''
   riceinfo.print_riceball("happy")
   testOutput = capsys.readouterr()
   actual = testOutput.out.strip()
   assert expected.strip() != actual

def test_rice_incorrect_emotion(capsys):
   riceinfo.print_riceball("funny")
   testOutput = capsys.readouterr()
   actual = testOutput.out
   print(actual)
   assert actual == "please choose one of the four emotions available: Happy, Sad, Angry, nervous\n"
