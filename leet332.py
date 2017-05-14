class Solution(object):
    '''
    Given a list of airline tickets represented by pairs of 
    departure and arrival airports [from, to], reconstruct 
    the itinerary in order. All of the tickets belong to a man 
    who departs from JFK. Thus, the itinerary must begin with JFK.

    '''
    def findItinerary(self, listAll):
        myDict = collections.defaultdict(list)
    
        for dep, tar in sorted(listAll)[::-1]:       
            myDict[dep] += tar,
    
        rList,traversePath = [], ['JFK']
    
        while traversePath:
        
        #traverse the tree
            while myDict[traversePath[-1]]:
                traversePath.append(myDict[traversePath[-1]].pop())

            rList.append(traversePath.pop())        
        return rList[::-1]
