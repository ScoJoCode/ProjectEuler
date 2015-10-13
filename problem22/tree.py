def isLessThan(s1,s2):
  l1 = len(s1)
  l2 = len(s2)
  for i in range(0,min(l1,l2)):
    if ord(s1[i])<ord(s2[i]):
      return True
    elif ord(s1[i])>ord(s2[i]):
      return False
  if l1<l2:
    return True
  else:
    return False
    

class Node:
  def __init__(self, val):
    self.l = None
    self.r = None
    self.v = val

class Tree:
  def __init__(self):
    self.root = None

  def getRoot(self):
    return self.root

  def add(self, val):
    if(self.root == None):
      self.root = Node(val)
    else:
      self._add(val, self.root)

  def _add(self, val, node):
    if(isLessThan(val,node.v)):
      if(node.l != None):
        self._add(val, node.l)
      else:
        node.l = Node(val)
    else:
      if(node.r != None):
        self._add(val, node.r)
      else:
        node.r = Node(val)

  def deleteTree(self):
    self.root = None

  def printTree(self):
    if(self.root != None):
      self._printTree(self.root)

  def _printTree(self,node):
    if(node != None):
      self._printTree(node.l)
      print str(node.v) + ' '
      self._printTree(node.r)

  def makeArray(self,a):
    if(self.root !=None):
      self._makeArray(self.root,a)

  def _makeArray(self,node,a):
    if(node != None):
      self._makeArray(node.l,a)
      a.append(node.v)
      self._makeArray(node.r,a)

