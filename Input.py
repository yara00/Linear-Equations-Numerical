import numpy as np
import re
import time
from fractions import Fraction


class InputValidator():
  def __init__(self, equations):
        self.equations = equations
        
  variables = set()
  coefArr = []
  b = []
  alpha ="abcdefghijklmnopqrstuvwxyz"
  equations = []
  def __variablesParser(self):
    self.variables = set()
    for i in self.equations:
      matchings = re.findall(r'[\w]+', i)
      for j in matchings:
        if j.isalnum() and not j.isnumeric():
          while j[0].isnumeric():
             j = j[1: len(j)]
          self.variables.add(j)
        
    self.variables = sorted(list(self.variables))
    if len(self.variables) != len(self.equations): return 1
    self.coefArr = np.zeros(shape=(len(self.variables),len(self.variables)))
    self.b = np.zeros(len(self.variables))
    return 0

  def __formatVariables(self):
    for i in range (0, len(self.equations)):
      self.equations[i] = self.equations[i].replace(" ", "")
      for j in range(len(self.variables)-1,-1,-1):
        self.equations[i] = re.sub(self.variables[j], self.alpha[j], self.equations[i])
   

  def __handleMultipleSigns(coef, sign):
    if coef == '+' and sign == '-':
      return '-'
    elif coef == '-' and sign == '+':
      return '-'
    else:
      return '+'

  def __handleCoefvalues(self, i,j, coef,  equalFlag):
    if self.equations[i][j] == "." or self.equations[i][j] == "/":
      return coef + self.equations[i][j]
    if coef == "" and self.equations[i][j] != "=":
      coef = coef + self.equations[i][j]
    elif coef == "-" or coef == "+" and self.equations[i][j] != "=":
      coef = self.handleMultipleSigns(coef, self.equations[i][j] )
    elif self.equations[i][j] != "=" or (self.equations[i][j] == "=" and coef != ""):
      if equalFlag == 0 or self.equations[i][j] == "=":
        try : self.b[i] -= eval(coef)
        except: return "error"
      else:
        try : self.b[i] += eval(coef)
        except: return "error"
      if self.equations[i][j] != "=":
        coef = self.equations[i][j]
      else:
        coef = ""    
    return coef

  def __handleCoefAssignment(self, i,j, coef, equalFlag, variable):
    var = ord(variable) - ord('a')
    if coef == '-' or coef == '+':
      coef = coef + "1"
    if coef != "":
      if equalFlag == 0:
        try :self.coefArr[i][var] += eval(coef)
        except: return "error"
      else :
        try :self.coefArr[i][var] -= eval(coef)
        except: return "error"
    return ""
  validOperations = [".", "-", "+", "/", "="]
  def __handleErrors(self):
    for i in range(0, len(self.equations)):
      coef = ""
      equalFlag = 0
      for j in range(0, len(self.equations[i])):
        if self.equations[i][j] == '=' :
          if equalFlag == 1: return 1
          equalFlag = 1
        if not self.equations[i][j].isalnum():
          if not self.equations[i][j] in self.validOperations:
            return 1
          coef = self.__handleCoefvalues(i,j, coef,  equalFlag)
          if coef == "error": return 1;
        if  self.equations[i][j].isnumeric():
          coef = coef + self.equations[i][j]
          if coef == "error": return 1
        if self.equations[i][j].isalpha():
          if coef == "":
            coef = "1"
          coef =  self.__handleCoefAssignment(i, j, coef,  equalFlag, self.equations[i][j])
      if coef != "":
        try:
          self.b[i] += eval(coef)
        except:
          return 1
    return 0
  
  def validation(self):
    
    self.__variablesParser()
    error = self.__formatVariables()
    if error == 1:
      return error, self.coefArr, self.b, self.variables
    error = self.__handleErrors()
    return error, self.coefArr, self.b, self.variables
