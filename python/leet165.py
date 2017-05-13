class Solution(object):
    def compareVersion(self, version1, version2):
        """
        165. Compare Version Numbers
        :type version1: str
        :type version2: str
        :rtype: int
        
        Compare two version numbers version1 and version2.
        If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
        """
        
        ver_list1 = version1.split('.')
        ver_list2 = version2.split('.')
        
        
        
        len1 = len(ver_list1)
        len2 = len(ver_list2)
        
        
        if len1 > 1:
            while int(ver_list1[-1]) == 0:
                ver_list1.pop()
            len1 = len(ver_list1)
        if len2 > 1:
            while int(ver_list2[-1]) == 0:
                ver_list2.pop()
            len2 = len(ver_list2)
            
        
        for item1, item2 in zip(ver_list1, ver_list2):
            
            if int(item1) < int(item2):
                return -1
            elif int(item1) > int(item2):
                return 1
        
        
        
        if len1 > len2:
            return 1
        elif len1 < len2:
            return -1
        else:
            return 0
                
