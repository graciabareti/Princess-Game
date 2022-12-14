# ------------------------------------------------------
#    Team Name: 
# Team Members:Gracia, Abby, Nina
#        Peers: 
#   References:
# Samples Database From: https://www.usabledatabases.com/database/books-isbn-covers/sample/#table_book
# ------------------------------------------------------
# WARNING: DO NOT EDIT THIS FILE

import csv
#from random import randint
header = []

class Question:
  """ A class that runs and displays each trivia question that the user will answer in order to play the game
  
  """
  def __init__(self, id:int, word:str, answer:dict):
    self.__id = id
    self.__question_wording = word
    self.__answers = answer  #dictionary answer:princess

  def getQuestion(self):
    """ returns each question the user must answer to complete the game
    :param self: instance of class
    :return self.__question_wording:(str) wording of question

    """
    return self.__question_wording

  def getAnswer(self):
    """returns user's answers
    :param self: instance of class
    :return self.__answers.keys:(list) list of keys in the dictionary
    """
    
    return list(self.__answers.keys())  #Returns a list of the keys in the dictionary.
    
  def getPrincess(self, user_answer):
    """ once an answer for each question has been selected, this function returns the princess that corresponds to the users answers.
    :param self: instance of class
    :param user_answer:(int)user's answer
    :return self.__answers[user_answer]:returns the princess corresponding to the users answer.
    """
    return self.__answers[user_answer]


def readDatabase():
  """ opens the spreadsheet data file needed for the game and loops through each question listed in the spreadsheet until the user answers all the questions
  :return question_list:(list) returns list of questions

  """
  question_list = []
  line_count = 0
  with open('PrincessData.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      for row in csv_reader:
        if line_count == 0:
          #row.remove(row[0])
          for element in row:
              header.append(element)
          line_count += 1
        else:
          id = row[0]
          question = row[1]
          answer_dict = {}
          for i in range(2,len(row),2):
            answer = row[i]
            princess = row[i+1]
            answer_dict[answer] = princess
          question = Question(id, question, answer_dict)
          question_list.append(question)
          line_count += 1
  return question_list


  

def score ():
  """ adds a point to each princess that corresponds to the answer given for each question. Then once all questions have been answered, all the points are added up and the princess with the maximum points selected

"""
  score = {"Tiana":0, "Merida":0, "Moana":0, "Rapunzel":0, "Jasmine":0, "Mulan":0, "Vanellope von Schweetz":0, "Cinderella":0, "Pocahontas":0}
  question_list = readDatabase()
  round = 1
  for q in question_list:
    print(q.getQuestion())
    answer_list = q.getAnswer()
    for count in range(len(answer_list)):
      print(str(count+1) + ". " + answer_list[count])
    user_response = int(input("What is your answer:"))
    response = answer_list[user_response - 1] 
    princess = q.getPrincess(response)
    help_score(score, princess)
    #score[princess] = score[princess] + 1
    #print(score)
    round +=1
  key_list = list(score.keys())
  val_list = list(score.values())
  max_score = max(val_list)
  position = val_list.index(max_score)
  print("Your princess is: "+ key_list[position])
  
def help_score(score, princess):
  # score = {"Tiana":0, "Merida":0, "Moana":0, "Rapunzel":0}
  # princess = q.getPrincess(response)
  score[princess] = score[princess] + 1
  
# def getprincesses(max_score):
#   match max_score:
    
  
if __name__ == "__main__":
  pass
else:
  pass
  
