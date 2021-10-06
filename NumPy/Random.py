import numpy as  np
a=np.random.randint(100,150,(4,5))
print(a)
print("********************************")
print(a[0:4:2,0:5:1])



import numpy as np
arr=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
arr2=np.array([3,4,2,32,4,232,43,23])
print(arr.ndim)

print(arr.shape)
print(arr[0,1,0:2])
arr2.sort()
print(arr2)
print(np.sort(arr))
ran=np.random.randint(1,100,size=(3,5))
print("random",ran)


import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0,1,2,3,4,5,6],hist=False,kde=False)
plt.show()



from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10],kde=False) #kenrel density Estimation)

plt.show()


import numpy as np
arr1 = np.array([1,2,3,4,5,6,7])
print(arr1[::2])
arr = np.array([1, 2, 3, 4],dtype=float)
print(arr)