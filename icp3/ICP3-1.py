import numpy as np
A = np.random.choice(range(1,21),15,replace=False)
print("Original array:")
print(A)
A[A.argmax()] = 0
print("Maximum value replaced by 0:")
print(A)