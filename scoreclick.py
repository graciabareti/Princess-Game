# ------------------------------------------------------
#    Team Name: Who's Under That Crown
# Team Members:Gracia, Abby, Nina
#        Peers: N/A
#   References: N/A
# ------------------------------------------------------

from graphics import*

score = {"Tiana":0, "Merida":0, "Moana":0, "Rapunzel":0, "Jasmine":0, "Mulan":0, "Vanellope von Schweetz":0, "Cinderella":0, "Pocahontas":0}

def help_score(score, princess):
  """ adds a point to each princess that corresponds to the answer given for each question. Then once all questions have been answered, all the points are added up and the princess with the maximum points selected

 """
  score[princess] = score[princess] + 1

def click (x,y):
  """ if a user clicks on a specific position on the screen with an answer, then a point goes to that specific princess which will be calculated at the end
  """
  
  if(x>30 and x<220 and y>350 and y<390):
    help_score(score, "Tiana")

  if(x>30 and x<220 and y>400 and y<440):
    help_score(score, "Merida")

  if(x>30 and x<220 and y>450 and y<490):
    help_score(score, "Moana")

  if(x>240 and x<430 and y>350 and y<390):
    help_score(score, "Rapunzel")

  if(x>240 and x<430 and y>400 and y<390):
    help_score(score, "Jasmine")

  if(x>240 and x<430 and y>450 and y<440):
    help_score(score, "Mulan")

  if(x>450 and x<640 and y>350 and y<390):
    help_score(score, "Vanellope von Schweetz")
  
  if(x>450 and x<640 and y>400 and y<440):
    help_score(score, "Cinderella")
    
  if(x>450 and x<640 and y>450 and y<490):
    help_score(score, "Pocahontas")

def getPrincess():
  key_list = list(score.keys())
  val_list = list(score.values())
  max_score = max(val_list)
  position = val_list.index(max_score)
  return key_list[position]
  
    



