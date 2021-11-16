#coding:utf-8
import os
import json
import pathlib

os.chdir("D:\\WISC\\stat628\\Module3\\Stat628_Module3_Group11")
print(os.getcwd())
dataset_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset")
save_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset_Bubble_Tea")
review_save_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset_review")

import tensorflow as tf

data_sets = []

for i in range(5):
    file_name = str(i + 1) + ".txt"
    lines_dataset = tf.data.TextLineDataset(os.path.join(review_save_path, file_name))
    dataset = lines_dataset.map(lambda ex: ex)
    data_sets.append(dataset)

BUFFER_SIZE = 50000
# BATCH_SIZE = 64
# TAKE_SIZE = 5000

_all_data = data_sets[0]
for labeled_dataset in data_sets[1:]:
    _all_data = _all_data.concatenate(labeled_dataset)

_all_data = _all_data.shuffle(
    BUFFER_SIZE, reshuffle_each_iteration=False)

from tensorflow_text.tools.wordpiece_vocab import bert_vocab_from_dataset as bert_vocab
from collections import defaultdict

bert_tokenizer_params = dict(lower_case=True)
reserved_tokens = ["[PAD]", "[UNK]", "[START]", "[END]"]

bert_vocab_args = dict(
    # The target vocabulary size
    vocab_size=10000,
    # Reserved tokens that must be included in the vocabulary
    reserved_tokens=reserved_tokens,
    # Arguments for `text.BertTokenizer`
    bert_tokenizer_params=bert_tokenizer_params,
    # Arguments for `wordpiece_vocab.wordpiece_tokenizer_learner_lib.learn`
    learn_params={},
)

print("Calculating vocab")

vocab = bert_vocab.bert_vocab_from_dataset(
    _all_data.batch(1000).prefetch(2),
    **bert_vocab_args
)


def write_vocab_file(filepath, vocab):
    with open(filepath, 'w', encoding="UTF-8") as f:
        for token in vocab:
            print(token, file=f)


write_vocab_file('Bubble_tea_vocab.txt', vocab)

print(len(vocab))


def labeler(example, index):
    return example, tf.cast(index, tf.int64)


data_sets = []
for i in range(5):
    file_name = str(i + 1) + ".txt"
    lines_dataset = tf.data.TextLineDataset(os.path.join(review_save_path, file_name))
    dataset = lines_dataset.map(lambda ex: labeler(ex, i + 1))
    data_sets.append(dataset)

BUFFER_SIZE = 50000
# BATCH_SIZE = 64
# TAKE_SIZE = 5000

all_data = data_sets[0]
for labeled_dataset in data_sets[1:]:
    all_data = all_data.concatenate(labeled_dataset)

all_data = all_data.shuffle(
    BUFFER_SIZE, reshuffle_each_iteration=False)

import tensorflow_text as text

Bubble_tea_tokenizer = text.BertTokenizer('Bubble_tea_vocab.txt', **bert_tokenizer_params)

# Take a look what's inside the tokenization
'''
token_sentence = []
words = []
sentences = []
txt_tokens = []
for examples in all_data.take(10):
    token_batch = Bubble_tea_tokenizer.tokenize(examples[0]).merge_dims(-2, -1)
    token_sentence.append(token_batch)
    words.append(Bubble_tea_tokenizer.detokenize(token_batch))
    txt_tokens.append(tf.gather(vocab, token_batch))
    sentences.append(examples[0])
    

vo_1_star = defaultdict(int)
vo_2_star = defaultdict(int)
vo_3_star = defaultdict(int)
vo_4_star = defaultdict(int)
vo_5_star = defaultdict(int)

## Form the frequency table for vocabulary Run about 1 hour.
count = 0
for examples in all_data:
    exec("save_dict = vo_%s_star" % (str(examples[1].numpy())))
    txt_token = tf.gather(vocab, Bubble_tea_tokenizer.tokenize(examples[0]).merge_dims(-2, -1))
    count += 1
    for words in txt_token:
        for word in words:
            save_dict[word.numpy()] += 1
    if count % 1000 == 0:
        print("Has read %s sentences." % count)
        print(txt_token)


## Bytes can not be written into file. Transform byte into str.


for i in range(5):
    new_dict = {}
    save_file = str(i + 1) + 'stars.txt'
    exec("save_dict = vo_%s_star" % (i + 1))
    print(i)
    for key in save_dict.keys():
        drop = save_dict[key]
        new_key = key
        try:
            new_key = str(key, encoding="utf-8")
        except Exception as e:
                print(e)
                print(key)
        finally:
            new_dict[new_key] = drop
    exec("vo_%s_star_str = new_dict" % (i + 1))

## Write into files. 1stars.txt - 5stars.txt

for i in range(5):
    save_file = str(i + 1) + 'stars.txt'
    exec("save_dict = vo_%s_star_str" % (i + 1))
    with open(os.path.join(review_save_path, "%s" % save_file), "w", encoding="utf-8") as wf:
        wf.write(json.dumps(save_dict))
'''
# START = tf.argmax(tf.constant(reserved_tokens) == "[START]")
# END = tf.argmax(tf.constant(reserved_tokens) == "[END]")
# def add_start_end(ragged):
#     count = ragged.bounding_shape()[0]
#     starts = tf.fill([count,1], START)
#     ends = tf.fill([count,1], END)
#     return tf.concat([starts, ragged, ends], axis=1)

