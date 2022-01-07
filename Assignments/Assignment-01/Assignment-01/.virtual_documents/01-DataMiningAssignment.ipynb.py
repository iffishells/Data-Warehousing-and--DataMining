# importing requried lib
import numpy as np
import math



# Reaiding file
data = open('sample-data.txt' , 'r' ,encoding='utf-8') 
data.readline()

for line in data.readlines():
    print(line.strip('\n'))
    


from collections import  Counter
class Node:
    def __init__(self,node,count=0):
        self.node = node
        self.count = count
        
class webMining:
    
    def __init__(self,data):
        self.data = data
        
    def count_table(self):
        
        distinct_count_element = { }
        
        for line in self.data.readlines():
            list_line = line.strip("\n").strip(" ").split(" ")
            
            print(list_line)
            key = Counter(list_line).keys()
            value = Counter(list_line).values()
            x = tuple(zip(key,value))
            print(x)
    
            
                
    
                   
    def distinct_element_count(self):
        
        distinct_element = []
        for line in data.readlines():
#             print(line)
            list_line = line.strip("\n").strip(" ").split(" ")
            for node in list_line:
                if node not in distinct_element:
                    distinct_element.append(node)
                    
#         print("Total Dbistinct elements : ",len(distinct_element))
        
        return distinct_element
    
        

    
    
if __name__ == '__main__':
    # Reaiding file
    data = open('sample-data.txt' , 'r' ,encoding='utf-8')
#     data = open('dataset WUM.txt' , 'r' ,encoding='utf-8')
    
#     data.readline()

#     for line in data.readlines():
#         print(line.strip('\n'))
    
    
    
    
    web_object = webMining(data)
#     web_object.distinct_element_count()
    web_object.count_table()


from collections import Counter

words = ['a', 'b', 'c', 'a']
words_1 = ['a', 'b', 'd', 'c']

a = list(Counter(words).keys()) # equals to list(set(words))
b = list(Counter(words).values()) # counts the elements' frequency

c = list(Counter(words_1).keys()) # equals to list(set(words))
d = list(Counter(words_1).values()) # counts the elements' frequency


y = a+c
print(" y ",y)
z = b+d
print(" z ",z)
x = zip(y,z)
print(tuple(x))


val = [1,23]
val2 = [2,4]
x =  val + val2
print(x)




from collections import Counter
from collections import defaultdict
from csv import reader
from collections import defaultdict
from itertools import chain, combinations

class Node:
    def __init__(self, itemName, frequency, parentNode):
        self.itemName = itemName
        self.count = frequency
        self.parent = parentNode
        self.children = {}
        self.next = None

    def increment(self, frequency):
        self.count += frequency

    def display(self, ind=1):
        print('  ' * ind, self.itemName, ' ', self.count)
        for child in list(self.children.values()):
            child.display(ind+1)

def getFromFile(fname):
    itemSetList = []
    frequency = []
    
    with open(fname, 'r') as file:
        csv_reader = reader(file)
        for line in csv_reader:
            line = list(filter(None, line))
            itemSetList.append(line)
            frequency.append(1)

    return itemSetList, frequency

def constructTree(itemSetList, frequency, minSup):
    headerTable = defaultdict(int)
    # Counting frequency and create header table
    for idx, itemSet in enumerate(itemSetList):
        for item in itemSet:
            headerTable[item] += frequency[idx]

    # Deleting items below minSup
    headerTable = dict((item, sup) for item, sup in headerTable.items() if sup >= minSup)
    if(len(headerTable) == 0):
        return None, None

    # HeaderTable column [Item: [frequency, headNode]]
    for item in headerTable:
        headerTable[item] = [headerTable[item], None]

    # Init Null head node
    fpTree = Node('Null', 1, None)
    # Update FP tree for each cleaned and sorted itemSet
    for idx, itemSet in enumerate(itemSetList):
        itemSet = [item for item in itemSet if item in headerTable]
        itemSet.sort(key=lambda item: headerTable[item][0], reverse=True)
        # Traverse from root to leaf, update tree with given item
        currentNode = fpTree
        for item in itemSet:
            currentNode = updateTree(item, currentNode, headerTable, frequency[idx])

    return fpTree, headerTable

