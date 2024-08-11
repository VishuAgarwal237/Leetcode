def solution(operations):

  res = ""
  arr = [False] * N
  for op in operations:

    if op[0] == 1:
      arr[op[1]] = True
    if op[0] == 2:
      for i in range(op[1] - op[2], op[1]+1):
        
        