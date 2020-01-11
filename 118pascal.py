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

    
    ''' best sollution
    class Solution:
    def generate(self, num_rows):
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle
    '''
