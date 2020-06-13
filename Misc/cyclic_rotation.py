# Given an array A and an integer K , Rotate the elements of array to right till /# K cycle

def rotation(A,K):
  result = [0] * len(A)
  for i in range(len (A)):
    result[(i+K) % len(A)] = A[i]
  return result

print(rotation([1,2,3,4,5],3))

