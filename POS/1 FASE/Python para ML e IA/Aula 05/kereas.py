from keras.models import Model
from keras.layers import Input, Dense, concatenate

#Definindo camadas persolaizadas
input_layer = Input(shape=(input_size))
dense_layer1 = Dense(64, activation='relu')(input_layer)
dense_layer2 = Dense(32, activation='relu')(input_layer)

#Conectando as camadas
concatenated_layer = concatenate([dense_layer1, dense_layer2])

#Camada de saída
output_layer = Dense(output_size, activation = 'softmax')(concatenated_layer)

#Criadno o modelo
custom_model = Model(inputs=[input_layer], outputs=output_layer)