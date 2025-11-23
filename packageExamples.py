import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt
import pandas as pd

#numpy package example:
# numpy array:
x = np.array([[1,2,3],[4,5,6]])
print("x:\n{}".format(x))

#scipy package example:
#create numpy array:
eye = np.eye(4)
print("NumPy array:\n{}".format(eye))
# convert numpy array to scipy sparse matrix in csr format
sparseMatrix = sparse.csr_matrix(eye)
print("\nSciPy sparse CSR matrix:\n{}".format(sparseMatrix))
# same example but in coo format
data = np.ones(4)
rowIndices=np.arange(4)
colIndices= np.arange(4)
eyeCoo = sparse.coo_matrix((data, (rowIndices, colIndices)))
print("COO repersentation:\n{}".format(eyeCoo))

#matplotlib example:
x = np.linspace(-10,10,100)
y = np.sin(x)
plt.plot(x,y, marker="x")
plt.show()

#pandas example
data = {'Name':["John", "Anna", "Peter", "Linda"],
        'Location':["New York", "Paris","Berlin","London"],
        'Age':[24,13,53,33]
        }
dataPandas = pd.DataFrame(data)
print(dataPandas)
