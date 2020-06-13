def solution(A,N):
  counters = [0] * N
  max_i = 0
  for x in A:
    if 1 <= x <=N:
      counters[x-1] += 1
      if counters[x-1] > max_i:
        max_i = counters[x-1]
      
    else:
        counters = [max_i] * N

  return counters

print (solution([3,4,4,6,1,4,4],5)) 