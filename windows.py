# ------------------------------------------------------
#    Team Name: Who's Under That Crown
# Team Members: Gracia, Nina, Abby
#        Peers: N/A
#   References: N/A
# ------------------------------------------------------


from graphics import *
from button import *

class Window:
  """ A class that constructs a window with objects that will be inherited by the question classes

  """
  def __init__(self, win, clickPoint):
    self.win = win
    self.clickPoint = clickPoint
    #objects contains a list of drawable shapes for this screen
    self.objects = []
  def draw(self):
    for object in self.objects:
      object.draw(self.win)
  
  def undraw(self):
    for object in self.objects:
      object.undraw()
      
  def setClick(self, clickPoint):
    self.clickPoint = clickPoint

      
class FirstPage (Window):
  """ A class that constructs a window that contains a welcome page
  
  """
  def __init__(self, win, clickPoint):
    Window.__init__(self, win, clickPoint)
    
    opening=Text(Point(350,40),"Who's Under That Crown Trivia Game")
  
    welcome = Image(Point(350,150), "images/Welcomepage.png")
  
    start= button(Point(260,250), Point(330,290), "START", "grey")

    quit= button(Point(360,250), Point(430,290), "QUIT", "red")
  
    self.objects = [opening, welcome, start, quit]
  # def checkButtons(self):
  #   for object in objects:
  #     if type(object) == button:
  #       if object.inside(clickPoint)==True:
  #         print("button true case")

class Instructions(Window):
  """ A class that constructs a window that include user guide instructions 

  """
  def __init__(self, win, clickPoint):
    Window.__init__(self, win, clickPoint)
  
    instructionsbox= button(Point(80,30), Point(600,250), "Welcome to 'Who's under that Crown'!\n The game that tells you which Disney Princess \n you are most like.To play the game just click \n the button corresponding to the answer \n that represents you best, then click next.", "white")
    
    ready_to_begin=Text(Point(350,280),"Are you ready to begin? ")

    yesbutton= button(Point(260,300), Point(330,340), "YES", "grey")
    
    nobutton= button(Point(360,300), Point(430,340), "NO", "red")

    self.objects = [instructionsbox, ready_to_begin, yesbutton, nobutton]
    
class FirstQuestion(Window):
  """ a class that constructs a window that contains the question, an image and the responses a user can choose for question one

  """
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   questionbox1= button(Point(30,30), Point(600,70), "What's your favorite weekend activity?", "white")
    
   FQ_Image1 = Image(Point(300,200), "images/Q1.png")
  
   answerbutton1_1= button(Point(30,350), Point(220,390), "Cooking", "grey")
   answerbutton1_2= button(Point(30,400), Point(220,440), "Archery", "grey")
   answerbutton1_3= button(Point(30,450), Point(220,490), "Swimming", "grey")
   answerbutton1_4= button(Point(240,350), Point(430,390), "Arts and crafts", "grey")
   answerbutton1_5= button(Point(240,400), Point(430,440), "Spa day", "grey")
   answerbutton1_6= button(Point(240,450), Point(430,490), "Hitting the gym", "grey")
   answerbutton1_7= button(Point(450,350), Point(640,390), "Go-karting", "grey")
   answerbutton1_8= button(Point(450,400), Point(640,440), "Chill Zoo day", "grey")
   answerbutton1_9= button(Point(450,450), Point(640,490), "Nature walks", "grey")  
   nextbutton1=button(Point(570,510), Point(660,550), "NEXT", "red") 
    
   self.objects=[questionbox1,FQ_Image1,answerbutton1_1,answerbutton1_2,answerbutton1_3,answerbutton1_4,answerbutton1_5,answerbutton1_6,answerbutton1_7,answerbutton1_8,answerbutton1_9, nextbutton1]


