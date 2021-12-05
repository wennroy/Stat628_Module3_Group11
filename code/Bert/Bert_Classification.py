import os

os.chdir("D:\\WISC\\stat628\\Module3\\Stat628_Module3_Group11")
print(os.getcwd())
dataset_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset")
save_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset_review_classification")

import tensorflow as tf
import tensorflow_hub as hub
from official.nlp import optimization
import tensorflow_text as text
from matplotlib import pyplot as plt

AUTOTUNE = tf.data.AUTOTUNE
batch_size = 32
seed = 628

raw_train_ds = tf.keras.utils.text_dataset_from_directory(
    save_path,
    batch_size = batch_size,
    validation_split = 0.2,
    subset = "training",
    seed = seed,
    )
class_names = raw_train_ds.class_names
train_ds = raw_train_ds.cache().prefetch(buffer_size=AUTOTUNE)

val_ds = tf.keras.utils.text_dataset_from_directory(
    save_path,
    batch_size = batch_size,
    validation_split = 0.2,
    subset = "validation",
    seed = seed)

val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

for text_batch, label_batch in train_ds.take(1):
  for i in range(3):
    print(f'Review: {text_batch.numpy()[i]}')
    label = label_batch.numpy()[i]
    print(f'Label : {label} ({class_names[label]})')

# bert_preprocess_model = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3")
bert_model_url = "D:/WISC/stat628/Module3/Stat628_Module3_Group11/code/Bert/small_bert_bert_en_uncased_L-2_H-128_A-2_2"
# bert_model = hub.load(bert_model_url)
preprocess_model_url = "D:/WISC/stat628/Module3/Stat628_Module3_Group11/code/Bert/bert_en_uncased_preprocess_3"

def build_classifier_model():
  text_input = tf.keras.layers.Input(shape=(), dtype=tf.string, name='text')
  preprocessing_layer = hub.KerasLayer(preprocess_model_url, name='preprocessing')
  encoder_inputs = preprocessing_layer(text_input)
  encoder = hub.KerasLayer(bert_model_url, trainable=True, name='BERT_encoder')
  outputs = encoder(encoder_inputs)
  net = outputs['pooled_output']
  net = tf.keras.layers.Dropout(0.1)(net)
  net = tf.keras.layers.Dense(100)(net)
  net = tf.keras.layers.Dense(1, activation=None, name='classifier')(net)
  return tf.keras.Model(text_input, net)


classifier_model = build_classifier_model()

# loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
# metrics = [tf.keras.metrics.SparseCategoricalAccuracy(name="accuracy")]

loss = tf.keras.losses.MeanSquaredError()
metrics = tf.keras.losses.MeanSquaredError()

epochs = 4
steps_per_epoch = tf.data.experimental.cardinality(train_ds).numpy()
num_train_steps = steps_per_epoch * epochs
num_warmup_steps = int(0.1*num_train_steps)

init_lr = 3e-4
optimizer = optimization.create_optimizer(init_lr=init_lr,
                                          num_train_steps=num_train_steps,
                                          num_warmup_steps=num_warmup_steps,
                                          optimizer_type='adamw')

classifier_model.compile(optimizer=optimizer,
                         loss=loss,
                         metrics=metrics)

print(f'Training model with {bert_model_url}')
history = classifier_model.fit(x=train_ds,
                               validation_data=val_ds,
                               epochs=epochs)
history_dict = history.history
print(history_dict.keys())

# acc = history_dict['accuracy']
# val_acc = history_dict['val_accuracy']
loss = history_dict['loss']
val_loss = history_dict['val_loss']

loss = [0.7899, 0.4795, 0.3810, 0.3415]
val_loss = [0.5445, 0.5255, 0.4958, 0.4957]

epochs = range(1, len(loss) + 1)
fig = plt.figure(figsize=(10, 6))
fig.tight_layout()

# plt.subplot(2, 1, 1)
# r is for "solid red line"
plt.plot(epochs, loss, 'r', label='Training loss')
# b is for "solid blue line"
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

# plt.subplot(2, 1, 2)
# plt.plot(epochs, acc, 'r', label='Training acc')
# plt.plot(epochs, val_acc, 'b', label='Validation acc')
# plt.title('Training and validation accuracy')
# plt.xlabel('Epochs')
# plt.ylabel('Accuracy')
# plt.legend(loc='lower right')

plt.show()

import datetime
dataset_name = 'yelp_mse_final'
saved_model_path = './code/Bert/Save_model/{}_bert_'.format(dataset_name.replace('/', '_') + datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
classifier_model.save(saved_model_path, include_optimizer=False)

'''
reloaded_model = tf.saved_model.load(saved_model_path)
def print_my_examples(inputs, results):
  result_for_printing = \
    [f'input: {inputs[i]:<30} : score: {results[i][0]:.6f}'
                         for i in range(len(inputs))]
  print(*result_for_printing, sep='\n')
  print()


examples = [
    'this is such an amazing movie!',  # this is the same sentence tried earlier
    'The movie was great!',
    'The movie was meh.',
    'The movie was okish.',
    'The movie was terrible...'
]

reloaded_results = tf.sigmoid(reloaded_model(tf.constant(examples)))
original_results = tf.sigmoid(classifier_model(tf.constant(examples)))

print('Results from the saved model:')
print_my_examples(examples, reloaded_results)
print('Results from the model in memory:')
print_my_examples(examples, original_results)

serving_results = reloaded_model \
            .signatures['serving_default'](tf.constant(examples))

serving_results = tf.sigmoid(serving_results['classifier'])

print_my_examples(examples, serving_results)
'''