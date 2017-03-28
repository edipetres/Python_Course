import random

grammar = {
      "_S"  : ["_NP _VP"],
      "_NP" : ["_N",
               "_A _NP _P _A _N"],
      "_VP" : ["_V",
               "_V _NP"],
      "_N"  : ["developer", "teacher", "student"],
      "_A"  : ["smart", "interesting", "nice", "desperate", "anoying"],
      "_P"  : ["about", "near"],
      "_V"  : ["learns", "trains", "tests", "is", "studies", "asks"]
  }


def expand(grammar):
    