class SecondQuestion(Window):
  """ a class that constructs a window that contains the question, an image and the responses a user can choose for question two

  """
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)
  
   questionbox2= button(Point(30,30), Point(600,70), "Which animal would you take out for coffee?", "white")
    
   FQ_Image2 = Image(Point(300,200), "images/Q2.png")
  
   answerbutton2_1= button(Point(30,350), Point(220,390), "Frog", "grey")
   answerbutton2_2= button(Point(30,400), Point(220,440), "Bear", "grey")
   answerbutton2_3= button(Point(30,450), Point(220,490), "Chicken", "grey")
   answerbutton2_4= button(Point(240,350), Point(430,390), "Chameleon", "grey")
   answerbutton2_5= button(Point(240,400), Point(430,440), "Tiger", "grey")
   answerbutton2_6= button(Point(240,450), Point(430,490), "Horse", "grey")
   answerbutton2_7= button(Point(450,350), Point(640,390), "Not an animal person", "grey")
   answerbutton2_7.text.setSize(9)  
   answerbutton2_8= button(Point(450,400), Point(640,440), "Mouse", "grey")
   answerbutton2_9= button(Point(450,450), Point(640,490), "Raccoon", "grey")  
   nextbutton2=button(Point(570,510), Point(660,550), "NEXT", "red") 
    
   self.objects=[questionbox2,FQ_Image2,answerbutton2_1,answerbutton2_2,answerbutton2_3,answerbutton2_4,answerbutton2_5,answerbutton2_6,answerbutton2_7,answerbutton2_8,answerbutton2_9, nextbutton2]

class ThirdQuestion(Window):
  """ a class that constructs a window that contains the question, an image and the responses a user can choose for question three

  """
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   questionbox3= button(Point(30,30), Point(600,70), "What best describes you?", "white")
    
   FQ_Image3 = Image(Point(300,200), "images/Q3.png")
  
   answerbutton3_1= button(Point(30,350), Point(220,390), "Workaholic", "grey")
   answerbutton3_2= button(Point(30,400), Point(220,440), "Rebellious", "grey")
   answerbutton3_3= button(Point(30,450), Point(220,490), "Stubborn", "grey")
   answerbutton3_4= button(Point(240,350), Point(430,390), "Selfless", "grey")
   answerbutton3_5= button(Point(240,400), Point(430,440), "Confident", "grey")
   answerbutton3_6= button(Point(240,450), Point(430,490), "Bold", "grey")
   answerbutton3_7= button(Point(450,350), Point(640,390), "Independent", "grey")
   answerbutton3_8= button(Point(450,400), Point(640,440), "Outgoing", "grey")
   answerbutton3_9= button(Point(450,450), Point(640,490), "Warrior", "grey")
   nextbutton3=button(Point(570,510), Point(660,550), "NEXT", "red")
    
   self.objects=[questionbox3,FQ_Image3,answerbutton3_1,answerbutton3_2,answerbutton3_3,answerbutton3_4,answerbutton3_5,answerbutton3_6,answerbutton3_7,answerbutton3_8,answerbutton3_9, nextbutton3]

class FourthQuestion(Window):
  """ a class that constructs a window that contains the question, an image and the responses a user can choose for question four

  """
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   questionbox4= button(Point(30,30), Point(600,70), "Where would you like to vacation?", "white")
    
   FQ_Image4 = Image(Point(300,200), "images/Q4.png")
  
   answerbutton4_1= button(Point(30,350), Point(220,390), "New Orleans", "grey")
   answerbutton4_2= button(Point(30,400), Point(220,440), "Scotland", "grey")
   answerbutton4_3= button(Point(30,450), Point(220,490), "Fiji", "grey")
   answerbutton4_4= button(Point(240,350), Point(430,390), "California", "grey")
   answerbutton4_5= button(Point(240,400), Point(430,440), "Egypt", "grey")
   answerbutton4_6= button(Point(240,450), Point(430,490), "China", "grey")
   answerbutton4_7= button(Point(450,350), Point(640,390), "Palo Alto", "grey")
   answerbutton4_8= button(Point(450,400), Point(640,440), "France", "grey")
   answerbutton4_9= button(Point(450,450), Point(640,490), "Bahamas", "grey")
   nextbutton4=button(Point(570,510), Point(660,550), "NEXT", "red")
    
   self.objects=[questionbox4,FQ_Image4,answerbutton4_1,answerbutton4_2,answerbutton4_3,answerbutton4_4,answerbutton4_5,answerbutton4_6,answerbutton4_7,answerbutton4_8,answerbutton4_9,nextbutton4]

