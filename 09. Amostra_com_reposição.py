import pandas as pd
import numpy as np

base = pd.read_csv('iris.csv') # ler o arquivo iris.cvv
# Amostra com reposição, se mudar para (falso) será uma amostra sem reposição
amostra = np.random.choice(a = [0, 1], size = 150, replace = True, 
                               p = [0.5, 0.5])     
# verifica o tamanho da amostrta
len(amostra) 

# Seleciona a quantidade de amostra com o value == 1 e 0
len(amostra[amostra == 1])
len(amostra[amostra == 0])
    