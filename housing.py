import os
import tarfile
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from six.moves import urllib
from zlib import crc32
from sklearn.model_selection import StratifiedShuffleSplit

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetchHousingData(housingUrl=HOUSING_URL, housingPath=HOUSING_PATH):
    if not os.path.isdir(housingPath):
        os.makedirs(housingPath)
    tgzPath = os.path.join(housingPath, "housing.tgz")
    urllib.request.urlretrieve(housingUrl, tgzPath)
    housingTgz=tarfile.open(tgzPath)
    housingTgz.extractall(path=housingPath)
    housingTgz.close()
    
def loadHousingData(housingPath=HOUSING_PATH):
    csv_path = os.path.join(housingPath, "housing.csv")
    return pd.read_csv(csv_path)

def splitTrainTest(data, testRatio):
    shuffledIndices = np.random.permutation(len(data))
    testSetSize = int(len(data)*testRatio)
    testIndices = shuffledIndices[:testSetSize]
    trainIndices = shuffledIndices[testSetSize:]
    return data.iloc[trainIndices], data.iloc[test_indices]

def testSetCheck(identifier, testRatio):
    return crc32(np.int64(identifier)) & 0xffffffff < testRatio * 2**32

def splitTrainTestById(data, testRatio, idColumn):
    ids = data[idColumn]
    inTestSet = ids.apply(lambda id_:testSetCheck(id_, testRatio))
    return data.loc[~inTestSet], data.loc[inTestSet]
    
#fetchHousingData()
housing = loadHousingData()

housing["income_cat"] = pd.cut(housing["median_income"],
 bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
 labels=[1, 2, 3, 4, 5])

split = StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)
for trainIndex, testIndex in split.split(housing, housing["income_cat"]):
    stratTrainSet = housing.loc[trainIndex]
    stratTestSet= housing.loc[testIndex]
    
#housing["income_cat"].hist()
#housing.hist(bins=50, figsize=(20,15))    
#print(housing.head())
#print(housing.info())
#print(housing.describe())
#plt.show()