def updateHeaderTable(item, targetNode, headerTable):
    if(headerTable[item][1] == None):
        headerTable[item][1] = targetNode
    else:
        currentNode = headerTable[item][1]
        # Traverse to the last node then link it to the target
        while currentNode.next get_ipython().getoutput("= None:")
            currentNode = currentNode.next
        currentNode.next = targetNode

def updateTree(item, treeNode, headerTable, frequency):
    if item in treeNode.children:
        # If the item already exists, increment the count
        treeNode.children[item].increment(frequency)
    else:
        # Create a new branch
        newItemNode = Node(item, frequency, treeNode)
        treeNode.children[item] = newItemNode
        # Link the new branch to header table
        updateHeaderTable(item, newItemNode, headerTable)

    return treeNode.children[item]

def ascendFPtree(node, prefixPath):
    if node.parent get_ipython().getoutput("= None:")
        prefixPath.append(node.itemName)
        ascendFPtree(node.parent, prefixPath)

def findPrefixPath(basePat, headerTable):
    # First node in linked list
    treeNode = headerTable[basePat][1] 
    condPats = []
    frequency = []
    while treeNode get_ipython().getoutput("= None:")
        prefixPath = []
        # From leaf node all the way to root
        ascendFPtree(treeNode, prefixPath)  
        if len(prefixPath) > 1:
            # Storing the prefix path and it's corresponding count
            condPats.append(prefixPath[1:])
            frequency.append(treeNode.count)

        # Go to next node
        treeNode = treeNode.next  
    return condPats, frequency

def mineTree(headerTable, minSup, preFix, freqItemList):
    # Sort the items with frequency and create a list
    sortedItemList = [item[0] for item in sorted(list(headerTable.items()), key=lambda p:p[1][0])] 
    # Start with the lowest frequency
    for item in sortedItemList:  
        # Pattern growth is achieved by the concatenation of suffix pattern with frequent patterns generated from conditional FP-tree
        newFreqSet = preFix.copy()
        newFreqSet.add(item)
        freqItemList.append(newFreqSet)
        # Find all prefix path, constrcut conditional pattern base
        conditionalPattBase, frequency = findPrefixPath(item, headerTable) 
        # Construct conditonal FP Tree with conditional pattern base
        conditionalTree, newHeaderTable = constructTree(conditionalPattBase, frequency, minSup) 
        if newHeaderTable get_ipython().getoutput("= None:")
            # Mining recursively on the tree
            mineTree(newHeaderTable, minSup,
                       newFreqSet, freqItemList)

def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)))

def getSupport(testSet, itemSetList):
    count = 0
    for itemSet in itemSetList:
        if(set(testSet).issubset(itemSet)):
            count += 1
    return count

def associationRule(freqItemSet, itemSetList, minConf):
    rules = []
    for itemSet in freqItemSet:
        subsets = powerset(itemSet)
        itemSetSup = getSupport(itemSet, itemSetList)
        for s in subsets:
            confidence = float(itemSetSup / getSupport(s, itemSetList))
            if(confidence > minConf):
                rules.append([set(s), set(itemSet.difference(s)), confidence])
    return rules

def getFrequencyFromList(itemSetList):
    frequency = [1 for i in range(len(itemSetList))]
    return frequency


def constructTree(itemSetList, frequency, minSup):
    headerTable = defaultdict(int)
    # Counting frequency and create header table
    for idx, itemSet in enumerate(itemSetList):
        for item in itemSet:
            headerTable[item] += frequency[idx]

    # Deleting items below minSup
    headerTable = dict((item, sup) for item, sup in headerTable.items() if sup >= minSup)
    if(len(headerTable) == 0):
        return None, None

    # HeaderTable column [Item: [frequency, headNode]]
    for item in headerTable:
        headerTable[item] = [headerTable[item], None]

    # Init Null head node
    fpTree = Node('Null', 1, None)
    # Update FP tree for each cleaned and sorted itemSet
    for idx, itemSet in enumerate(itemSetList):
        itemSet = [item for item in itemSet if item in headerTable]
        itemSet.sort(key=lambda item: headerTable[item][0], reverse=True)
        # Traverse from root to leaf, update tree with given item
        currentNode = fpTree
        for item in itemSet:
            currentNode = updateTree(item, currentNode, headerTable, frequency[idx])

    return fpTree, headerTable

