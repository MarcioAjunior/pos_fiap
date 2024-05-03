import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Criando um conjunto de dados de exemplo
np.random.seed(0)
X = np.random.rand(30, 2) * 10  # 30 amostras, 2 características

print(X)

# Visualizando os dados originais
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1])
plt.title("Dados Originais")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

# Aplicando o StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Visualizando os dados após o StandardScaler
plt.subplot(1, 2, 2)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1])
plt.title("Dados após StandardScaler")
plt.xlabel("Feature 1 (Padronizado)")
plt.ylabel("Feature 2 (Padronizado)")

plt.tight_layout()
plt.show()
