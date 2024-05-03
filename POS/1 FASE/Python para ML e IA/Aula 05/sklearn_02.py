from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier

# Pipeline com escalonamento, redução de dimensionalidade e classificação
pipeline = Pipeline([
    ('scaler', StandardScaler())
    ('pca', PCA(n_components=3))
    ('classifier', RandomForestClassifier())
])

# Treinando o modelo e fazendo previsão
pipeline.fit(X_train, y_train)
prediction = pipeline.predict(X_test)