class FifthQuestion(Window):
  """ a class that constructs a window that contains the question, an image and the responses a user can choose for question five

  """
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   questionbox5= button(Point(30,30), Point(600,70), "When I am older, I would like to live in a...","white")
    
   FQ_Image5 = Image(Point(300,200), "images/Q5.png")
  
   answerbutton5_1= button(Point(30,350), Point(220,390), "Large House", "grey")
   answerbutton5_2= button(Point(30,400), Point(220,440), "Ranch", "grey")
   answerbutton5_3= button(Point(30,450), Point(220,490), "Beach House", "grey")
   answerbutton5_4= button(Point(240,350), Point(430,390), "Penthouse", "grey")
   answerbutton5_5= button(Point(240,400), Point(430,440), "Luxury Condo", "grey")
   answerbutton5_6= button(Point(240,450), Point(430,490), "Apartment", "grey")
   answerbutton5_7= button(Point(450,350), Point(640,390), "Tiny House", "grey")
   answerbutton5_8= button(Point(450,400), Point(640,440), "Cabin", "grey")
   answerbutton5_9= button(Point(450,450), Point(640,490), "Yurt", "grey")  
   nextbutton5=button(Point(570,510), Point(660,550), "NEXT", "red")
    
   self.objects=[questionbox5,FQ_Image5,answerbutton5_1,answerbutton5_2,answerbutton5_3,answerbutton5_4,answerbutton5_5,answerbutton5_6,answerbutton5_7,answerbutton5_8,answerbutton5_9,nextbutton5]

class SixthQuestion(Window):
  """ a class that constructs a window that contains the question, an image and the responses a user can choose for question six

  """
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   questionbox6= button(Point(30,30), Point(600,70), "What is your intended major/field?", "white")
    
   FQ_Image6 = Image(Point(300,200), "images/Q6.png")
  
   answerbutton6_1= button(Point(30,350), Point(220,390), "Business/Entrepreneurship", "grey")
   answerbutton6_1.text.setSize(9)
    
   answerbutton6_2= button(Point(30,400), Point(220,440), "Humanities", "grey")
   answerbutton6_2.text.setSize(10)
    
   answerbutton6_3= button(Point(30,450), Point(220,490), "Biological Sciences", "grey")
   answerbutton6_3.text.setSize(9)
    
   answerbutton6_4= button(Point(240,350), Point(430,390), "Visual and Performing Arts", "grey")
   answerbutton6_4.text.setSize(9)
    
   answerbutton6_5= button(Point(240,400), Point(430,440), "Aviation and Airway Science", "grey")
   answerbutton6_5.text.setSize(9)
    
   answerbutton6_6= button(Point(240,450), Point(430,490), "Gender Studies/History", "grey")
   answerbutton6_6.text.setSize(9)
    
   answerbutton6_7= button(Point(450,350), Point(640,390), "Technology", "grey")
   answerbutton6_7.text.setSize(10)
    
   answerbutton6_8= button(Point(450,400), Point(640,440), "Fashion Design", "grey")
   answerbutton6_8.text.setSize(10)
    
   answerbutton6_9= button(Point(450,450), Point(640,490), "Environmental Science", "grey")   
   answerbutton6_9.text.setSize(9)
    
   nextbutton6=button(Point(570,510), Point(660,550), "NEXT", "red") 
    
   self.objects=[questionbox6,FQ_Image6,answerbutton6_1,answerbutton6_2,answerbutton6_3,answerbutton6_4,answerbutton6_5,answerbutton6_6,answerbutton6_7,answerbutton6_8,answerbutton6_9, nextbutton6]

