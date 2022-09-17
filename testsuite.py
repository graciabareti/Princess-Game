# ------------------------------------------------------
#    Team Name: Who's Under That Crown 
# Team Members: Gracia, Nina, Abby
#        Peers: N/A
#   References: N/A
# ------------------------------------------------------
""" This Python script is for you to test your code before submitting it. 

Usage: click "Shell" next to "Console", then type "python3 tests.py" as shown below:
~/Final-Project$ python3 testsuite.py
"""
import unittest
from main import *
from readspreadsheet import *

class SimpleTest(unittest.TestCase):
 
 def test_score(self):
  score = {"Tiana":0, "Merida":0, "Moana":0, "Rapunzel":0}
  score_final = {"Tiana":0, "Merida":0, "Moana":1, "Rapunzel":0}
  help_score(score, "Moana")
  self.assertEqual(score, score_final)

  def test_readDatabase(self):
    self.assertIn(question, question_list)







    



if __name__ == '__main__':  
  unittest.main()