'''
## Export the tf.module
print("Exporting the module")
class CustomTokenizer(tf.Module):
  def __init__(self, reserved_tokens, vocab_path):
    self.tokenizer = text.BertTokenizer(vocab_path, lower_case=True)
    self._reserved_tokens = reserved_tokens
    self._vocab_path = tf.saved_model.Asset(vocab_path)

    vocab = pathlib.Path(vocab_path).read_text().splitlines()
    self.vocab = tf.Variable(vocab)

    ## Create the signatures for export:

    # Include a tokenize signature for a batch of strings.
    self.tokenize.get_concrete_function(
        tf.TensorSpec(shape=[None], dtype=tf.string))

    # Include `detokenize` and `lookup` signatures for:
    #   * `Tensors` with shapes [tokens] and [batch, tokens]
    #   * `RaggedTensors` with shape [batch, tokens]
    self.detokenize.get_concrete_function(
        tf.TensorSpec(shape=[None, None], dtype=tf.int64))
    self.detokenize.get_concrete_function(
          tf.RaggedTensorSpec(shape=[None, None], dtype=tf.int64))

    self.lookup.get_concrete_function(
        tf.TensorSpec(shape=[None, None], dtype=tf.int64))
    self.lookup.get_concrete_function(
          tf.RaggedTensorSpec(shape=[None, None], dtype=tf.int64))

    # These `get_*` methods take no arguments
    self.get_vocab_size.get_concrete_function()
    self.get_vocab_path.get_concrete_function()
    self.get_reserved_tokens.get_concrete_function()

  @tf.function
  def tokenize(self, strings):
    enc = self.tokenizer.tokenize(strings)
    # Merge the `word` and `word-piece` axes.
    enc = enc.merge_dims(-2,-1)
    enc = add_start_end(enc)
    return enc

  @tf.function
  def detokenize(self, tokenized):
    words = self.tokenizer.detokenize(tokenized)
    return cleanup_text(self._reserved_tokens, words)

  @tf.function
  def lookup(self, token_ids):
    return tf.gather(self.vocab, token_ids)

  @tf.function
  def get_vocab_size(self):
    return tf.shape(self.vocab)[0]

  @tf.function
  def get_vocab_path(self):
    return self._vocab_path

  @tf.function
  def get_reserved_tokens(self):
    return tf.constant(self._reserved_tokens)

tokenizers = tf.Module()
tokenizers.en = CustomTokenizer(reserved_tokens, 'Bubble_tea_vocab.txt')
model_name = 'Bubble_tea'
tf.saved_model.save(tokenizers, model_name)
'''

## Subword tokenization idf calculate


idf_vo_1_star = defaultdict(int)
idf_vo_2_star = defaultdict(int)
idf_vo_3_star = defaultdict(int)
idf_vo_4_star = defaultdict(int)
idf_vo_5_star = defaultdict(int)

## Form the frequency table for vocabulary Run about 1 hour.

count_sentences = []
[count_sentences.append(0) for _ in range(5)]

print("idf frequency table")
count = 0
for examples in all_data:
    temp_dict = defaultdict(int)
    exec("save_dict = idf_vo_%s_star" % (str(examples[1].numpy())))
    exec("count_sentences[%s] += 1" % (str(examples[1].numpy()-1)))
    txt_token = tf.gather(vocab, Bubble_tea_tokenizer.tokenize(examples[0]).merge_dims(-2, -1))
    count += 1
    for words in txt_token:
        for word in words:
            temp_dict[word.numpy()] += 1
    for key in temp_dict.keys():
        save_dict[key] += 1

    if count % 1000 == 0:
        print("Has read %s sentences." % count)
        print(txt_token)



for i in range(5):
    new_dict = {}
    # save_file = str(i + 1) + 'stars_idf.txt'
    exec("save_dict = idf_vo_%s_star" % (i + 1))
    print(i)
    for key in save_dict.keys():
        drop = save_dict[key]
        new_key = key
        try:
            new_key = str(key, encoding="utf-8")
        except Exception as e:
                print(e)
                print(key)

        new_dict[new_key] = drop

    exec("idf_vo_%s_star_str = new_dict" % (i + 1))

## Write into files. 1stars.txt - 5stars.txt

for i in range(5):
    save_file = str(i + 1) + 'stars_idf.txt'
    exec("save_dict = idf_vo_%s_star_str" % (i + 1))
    with open(os.path.join(review_save_path, "%s" % save_file), "w", encoding="utf-8") as wf:
        wf.write(json.dumps(save_dict))

count_dict = {}
for i in range(5):
    count_dict[i+1] = count_sentences[i]
with open(os.path.join(review_save_path, "count_sentences.txt"), "w", encoding="utf-8") as f:
    f.write(json.dumps(count_dict))