class SeventhQuestion(Window):
  """ a class that constructs a window that contains the question, an image and the responses a user can choose for question seven

  """
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   questionbox7= button(Point(30,30), Point(600,70), "What is your favorite spot to study on campus?", "white")
    
   FQ_Image7 = Image(Point(300,200), "images/Q7.png")
  
   answerbutton7_1= button(Point(30,350), Point(220,390), "Neilson Library", "grey")
   answerbutton7_2= button(Point(30,400), Point(220,440), "Ainsworth Gym", "grey")
   answerbutton7_3= button(Point(30,450), Point(220,490), "Crew House", "grey")
   answerbutton7_4= button(Point(240,350), Point(430,390), "Your Room", "grey")
   answerbutton7_5= button(Point(240,400), Point(430,440), "Sage Hall", "grey")
   answerbutton7_6= button(Point(240,450), Point(430,490), "Ainsworth Gym", "grey")
   answerbutton7_7= button(Point(450,350), Point(640,390), "Ford Hall", "grey")
   answerbutton7_8= button(Point(450,400), Point(640,440), "Hillyer Art Library", "grey")
   answerbutton7_9= button(Point(450,450), Point(640,490), "Burton Hall", "grey")  
   nextbutton7=button(Point(570,510), Point(660,550), "NEXT", "red") 
    
   self.objects=[questionbox7,FQ_Image7,answerbutton7_1,answerbutton7_2,answerbutton7_3,answerbutton7_4,answerbutton7_5,answerbutton7_6,answerbutton7_7,answerbutton7_8,answerbutton7_9, nextbutton7]

class EighthQuestion(Window):
  """ a class that constructs a window that contains the question, an image and the responses a user can choose for question eight

  """
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   questionbox8= button(Point(30,30), Point(600,70), "What is your favorite food?", "white")
    
   FQ_Image8 = Image(Point(300,200), "images/Q8.png")
  
   answerbutton8_1= button(Point(30,350), Point(220,390), "Gumbo", "grey")
   answerbutton8_2= button(Point(30,400), Point(220,440), "Steak", "grey")
   answerbutton8_3= button(Point(30,450), Point(220,490), "Seafood", "grey")
   answerbutton8_4= button(Point(240,350), Point(430,390), "Salad", "grey")
   answerbutton8_5= button(Point(240,400), Point(430,440), "Fruit Salad", "grey")
   answerbutton8_6= button(Point(240,450), Point(430,490), "Traditional Foods", "grey")
   answerbutton8_7= button(Point(450,350), Point(640,390), "Candy", "grey")
   answerbutton8_8= button(Point(450,400), Point(640,440), "Charcuterie Board", "grey")
   answerbutton8_9= button(Point(450,450), Point(640,490), "Smoothie Bowls", "grey")  
   nextbutton8=button(Point(570,510), Point(660,550), "NEXT", "red") 
    
   self.objects=[questionbox8,FQ_Image8,answerbutton8_1,answerbutton8_2,answerbutton8_3,answerbutton8_4,answerbutton8_5,answerbutton8_6,answerbutton8_7,answerbutton8_8,answerbutton8_9, nextbutton8]

class NinthQuestion(Window):
  """ a class that constructs a window that contains the question, an image and the responses a user can choose for question nine

  """
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   questionbox9= button(Point(30,30), Point(600,70), "Are you responsible with money?", "white")
    
   FQ_Image9 = Image(Point(300,200), "images/Q9.png")
  
   answerbutton9_1= button(Point(30,350), Point(220,390), "Yes", "grey")
   answerbutton9_2= button(Point(30,400), Point(220,440), "What is responsibility?", "grey")
   answerbutton9_2.text.setSize(10)
   answerbutton9_3= button(Point(30,450), Point(220,490), "No", "grey")
   answerbutton9_4= button(Point(240,350), Point(430,390), "What is money?", "grey")
   answerbutton9_5= button(Point(240,400), Point(430,440), "Loaded", "grey")
   answerbutton9_6= button(Point(240,450), Point(430,490), "From old money", "grey")
   answerbutton9_7= button(Point(450,350), Point(640,390), "Who needs money?", "grey")
   answerbutton9_8= button(Point(450,400), Point(640,440), "I don't have a job", "grey")
   answerbutton9_9= button(Point(450,450), Point(640,490), "I was robbed", "grey")  
   nextbutton9=button(Point(570,510), Point(660,550), "NEXT", "red") 
    
   self.objects=[questionbox9,FQ_Image9,answerbutton9_1,answerbutton9_2,answerbutton9_3,answerbutton9_4,answerbutton9_5,answerbutton9_6,answerbutton9_7,answerbutton9_8,answerbutton9_9, nextbutton9]

