import os
import shutil
import json
from sklearn.metrics import pairwise

os.chdir("D:\\WISC\\stat628\\Module3\\Stat628_Module3_Group11")
print(os.getcwd())
dataset_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset")
save_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset_Bubble_Tea")

import seaborn as sns
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text
from official.nlp import optimization

from matplotlib import pyplot as plt


'''
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=1.0)
config = tf.ConfigProto(gpu_options=gpu_options, allow_soft_placement=False, log_device_placement=False)
session = tf.Session(config=config)
'''

# Read from bubble_tea_review.json
file_name = "review.json"
sentences = []
with open(os.path.join(save_path, "bubble_tea_%s" % file_name), 'r', encoding="utf-8") as f:
    for i in range(5):
        line = f.__next__()
        dict_json = json.loads(line)
        sentences.append(dict_json["text"])

bert_preprocess_model = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3")
print("End preprocess")

bert_model_url = "D:/WISC/stat628/Module3/Stat628_Module3_Group11/code/Bert/small_bert_bert_en_uncased_L-2_H-128_A-2_2"
bert_model = hub.load(bert_model_url)

print("Here")

sentences.append("A partial solar eclipse occurs in the polar regions of the Earth when the center of the Moons shadow misses the Earth.")
sentences.append("A solar eclipse occurs when the Moon passes between Earth and the Sun, thereby totally or partly obscuring the image of the Sun for a viewer on Earth.")
inputs = bert_preprocess_model(sentences)
outputs = bert_model(inputs)

print("Sentences:")
print(sentences)

print("\nBERT inputs:")
print(inputs)

print("\nPooled embeddings:")
print(outputs["pooled_output"])

print("\nPer token embeddings:")
print(outputs["sequence_output"])

def plot_similarity(features, labels):
    """Plot a similarity matrix of the embeddings."""
    cos_sim = pairwise.cosine_similarity(features)
    sns.set(font_scale=1.2)
    cbar_kws=dict(use_gridspec=False, location="left")
    g = sns.heatmap(
      cos_sim, xticklabels=labels, yticklabels=labels,
      vmin=0, vmax=1, cmap="Blues", cbar_kws=cbar_kws)
    g.tick_params(labelright=True, labelleft=False)
    g.set_yticklabels(labels, rotation=0)
    g.set_title("Semantic Textual Similarity")
    plt.show()

plot_similarity(outputs["pooled_output"], sentences)

# BERT

