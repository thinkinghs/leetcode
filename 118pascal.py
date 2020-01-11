# https://leetcode.com/problems/pascals-triangle/solution/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        
        output = list()
        output.append([1])
        output.append([1,1])
        node = [1,1]

        for i in range(numRows-2):
            new_node = list()
            new_node.append(1)
            for e in range(1,len(node)):
                new_node.append(node[e-1] + node[e])
            new_node.append(1)

            node = new_node
            output.append(new_node)

        return output