class TenthQuestion(Window):
  """ a class that constructs a window that contains the question, an image and the responses a user can choose for question ten

  """
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   questionbox10= button(Point(30,30), Point(600,70), "What career would you like to pursue?", "white")
    
   FQ_Image10 = Image(Point(300,200), "images/Q10.png")
  
   answerbutton10_1= button(Point(30,350), Point(220,390), "A CEO/business owner", "grey")
   answerbutton10_2= button(Point(30,400), Point(220,440), "A Professional Athlete", "grey")
   answerbutton10_3= button(Point(30,450), Point(220,490), "Military", "grey")
   answerbutton10_4= button(Point(240,350), Point(430,390), "Teacher", "grey")
   answerbutton10_5= button(Point(240,400), Point(430,440), "Politician", "grey")
   answerbutton10_6= button(Point(240,450), Point(430,490), "Pro-Fighter", "grey")
   answerbutton10_7= button(Point(450,350), Point(640,390), "Software Engineer", "grey")
   answerbutton10_8= button(Point(450,400), Point(640,440), "Vet", "grey")
   answerbutton10_9= button(Point(450,450), Point(640,490), "Translator", "grey")  
   nextbutton10=button(Point(570,510), Point(660,550), "NEXT", "red") 
    
   self.objects=[questionbox10,FQ_Image10,answerbutton10_1,answerbutton10_2,answerbutton10_3,answerbutton10_4,answerbutton10_5,answerbutton10_6,answerbutton10_7,answerbutton10_8,answerbutton10_9, nextbutton10]

class EleventhQuestion(Window):
  """ a class that constructs a window that contains the question, an image and the responses a user can choose for question eleven

  """
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   questionbox11= button(Point(30,30), Point(600,70), "One word that describes your style.", "white")
    
   FQ_Image11 = Image(Point(300,200), "images/Q11.png")
  
   answerbutton11_1= button(Point(30,350), Point(220,390), "Retro", "grey")
   answerbutton11_2= button(Point(30,400), Point(220,440), "Functional", "grey")
   answerbutton11_3= button(Point(30,450), Point(220,490), "Colorful", "grey")
   answerbutton11_4= button(Point(240,350), Point(430,390), "Medieval", "grey")
   answerbutton11_5= button(Point(240,400), Point(430,440), "Elegant", "grey")
   answerbutton11_6= button(Point(240,450), Point(430,490), "Sporty", "grey")
   answerbutton11_7= button(Point(450,350), Point(640,390), "Sweats", "grey")
   answerbutton11_8= button(Point(450,400), Point(640,440), "Formal", "grey")
   answerbutton11_9= button(Point(450,450), Point(640,490), "Traditional", "grey")  
   nextbutton11=button(Point(570,510), Point(660,550), "NEXT", "red") 
    
   self.objects=[questionbox11,FQ_Image11,answerbutton11_1,answerbutton11_2,answerbutton11_3,answerbutton11_4,answerbutton11_5,answerbutton11_6,answerbutton11_7,answerbutton11_8,answerbutton11_9, nextbutton11]

