def solution(A):
  m = max(A)
  if m < 1:
    return 1
  A = set(A)
  B = set(range(1,m+1))
  C = B-A
  if len(C) == 0:
    return m+1
  else:
    return min(C)

print(solution([1,3,6,4,1,2]))

  