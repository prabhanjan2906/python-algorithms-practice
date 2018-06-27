from functools import reduce

def generate(numRows):
      if numRows == 0:
        return []
      tr = [[1]]

      def createPascalTr(a, b):
        tr[-1].append(a+b)
        return b

      for i in range (1, numRows):
        tr.append([1])
        reduce(createPascalTr, tr[i-1])
        tr[-1].append(1)
        
      print(tr)
generate(6)
