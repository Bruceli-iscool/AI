import os
import tarfile
import pandas as pd
import matplotlib.pyplot as plt
from six.moves import urllib

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
#fetchHousingData()
housing = loadHousingData()
print(housing.head())
print(housing.info())
print(housing.describe())
housing.hist(bins=50, figsize=(20,15))
plt.show()
