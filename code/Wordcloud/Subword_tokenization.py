#coding:utf-8
import os
import json

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

## Form the frequency table for vocabulary
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

new_dict = {}
for i in range(5):
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
    save_dict = new_dict

## Write into files. 1stars.txt - 5stars.txt

for i in range(5):
    save_file = str(i + 1) + 'stars.txt'
    exec("save_dict = vo_%s_star" % (i + 1))
    with open(os.path.join(review_save_path, "%s" % save_file), "w", encoding="utf-8") as wf:
        wf.write(json.dumps(save_dict))


