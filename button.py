# ------------------------------------------------------
#    Team Name:Who's Under That Crown 
# Team Members:Gracia, Abby, Nina
#        Peers: N/A
#   References:N/A
# ------------------------------------------------------


from graphics import *


class button:
  """ constructs buttons for game 
  
  """
  def __init__(self, left,right,text, color):
    self.left=left
    self.right=right
    self.body=Rectangle(left, right)
    #split the text argument by \n
    #iterate over the text argument and turn each row into a Text object and add this to the self.text array
    #make sure that you adjust the points to fit well into the screen
    self.text = Text(Point(left.getX()+(right.getX()-left.getX())/2,left.getY()+(right.getY()-left.getY())/2),text)
    self.body.setFill(color)
  
  def draw(self, win):
    self.body.draw(win)
    self.text.draw(win)
  
  def undraw(self):
    self.body.undraw()
    self.text.undraw()
     
  def inside(point, rectangle):
    
    ll = self.left 
    ur = self.right
    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()
  
  