class TwelfthQuestion(Window):
  """ a class that constructs a window that contains the question, an image and the responses a user can choose for question tweleve

  """
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   questionbox12= button(Point(30,30), Point(600,70), "What is your ideal date at night?", "white")
    
   FQ_Image12 = Image(Point(300,200), "images/Q12.png")
  
   answerbutton12_1= button(Point(30,350), Point(220,390), "Dinner", "grey")
   answerbutton12_2= button(Point(30,400), Point(220,440), "Going Outdoors", "grey")
   answerbutton12_3= button(Point(30,450), Point(220,490), "Beach Day", "grey")
   answerbutton12_4= button(Point(240,350), Point(430,390), "Romantic Boat Ride", "grey")
   answerbutton12_5= button(Point(240,400), Point(430,440), "Plane ride", "grey")
   answerbutton12_6= button(Point(240,450), Point(430,490), "Axe-throwing", "grey")
   answerbutton12_7= button(Point(450,350), Point(640,390), "NASCAR date", "grey")
   answerbutton12_8= button(Point(450,400), Point(640,440), "Ballroom dancing", "grey")
   answerbutton12_9= button(Point(450,450), Point(640,490), "Archery date", "grey")  
   nextbutton12=button(Point(570,510), Point(660,550), "NEXT", "red") 
    
   self.objects=[questionbox12,FQ_Image12,answerbutton12_1,answerbutton12_2,answerbutton12_3,answerbutton12_4,answerbutton12_5,answerbutton12_6,answerbutton12_7,answerbutton12_8,answerbutton12_9, nextbutton12]

class ThirteenthQuestion(Window):
  """ a class that constructs a window that contains the question, an image and the responses a user can choose for question thirteen

  """
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   questionbox13= button(Point(30,30), Point(600,70), "One of your strengths is your ability to be:", "white")
    
   FQ_Image13 = Image(Point(300,200), "images/Q13.png")
  
   answerbutton13_1= button(Point(30,350), Point(220,390), "Industrious", "grey")
   answerbutton13_2= button(Point(30,400), Point(220,440), "Scrappy/Determined", "grey")
   answerbutton13_3= button(Point(30,450), Point(220,490), "Brave", "grey")
   answerbutton13_4= button(Point(240,350), Point(430,390), "Friendly", "grey")
   answerbutton13_5= button(Point(240,400), Point(430,440), "Cunning", "grey")
   answerbutton13_6= button(Point(240,450), Point(430,490), "Fearless", "grey")
   answerbutton13_7= button(Point(450,350), Point(640,390), "Persistent", "grey")
   answerbutton13_8= button(Point(450,400), Point(640,440), "Kind", "grey")
   answerbutton13_9= button(Point(450,450), Point(640,490), "Persausive", "grey")  
   nextbutton13=button(Point(570,510), Point(660,550), "NEXT", "red") 
    
   self.objects=[questionbox13,FQ_Image13,answerbutton13_1,answerbutton13_2,answerbutton13_3,answerbutton13_4,answerbutton13_5,answerbutton13_6,answerbutton13_7,answerbutton13_8,answerbutton13_9, nextbutton13]

class FourteenthQuestion(Window):
  """ a class that constructs a window that contains the question, an image and the responses a user can choose for question fourteen

  """
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   questionbox14= button(Point(30,30), Point(600,70), "What is your go to genre of music?", "white")
    
   FQ_Image14 = Image(Point(300,200), "images/Q14.png")
  
   answerbutton14_1= button(Point(30,350), Point(220,390), "Jazz", "grey")
   answerbutton14_2= button(Point(30,400), Point(220,440), "Folk", "grey")
   answerbutton14_3= button(Point(30,450), Point(220,490), "Reggae", "grey")
   answerbutton14_4= button(Point(240,350), Point(430,390), "Pop", "grey")
   answerbutton14_5= button(Point(240,400), Point(430,440), "R&B", "grey")
   answerbutton14_6= button(Point(240,450), Point(430,490), "Rock", "grey")
   answerbutton14_7= button(Point(450,350), Point(640,390), "K-Pop", "grey")
   answerbutton14_8= button(Point(450,400), Point(640,440), "Country", "grey")
   answerbutton14_9= button(Point(450,450), Point(640,490), "Indie", "grey")  
   nextbutton14=button(Point(570,510), Point(660,550), "NEXT", "red") 
    
   self.objects=[questionbox14,FQ_Image14,answerbutton14_1,answerbutton14_2,answerbutton14_3,answerbutton14_4,answerbutton14_5,answerbutton14_6,answerbutton14_7,answerbutton14_8,answerbutton14_9, nextbutton14]

