


from sklearn.model_selection import GridSearchCV

#Definindo os parâmetros a serem testados
param_grid = {
    'classifier__n_estimators': [50,100,200]
    ,'classifier__max_depth' : [None, 10, 20]
}

#Criando um objeto GridSearchCV
grid_search = GridSearchCV(estimator=pipeline,
                           param_grid=param_grid, cv=5)


grid_search.fit(X_train, y_train)

best_params = grid_search.best_params_