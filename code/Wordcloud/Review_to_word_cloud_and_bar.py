#coding:utf-8
import os
import json
import numpy as np
import time
import datetime
from collections import defaultdict


os.chdir("D:\\WISC\\stat628\\Module3\\Stat628_Module3_Group11")
print(os.getcwd())
dataset_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset")
save_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset_Bubble_Tea")
review_save_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset_review")

## Subword tokenization
vo_1_star = defaultdict(int)
vo_2_star = defaultdict(int)
vo_3_star = defaultdict(int)
vo_4_star = defaultdict(int)
vo_5_star = defaultdict(int)

for i in range(5):
    save_file = str(i+1) + "stars.txt"

    with open(os.path.join(review_save_path, "%s" % save_file), "r", encoding="UTF-8") as f:
        line = f.__next__()
        save_dict = json.loads(line)
        exec("vo_%s_star = save_dict" % (i + 1))


import wordcloud
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stopword = stopwords.words('english')
english_punctuations_and_filter_words = [',','.',':',';','?','(',')','[',']','&','!','*','@','#','$','%','\'', '\"','/','-','\\',
                        'get', 'got', 'back', 'ordered', 'tea','teas','also','drink','drinks','order', 'and'
                        'take','took']
[stopword.append(_) for _ in english_punctuations_and_filter_words]

# Delete the stopwords and punctuations

count = [0 for _ in range(5)]
words_count = [0 for _ in range(5)]
for i in range(5):
    new_dict = {}
    exec("save_dict = vo_%s_star" % (i + 1))
    for key in save_dict.keys():
        count[i] += 1
        if key in stopword:
            continue
        new_dict[key] = save_dict[key]
        words_count[i] += save_dict[key]

    exec("vo_%s_star = new_dict" % (i + 1))

# Form a total word frequency
total_dict = defaultdict(int)

for i in range(5):
    exec("save_dict = vo_%s_star" % (i + 1))
    for key in save_dict.keys():
        if key in stopword:
            continue
        total_dict[key] += save_dict[key]

total_word = 0
for key in total_dict.keys():
    total_word += 1

# Function of drawing a wordcloud.
def draw_wordcloud(word_freq, pic_name, input_pic):
    backgroud_Image = plt.imread(input_pic)


    wc = wordcloud.WordCloud(background_color='white',# 设置背景颜色
                             mask=backgroud_Image,
                             max_words=2000,
                             max_font_size=150,  # 设置字体最大值
                             random_state=30
                             )

    wc.generate_from_frequencies(total_dict)
    img_colors = ImageColorGenerator(backgroud_Image)
    #字体颜色为背景图片的颜色
    wc.recolor(color_func=img_colors)
    plt.imshow(wc) # 显示词云
    plt.axis('off') # 关闭坐标轴
    plt.show() # 显示图像
    cur_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    wc.to_file("wordcloud_pic/" + pic_name + cur_time + ".jpg")
    print("Finished writing wordcloud %s"%pic_name)

draw_wordcloud(total_dict, "word_freq", "wordcloud.jpg")
draw_wordcloud(vo_1_star, "vo_1_star", "thumbs_down.jpg")
draw_wordcloud(vo_5_star, "vo_5_star", "thumbs_up.jpg")

## tf-idf

idf_vo_1_star = defaultdict(int)
idf_vo_2_star = defaultdict(int)
idf_vo_3_star = defaultdict(int)
idf_vo_4_star = defaultdict(int)
idf_vo_5_star = defaultdict(int)

for i in range(5):
    save_file = str(i+1) + "stars_idf.txt"

    with open(os.path.join(review_save_path, "%s" % save_file), "r", encoding="UTF-8") as f:
        line = f.__next__()
        save_dict = json.loads(line)
        exec("idf_vo_%s_star = save_dict" % (i + 1))

with open(os.path.join(review_save_path, "count_sentences.txt"), "r", encoding="utf-8") as f:
    line = f.__next__()
    count_sentences_dict = json.loads(line)
count_sentences = []
for i in range(5):
    count_sentences.append(count_sentences_dict[str(i+1)])

for i in range(5):
    new_dict = {}
    exec("save_dict = idf_vo_%s_star" % (i + 1))
    for key in save_dict.keys():
        count[i] += 1
        if key in stopword:
            continue
        new_dict[key] = save_dict[key]

    exec("idf_vo_%s_star = new_dict" % (i + 1))


idf_total_dict = defaultdict(int)
for i in range(5):
    exec("save_dict = vo_%s_star" % (i + 1))
    for key in save_dict.keys():
        if key in stopword:
            continue
        idf_total_dict[key] += save_dict[key]

import math
# Calculate the tf-idf
# count_sentences: idf sentences count, count: word count


