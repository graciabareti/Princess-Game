# ------------------------------------------------------
#    Team Name: Who's Under That Crown 
# Team Members:Gracia, Abby, Nina
#        Peers: N/A
#   References:https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/
# ------------------------------------------------------

from graphics import * 
import random
from button import *
from windows import *
import time
from scoreclick import *

## Basic Function to demonstrate test suite.

def quitPage(win):
    """ If the user makes the choice to not want to play anymore then they will be brought to a quit user page

    """
  
    exitpage=ExitPage(win,None)
    exitpage.draw()
    clickPoint = win.getMouse()
    if (clickPoint.getX()>150 and clickPoint.getX()<560) and (clickPoint.getY()>430 and clickPoint.getY()<470):
      # press back to start
      # undraw exit pag for first page
      exitpage.undraw()
      # draw first page
      startPage(win) 
      # have to fix start loop from this point
      
def startPage(win):
  """ creates buttons and click point options for each questions window for the user to use

  """
  firstpage=FirstPage(win, None)
  firstpage.draw()
  clickPoint = win.getMouse()
  if (clickPoint.getX()>260 and clickPoint.getX()<330) and (clickPoint.getY()>250 and clickPoint.getY()<290):
    # press start
    #undraw first page for second page
    firstpage.undraw()
    # draw instructions page
    instructions=Instructions(win,None)
    instructions.draw()
    clickPoint = win.getMouse()
  elif (clickPoint.getX()>360 and clickPoint.getX()<430) and (clickPoint.getY()>250 and clickPoint.getY()<290):
    # press quit
    # undraw first page for exit page
    firstpage.undraw()
    # draw exit page
    quitPage(win)
  if(clickPoint.getX()>260and clickPoint.getX()<330) and (clickPoint.getY()>300 and clickPoint.getY()<340):
    # yesbutton 
    # undraw instructions page
    instructions.undraw()
      # draw first question page
    firstquestion=FirstQuestion(win, None)
    firstquestion.draw()
    clickPoint = win.getMouse() 
    click(clickPoint.getX(), clickPoint.getY())
    print("test")
    clickPoint = win.getMouse()
  elif (clickPoint.getX()>360 and clickPoint.getX()<430) and (clickPoint.getY()>300and clickPoint.getY()<340):
      # press no button
      # undraw instructions for exit page
      instructions.undraw()
      # draw exit page
      quitPage(win)
      if (clickPoint.getX()>150 and clickPoint.getX()<560) and (clickPoint.getY()>430 and clickPoint.getY()<470):
      # press back to start
      # undraw exit pag for first page
       exitpage.undraw()
      # draw first page
       firstpage.draw()
       clickPoint = win.getMouse()  
       click(clickPoint.getX(), clickPoint.getY()) 
       clickPoint = win.getMouse()
  if(clickPoint.getX()>570and clickPoint.getX()<660) and (clickPoint.getY()>510 and clickPoint.getY()<550):
    # next button
    # undraw first question page
    firstquestion.undraw()
    # draw second question page
    secondquestion=SecondQuestion(win, None)
    secondquestion.draw()
    clickPoint = win.getMouse()  
    click(clickPoint.getX(), clickPoint.getY()) 
    clickPoint = win.getMouse()
  if(clickPoint.getX()>570and clickPoint.getX()<660) and (clickPoint.getY()>510 and clickPoint.getY()<550):
    # undraw second question page
    secondquestion.undraw()
    # draw third question page
    thirdquestion=ThirdQuestion(win, None)
    thirdquestion.draw()
    clickPoint = win.getMouse()
    click(clickPoint.getX(), clickPoint.getY()) 
    clickPoint = win.getMouse()
  if(clickPoint.getX()>570and clickPoint.getX()<660) and (clickPoint.getY()>510 and clickPoint.getY()<550):
    # undraw third question page
    thirdquestion.undraw()
    # draw fourth question page
    fourthquestion=FourthQuestion(win, None)
    fourthquestion.draw()
    clickPoint = win.getMouse()
    click(clickPoint.getX(), clickPoint.getY()) 
    clickPoint = win.getMouse()
  if(clickPoint.getX()>570and clickPoint.getX()<660) and (clickPoint.getY()>510 and clickPoint.getY()<550):
    # undraw fourth page
    fourthquestion.undraw()
    # draw fifth question page
    fifthquestion=FifthQuestion(win, None)
    fifthquestion.draw()
    clickPoint = win.getMouse()
    click(clickPoint.getX(), clickPoint.getY()) 
    clickPoint = win.getMouse()
  if(clickPoint.getX()>570and clickPoint.getX()<660) and (clickPoint.getY()>510 and clickPoint.getY()<550):
    # undraw fifth question page
    fifthquestion.undraw()
    # draw sixth question page
    sixthquestion=SixthQuestion(win, None)
    sixthquestion.draw()
    clickPoint = win.getMouse()
    click(clickPoint.getX(), clickPoint.getY()) 
    clickPoint = win.getMouse()
  if(clickPoint.getX()>570and clickPoint.getX()<660) and (clickPoint.getY()>510 and clickPoint.getY()<550):
    # undraw sixth question page
    sixthquestion.undraw()
    # draw seventh question page
    seventhquestion=SeventhQuestion(win, None)
    seventhquestion.draw()
    clickPoint = win.getMouse()
    click(clickPoint.getX(), clickPoint.getY()) 
    clickPoint = win.getMouse()
  if(clickPoint.getX()>570and clickPoint.getX()<660) and (clickPoint.getY()>510 and clickPoint.getY()<550):
    # undraw seventh question page
    seventhquestion.undraw()
    # draw eighth question page
    eighthquestion=EighthQuestion(win, None)
    eighthquestion.draw()
    clickPoint = win.getMouse()
    click(clickPoint.getX(), clickPoint.getY()) 
    clickPoint = win.getMouse()
  if(clickPoint.getX()>570and clickPoint.getX()<660) and (clickPoint.getY()>510 and clickPoint.getY()<550):
    # undraw eighth question page
    eighthquestion.undraw()
    # draw ninth question page
    ninthquestion=NinthQuestion(win, None)
    ninthquestion.draw()
    clickPoint = win.getMouse()
    click(clickPoint.getX(), clickPoint.getY()) 
    clickPoint = win.getMouse()
  if(clickPoint.getX()>570and clickPoint.getX()<660) and (clickPoint.getY()>510 and clickPoint.getY()<550):
    # undraw ninth question page
    ninthquestion.undraw()
    # draw tenth question page
    tenthquestion=TenthQuestion(win, None)
    tenthquestion.draw()
    clickPoint = win.getMouse()
    click(clickPoint.getX(), clickPoint.getY()) 
    clickPoint = win.getMouse()
  if(clickPoint.getX()>570and clickPoint.getX()<660) and (clickPoint.getY()>510 and clickPoint.getY()<550):
    # undraw tenth question page
    tenthquestion.undraw()
    # draw eleventh question page
    eleventhquestion=EleventhQuestion(win, None)
    eleventhquestion.draw()
    clickPoint = win.getMouse()
    click(clickPoint.getX(), clickPoint.getY()) 
    clickPoint = win.getMouse()
  if(clickPoint.getX()>570and clickPoint.getX()<660) and (clickPoint.getY()>510 and clickPoint.getY()<550):
    # undraw eleventh question page
    eleventhquestion.undraw()
    # draw twelfth question page
    twelfthquestion=TwelfthQuestion(win, None)
    twelfthquestion.draw()
    clickPoint = win.getMouse()
    click(clickPoint.getX(), clickPoint.getY()) 
    clickPoint = win.getMouse()
  if(clickPoint.getX()>570and clickPoint.getX()<660) and (clickPoint.getY()>510 and clickPoint.getY()<550):
    # undraw twelfth question page
    twelfthquestion.undraw()
    # draw thirteenth question page
    thirteenthquestion=ThirteenthQuestion(win, None)
    thirteenthquestion.draw()
    clickPoint = win.getMouse()
    click(clickPoint.getX(), clickPoint.getY()) 
    clickPoint = win.getMouse()
  if(clickPoint.getX()>570and clickPoint.getX()<660) and (clickPoint.getY()>510 and clickPoint.getY()<550):
    # undraw thirteenth question page
    thirteenthquestion.undraw()
    # draw fourteenth question page
    fourteenthquestion=FourteenthQuestion(win, None)
    fourteenthquestion.draw()
    clickPoint = win.getMouse()
    click(clickPoint.getX(), clickPoint.getY()) 
    clickPoint = win.getMouse()
  if(clickPoint.getX()>570and clickPoint.getX()<660) and (clickPoint.getY()>510 and clickPoint.getY()<550):
    # undraw fourteenth question page
    fourteenthquestion.undraw()
    # draw fifteenth question page
    fifteenthquestion=FifteenthQuestion(win, None)
    fifteenthquestion.draw()
    clickPoint = win.getMouse()
    click(clickPoint.getX(), clickPoint.getY()) 
    clickPoint = win.getMouse()
  if(clickPoint.getX()>570and clickPoint.getX()<660) and (clickPoint.getY()>510 and clickPoint.getY()<550):
    # undraw fifteenth question page
    fifteenthquestion.undraw()
    print("testing")
    tianapage= Tiana(win, None)
    meridapage=Merida(win, None)
    moanapage=Moana(win, None)
    rapunzelpage=Rapunzel(win, None)
    jasminepage=Jasmine(win,None)
    mulanpage=Mulan(win, None)
    vanellopepage=VanellopevonSchweetz(win, None)
    cinderellapage=Cinderella(win, None)
    pocahontaspage=Pocahontas(win, None)
    userPrincess = getPrincess()
    print(userPrincess)
    if userPrincess == "Tiana":
      tianapage.draw()
    if userPrincess== "Merida":
      meridapage.draw()
    if userPrincess== "Moana":
      moanapage.draw()
    if userPrincess== "Rapunzel":
      rapunzelpage.draw()
    if userPrincess== "Jasmine":
      jasminepage.draw()
    if userPrincess== "Mulan":
      mulanpage.draw()
    if userPrincess== "Vanellope von Schweetz":
      vanellopepage.draw()
    if userPrincess== "Cinderella":
      cinderellapage.draw()
    if userPrincess== "Pocahontas":
      pocahontaspage.draw()
    
      
      
    

def main():
  win = GraphWin("Opener", 700, 600)
  win.setBackground('Cyan')
  startPage(win)

if __name__ == "__main__":  
  main()

