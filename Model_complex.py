import tensorflow as tf
from tensorflow import keras
from keras import layers

model = keras.Sequential(
    [
        layers.InputLayer(input_shape=(1,), dtype=tf.string),
        layers.TextVectorization(output_mode="int"),
        layers.Embedding(input_dim=1000, output_dim=64),
        layers.Bidirectional(layers.LSTM(64)),
    ]
)

model2 = keras.Sequential(
    [
        layers.InputLayer(input_shape=(1,), dtype=tf.string),
        layers.TextVectorization(output_mode="int", ngrams=2),
        layers.Embedding(input_dim=1000, output_dim=64),
        layers.Bidirectional(layers.LSTM(64)),
    ]
)

combined = layers.concatenate([model.output, model2.output])

output_layer = layers.Dense(5)(combined)

model3 = keras.Model(inputs=[model.input, model2.input], outputs=output_layer)

model3.compile(optimizer=tf.keras.optimizers.Adam(0.01), loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True), metrics=["accuracy"])

model4 = keras.Sequential(
    [
        layers.InputLayer(input_shape=(1,), dtype=tf.string),
        layers.TextVectorization(output_mode="int", ngrams=3),
        layers.Embedding(input_dim=1000, output_dim=64),
        layers.Bidirectional(layers.LSTM(64)),
    ]
)

combined2 = layers.concatenate([combined, model4.output])

output_layer2 = layers.Dense(5)(combined2)

model5 = keras.Model(inputs=[model.input, model2.input, model4.input], outputs=output_layer2)

model5.compile(optimizer=tf.keras.optimizers.Adam(0.01), loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True), metrics=["accuracy"])
model5.summary()
opt = tf.keras.optimizers.Adam(learning_rate=0.001)
loss_fn = tf.keras.losses.CategoricalCrossentropy(from_logits=True)
acc_metric = tf.keras.metrics.CategoricalAccuracy()