tf_idf_vo_1_star = defaultdict(int)
tf_idf_vo_2_star = defaultdict(int)
tf_idf_vo_3_star = defaultdict(int)
tf_idf_vo_4_star = defaultdict(int)
tf_idf_vo_5_star = defaultdict(int)

for i in range(5):
    new_dict = {}
    exec("save_dict = vo_%s_star" % (i + 1))
    exec("idf_save_dict = defaultdict(int,idf_vo_%s_star)" % (i + 1))
    for key in save_dict.keys():
        new_dict[key] = save_dict[key]/count[i] * math.log10(sum(count_sentences)/(1+idf_save_dict[key]))

    exec("tf_idf_vo_%s_star = new_dict" % (i + 1))

draw_wordcloud(tf_idf_vo_1_star, "tf_idf_vo_1_star", "thumbs_down.jpg")
draw_wordcloud(tf_idf_vo_5_star, "tf_idf_vo_5_star", "thumbs_up.jpg")

for i in range(5):
    save_file = str(i + 1) + 'stars_tf_idf.txt'
    exec("save_dict = tf_idf_vo_%s_star" % (i + 1))
    with open(os.path.join(review_save_path, "%s" % save_file), "w", encoding="utf-8") as wf:
        wf.write(json.dumps(save_dict))

## Draw the bar/hist
def draw_hist_tfidf(word):
    freq_height = [tf_idf_vo_1_star[word]]
    freq_height.append(tf_idf_vo_2_star[word])
    freq_height.append(tf_idf_vo_3_star[word])
    freq_height.append(tf_idf_vo_4_star[word])
    freq_height.append(tf_idf_vo_5_star[word])
    print(freq_height)
    plt.bar([1,2,3,4,5],freq_height)
    plt.xlabel("Ratings")
    plt.ylabel("tf-idf")
    plt.title(word)

def draw_hist_tf(word):
    freq_height = [vo_1_star[word]]
    freq_height.append(vo_2_star[word])
    freq_height.append(vo_3_star[word])
    freq_height.append(vo_4_star[word])
    freq_height.append(vo_5_star[word])
    print(freq_height)
    plt.bar([1,2,3,4,5],freq_height)
    plt.xlabel("Ratings")
    plt.ylabel("tf")
    plt.title(word)

def draw_hist(words):
    freq_height_tfidf = [0 for _ in range(5)]
    freq_height_tfidf[0] = tf_idf_vo_1_star[word]
    freq_height_tfidf[1] = tf_idf_vo_2_star[word]
    freq_height_tfidf[2] = tf_idf_vo_3_star[word]
    freq_height_tfidf[3] = tf_idf_vo_4_star[word]
    freq_height_tfidf[4] = tf_idf_vo_5_star[word]
    freq_height = [vo_1_star[word]/words_count[0]]
    freq_height.append(vo_2_star[word]/words_count[1])
    freq_height.append(vo_3_star[word]/words_count[2])
    freq_height.append(vo_4_star[word]/words_count[3])
    freq_height.append(vo_5_star[word]/words_count[4])
    print(freq_height)
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    p1 = ax1.bar([1, 3, 5, 7, 9], freq_height,color='lightseagreen', label = "Term frequency",align='edge')
    ax1.set_ylabel("Term frequency")
    p2 = ax2.bar([2, 4, 6, 8, 10], freq_height_tfidf, label="TF-IDF",align='edge')
    ax2.set_ylabel("TF-IDF")
    plt.xticks([2,4,6,8,10], [1,2,3,4,5])
    plt.tight_layout()
    plt.legend(handles = [p1,p2])
    plt.xlabel("Ratings")
    plt.title(word)


word_list = ['cold','hot', 'sweetness', 'ice', 'service', 'bad', 'loud', 'quiet', 'noise', 'to','go', 'dessert', 'dumpling', 'affordable', 'snack',
             'bubble','boba','comfortable','music','worse','friendly','unfriendly','friend','familiar','sugar','toppings',
             'topping','##able','un','##ly','taro','coconut','cheap','expensive','environment','coconut','couples','delivery','food',
             'coffee','sweet','bitter','ever','dine','ingredients','wait','time','money','never','location','delicious','app','fresh','milk','milks']
word_list.sort()

for word in word_list:
    try:
        draw_hist(word)
        plt.savefig("wordcloud_pic/freq_pic/" + word +".jpg", dpi=600, bbox_inches = 'tight')
    except Exception as e:
        print(e)
from collections import Counter

most_common = Counter(total_dict).most_common()

with open("most_common_words.txt", "w", encoding="UTF-8") as f:
    for common in most_common[:300]:
        f.write(common[0] + ': ' + str(common[1])+ "\n")