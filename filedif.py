import os

def diff(source,target):
  f = open(source,'r')
  g = open(target,'r')

  reference = f.readlines()
  done = g.readlines()
  for i in reference:
    if i not in done:
      print(i)