def updateTree(item, treeNode, headerTable, frequency):
    if item in treeNode.children:
        # If the item already exists, increment the count
        treeNode.children[item].increment(frequency)
    else:
        # Create a new branch
        newItemNode = Node(item, frequency, treeNode)
        treeNode.children[item] = newItemNode
        # Link the new branch to header table
        updateHeaderTable(item, newItemNode, headerTable)

    return treeNode.children[item]

def updateHeaderTable(item, targetNode, headerTable):
    if(headerTable[item][1] == None):
        headerTable[item][1] = targetNode
    else:
        currentNode = headerTable[item][1]
        # Traverse to the last node then link it to the target
        while currentNode.next get_ipython().getoutput("= None:")
            currentNode = currentNode.next
        currentNode.next = targetNode
        

def mineTree(headerTable, minSup, preFix, freqItemList):
    # Sort the items with frequency and create a list
    sortedItemList = [item[0] for item in sorted(list(headerTable.items()), key=lambda p:p[1][0])] 
    # Start with the lowest frequency
    for item in sortedItemList:  
        # Pattern growth is achieved by the concatenation of suffix pattern with frequent patterns generated from conditional FP-tree
        newFreqSet = preFix.copy()
        newFreqSet.add(item)
        freqItemList.append(newFreqSet)
        # Find all prefix path, constrcut conditional pattern base
        conditionalPattBase, frequency = findPrefixPath(item, headerTable) 
        # Construct conditonal FP Tree with conditional pattern base
        conditionalTree, newHeaderTable = constructTree(conditionalPattBase, frequency, minSup) 
        if newHeaderTable get_ipython().getoutput("= None:")
            # Mining recursively on the tree
            mineTree(newHeaderTable, minSup,
                       newFreqSet, freqItemList)

def findPrefixPath(basePat, headerTable):
    # First node in linked list
    treeNode = headerTable[basePat][1] 
    condPats = []
    frequency = []
    while treeNode get_ipython().getoutput("= None:")
        prefixPath = []
        # From leaf node all the way to root
        ascendFPtree(treeNode, prefixPath)  
        if len(prefixPath) > 1:
            # Storing the prefix path and it's corresponding count
            condPats.append(prefixPath[1:])
            frequency.append(treeNode.count)

        # Go to next node
        treeNode = treeNode.next  
    return condPats, frequency

def ascendFPtree(node, prefixPath):
    if node.parent get_ipython().getoutput("= None:")
        prefixPath.append(node.itemName)
        ascendFPtree(node.parent, prefixPath)
        
        
def fpgrowthFromFile(fname, minSupRatio, minConf):
    itemSetList, frequency = fname
    minSup = len(itemSetList) * minSupRatio
    fpTree, headerTable = constructTree(itemSetList, frequency, minSup)

    freqItems = []
    mineTree(headerTable, minSup, set(), freqItems)
    rules = associationRule(freqItems, itemSetList, minConf)
    return freqItems, rules


# data = open('sample-data.txt' , 'r' ,encoding='utf-8')
data = open('dataset-WUM.txt' , 'r' ,encoding='utf-8')

list_of_item = []
for line in data.readlines():
        node_list = line.strip('\n').strip('').split(" ")
        for val in node_list:
            list_of_item.append(val)

itemset = list(Counter(list_of_item).keys())
freq = list(Counter(list_of_item).values())

# print("Total Itemset :\n",len(itemset))
# print("total Freq sum :\n",sum(freq))

# print("Itemset :\n",itemset)
# print("Freq :\n",freq)
# x = zip(itemset,freq)
# print(tuple(x))
# print("Total item set : ",len(list_of_item))


fpgrowthFromFile((itemset,freq),2,0.2)  


val1 ,val2 = (1,2)


val1


val2