class FifteenthQuestion(Window):
  """ a class that constructs a window that contains the question, an image and the responses a user can choose for question fifthteen

  """
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   questionbox15= button(Point(30,30), Point(600,70), "What magical power would you want?", "white")
    
   FQ_Image15 = Image(Point(300,200), "images/Q15.png")
  
   answerbutton15_1= button(Point(30,350), Point(220,390), "Shapeshifting", "grey")
   answerbutton15_2= button(Point(30,400), Point(220,440), "Super Strength", "grey")
   answerbutton15_3= button(Point(30,450), Point(220,490), "Water bending", "grey")
   answerbutton15_4= button(Point(240,350), Point(430,390), "Immortality", "grey")
   answerbutton15_5= button(Point(240,400), Point(430,440), "Flight", "grey")
   answerbutton15_6= button(Point(240,450), Point(430,490), "Teleportation", "grey")
   answerbutton15_7= button(Point(450,350), Point(640,390), "Speed", "grey")
   answerbutton15_8= button(Point(450,400), Point(640,440), "Invsibility", "grey")
   answerbutton15_9= button(Point(450,450), Point(640,490), "Ability to speak to animals", "grey")  
   answerbutton15_9.text.setSize(9)
   nextbutton15=button(Point(570,510), Point(660,550), "NEXT", "red") 
    
   self.objects=[questionbox15,FQ_Image15,answerbutton15_1,answerbutton15_2,answerbutton15_3,answerbutton15_4,answerbutton15_5,answerbutton15_6,answerbutton15_7,answerbutton15_8,answerbutton15_9, nextbutton15]

class Tiana(Window):
  """ Displays a picture and a description of Tiana if the user chooses the maximum amount of responses corresponding to her

  """
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)
                       
   P_Tiana = Image(Point(320,300), "images/tiana.png")
    
   princessboxTiana= button(Point(30,350), Point(600,550), "Your Princess is Tiana! \n You’re entrepreneurial, talented, and kind.\n You’re not afraid of putting in hard work and \n getting the job done. As a high-energy \n and driven woman, Tiana is the epitome of \n an Achiever.  You're motivated by success \n and the public’s perception of you.", "white")
   self.objects=[P_Tiana,princessboxTiana]

class Merida(Window):
  """ Displays a picture and a description of Merida if the user chooses the maximum amount of responses corresponding to her"""
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)
                         
   P_Merida = Image(Point(300,470), "images/merida.png")
    
   princessboxMerida= button(Point(60,400), Point(600,550), "Your Princess is Merida! \n You’re adventurous, headstrong and daring. \n You and Merida break traditions and pave \n your own path. You both love being active, \n and you are a great athlete. Your favorite place \n to be is outside!", "white")
   self.objects=[P_Merida,princessboxMerida]

class Moana(Window):
  """ Displays a picture and a description of Moana if the user chooses the maximum amount of responses corresponding to her """
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)
                      
   P_Moana = Image(Point(300,350), "images/moana.png")
  
   princessboxMoana= button(Point(30,400), Point(650,550), "Your Princess is Moana \n You are vibrant, strong-willed and optimistic. You and Moana love the \n ocean, you care about it, and it feels like home to you. You are an \n intelligent, capable and compassionate leader who will take risks \n to do what you believe is right.", "white")
   self.objects=[P_Moana,princessboxMoana]
  
class Rapunzel(Window):
  """ Displays a picture and a description of Rapunzel if the user chooses the maximum amount of responses corresponding to her

  """ 
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   P_Rapunzel= Image(Point(350,450),"images/rapunzel.png")
   
   princessboxRapunzel= button(Point(30,400), Point(650,550),"Your Princess is Rapunzel! \n You're creative and hopeful even in difficult circumstances.\n You and Rapunzel have an optimistic outlook on life, and you \n follow your dreams wherever they lead. Your free spirited nature allows \n you to enjoy life to its fullest. Just remember to pack your frying pan \n on your next adventure.", "white")
   self.objects=[P_Rapunzel,princessboxRapunzel]                      
 

