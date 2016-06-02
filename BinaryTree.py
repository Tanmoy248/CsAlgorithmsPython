# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 18:56:03 2015

@author: thakut1
"""
# implementation with node traversal methods
class Node():
    def __init__(self,val,parent= None):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None
class Tree():
    def __init__(self):
        self.root = None
    def getRoot(self):
        return self.root
    def add(self,val):
        if self.root == None:
            self.root = Node(val)
        else:
            self._add(val,self.root)
    def _add(self,val,node):
        if val < node.val:
            if node.left is not None:
                self._add(val,node.left)
            else:
                node.left = Node(val,node)
        else:
            if node.right is not None:
                self._add(val,node.right)
            else:
                node.right = Node(val,node)
    
    def find(self, val):
        # Search complexity when balanced tree is O(logn)
        if self.root is not None:
            return self._find(val,self.root)
        else:
            return None
    def _find(self,val,node):
        #print val,node.val
        if val == node.val:
            #print "matched"
            return node
        elif val < node.val and node.left is not None:
            return self._find(val,node.left)
        elif val > node.val and node.right is not None:
            return self._find(val,node.right)
        else:
            print val,"value not found"
            return None
    def deleteTree(self):
        self.root = None
        
    def delete_node(self,val):
        node = self.find(val)
        if node is None:
            return None
        else:
            self._delete_node(val,node)
    
    def _delete_node(self,val,node):
        if node == self.root:
            self.root = None
        else:
            # Case 1 when the node is a left node and a right node exists
            #if node == node.parent.left and node.left is not None:
            if node.left is not None:
                replacement = self.find(self.maximum(node.left.val))
                node.parent.left = replacement
                self.delete_node(replacement.val)
            #elif node == node.parent.right and node.right is not None:
            elif node.right is not None:
                r_val = node.right
                print "right node val",r_val.val
                print "minimum", self.minimum(r_val.val)
                replacement = self.find(self.minimum(node.right.val))
                # recursively delete the replacement from original position
                self.delete_node(replacement.val)
                node.parent.right = replacement
                replacement.parent = node.parent
                print "new right child",node.parent.right.val
                
                #removing all links for deleted node
                node.parent = None
                node.left = None
                node.right = None
            elif node.left is None and node.right is None:
                # Case 3 : Its a leaf node
                node.parent = None
                
    
    
    
    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)
    
    # The printTree is a inorder tree walk
    def _printTree(self, node):
        #print "current node",node.val
        if node is not None:
            #print "called by",node.val
            self._printTree(node.left)
            print str(node.val) + ' '
           # print "right child of",node.val,node.right.val
            self._printTree(node.right)
            
    def minimum(self,val):
        node = self.find(val)
        #print node.val
        #minval = 0
        if node is not None:
            #print "recursive call"
            return self._minimum(val,node)
            #print "came back from child process",minval
        else:
            #"in final else"
            return node
    def _minimum(self,val,node):
        minval = 0
        if node.left is not None:
            #print  "parent node value",node.val, node.left.val
            return self._minimum(val,node.left)
        else:
            #print "In else", "parent node value",node.val
            minval = node.val
            #print "minval",minval
            return minval
        #print "outside now",minval
    def maximum(self,val):
        #print "find max"
        node = self.find(val)
        if node.right is not None:
            return self._maximum(val,node)
        else:
            #print "no right node",node.val
            return node.val
    def _maximum(self,val,node):
        if node.right is not None:
            return self._maximum(val,node.right)
        else:
            return node.val
    def successor(self,val):
        node = self.find(val)
        if node is None:
            return None 
        elif node is not None and node.right is not None:
            return self._minimum(val,node.right)
        elif node.right is None:
            return self._successor(val,node,node.parent)
    def _successor(self,val,node,parent):
        
        if parent is None:
            return None
        elif parent.left is None :
            return self._successor(parent.val,parent,parent.parent)
        elif parent.left == node :
            #print "matched with left node"
            return parent.val
        elif parent.left <> node:
            return self._successor(parent.val,parent,parent.parent)
    def predecessor(self,val):
        node = self.find(val)
        if node is None:
            return None
        elif node.left is not None:
            return self._maximum(node.left.val,node.left)
        elif node.left is None and node <> node.parent.left:
            return node.parent.val
        else:
            return None
            
    #def transplant(T,u,v):
    
    def level_order_traversal(self,key=None):
        from copy import deepcopy
        if key is None:
            node = self.root
        else:
            node = Node(key)
        p_node = [node]
        level = [0]
        i = 0
        for x in p_node:
            if x is not None:
                if x.parent is not None:
                    #print "chekcing the traversal",x.val,"parent",x.parent.val
                    idx = p_node.index(x.parent) + 1
                    #print "parent info",x.parent.val,idx
                    nxtlevel = idx + 1
                else:
                    idx = 0
                    nxtlevel = 1
                    print "at root", idx, p_node[idx].val
                    temp = []
                if x.left is not None:
                    #print "left node exists"
                    p_node.append(x.left)
                    level.append(nxtlevel)
                if x.right is not None:
                    #print "right node exists","nextlevel",nxtlevel
                    p_node.append(x.right)
                    level.append(nxtlevel)
                # i keeps track of the element position in p_node
                #print "index",i, "level[i]",level[i],"curr node",x.val
                print level
                try:
                    if level[i] == level[i+1]:
                        #print "append"
                        temp.append(x.val)
                    else:
                            temp.append(x.val)
                            print [element for element in temp]
                            temp = []
                except IndexError:
                    temp.append(x.val)
                    print [element for element in temp]
                    temp = []
                    print "no more elements"
            i += 1
    def pre_order_traversal(self):
        if self.root is not None:
            self._pre_order_traversal(self.root)
    
    # The printTree is a inorder tree walk
    def _pre_order_traversal(self, node):
        #print "current node",node.val
        if node is not None:
            #print "called by",node.val
            print str(node.val) + ' '
            self._pre_order_traversal(node.left)
            
           # print "right child of",node.val,node.right.val
            self._pre_order_traversal(node.right)

""""
the graph is as below

            3
           / \
          0   4
         / \   \
       -1  2    8
          / \
         1   2.5
         
"""

tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(-1)
tree.add(8)
tree.add(2)
tree.add(2.5)
tree.add(1)
tree.printTree()
print tree.root.val
#print (tree.find(-1)).val
print "find 2",(tree.find(2)).parent.val
#print tree.minimum(4)
#print tree.maximum(0)
print "predecessor",tree.predecessor(-1)
tree.delete_node(4)
#tree.printTree()
tree.level_order_traversal()
tree.find(100)
tree.pre_order_traversal()
#print "successor",tree.successor(8)
        
            
      
    