class Jasmine(Window):
  """ Displays a picture and a description of Jasmine if the user chooses the maximum amount of responses corresponding to her

  """
  
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   P_Jasmine= Image(Point(300,300), "images/jasmine.png")
                         
   princessboxJasmine = button(Point(30,400), Point(650,550), "Your Princess is Jasmine \n You’re driven, confident, and compassionate. You want to see \n the world and go on as many adventures as possible. You and \n Jasmine excel at confrontation and leadership. Your biggest \n motivation is defending justice for yourself and others. We \nknow you are destined for great things!", "white")
   self.objects=[P_Jasmine,princessboxJasmine]  

class Mulan(Window):
  """ Displays a picture and a description of Mulan if the user chooses the maximum amount of responses corresponding to her

  """
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   P_Mulan= Image(Point(350,310), "images/mulan.png")
                         
   princessboxMulan = button(Point(50,350), Point(630,550),"Your Princess is Mulan! \n You and Mulan are excellent athletes, you push \n your physical boundaries to be the best at what\n you do. You are bold, brave and compassionate. You \n are willing to risk your life to protect the people \n you love. You respect cultural traditions but also \n  understand that some rules should be broken, \n and you are not afraid to push the boundaries of gender.", "white")
   self.objects=[P_Mulan,princessboxMulan]  
                      
                            
class VanellopevonSchweetz(Window):
  """ Displays a picture and a description of Vanellope von Schweetz if the user chooses the maximum amount of responses corresponding to her

  """
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   P_VanellopevonSchweetz= Image(Point(350,250), "images/vanellope.png")
                         
   princessboxVanellope = button(Point(50,350), Point(630,550), "Your Princess is Vanellope von Schweetz! \n You are strong, fun, and an absolute legend on the race track \n and on the computer. You are a breath of fresh air for those \n around you. You are always up for an adventure, and you \n approach every challenge with positivity and curiosity. \n You’re our hero!", "white")
   self.objects=[P_VanellopevonSchweetz,princessboxVanellope]  

class Cinderella(Window):
  """ Displays a picture and a description of Cinderella if the user chooses the maximum amount of responses corresponding to her"""
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   P_Cinderella= Image(Point(300,200), "images/cinderella.png")
                         
   princessboxCinderella = button(Point(100,350), Point(550,550), "Your Princess is Cinderella! \n You and Cinderella are kind, gentle and industrious. \n You are a friend to all, especially the vulnerable.\n You love animals and the simple pleasures in life, \n but you are also boujee at heart.", "white")
   self.objects=[P_Cinderella,princessboxCinderella] 
  
class Pocahontas(Window):
  """ Displays a picture and a description of Pochontas if the user chooses the maximum amount of responses corresponding to her

  """ 
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   P_Pocahontas= Image(Point(300,300), "images/pocahontas.png")
                         
   princessboxPocahontas = button(Point(110,350), Point(600,500), "Your Princess is Pocahontas! \n You’re courageous and open-minded, with \n an inner strength that’s steady as the beating drum. \n You are adventurous and feel at home in nature.\n Above all, you are fierce in the defense of what you love.", "white")

   self.objects=[P_Pocahontas, princessboxPocahontas] 
                              

class ExitPage(Window):
  """
  constructs an exit page that put a sadface window, to be used any time user chooses not to continue
  """
  def __init__(self, win, clickPoint):
   Window.__init__(self, win, clickPoint)

   goodbyebox= button(Point(30,30), Point(660,70), "OK BYE", "white")

   Exitpage = Image(Point(350,250), "images/Exitpage.gif")
    
   backtostart=button(Point(150,430), Point(560,470), "BACK TO START", "red")

   self.objects=[goodbyebox,Exitpage,backtostart]
  
   