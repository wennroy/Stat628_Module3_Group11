#coding:utf-8
import os
import json
import numpy as np
from collections import defaultdict

os.chdir("D:\\WISC\\stat628\\Module3\\Stat628_Module3_Group11")
print(os.getcwd())
dataset_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset")
save_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset_Bubble_Tea")
review_save_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset_review")

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

import tensorflow_transform as tft

import wordcloud
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stopword = stopwords.words('english')
english_punctuations_and_filter_words = [',','.',':',';','?','(',')','[',']','&','!','*','@','#','$','%','\'', '\"',
                        'get', 'got', 'back', 'drink', 'ordered', 'tea','milk']
[stopword.append(_) for _ in english_punctuations_and_filter_words]

# Delete the stopwords and punctuations

count = [0 for _ in range(5)]
for i in range(5):
    new_dict = {}
    exec("save_dict = vo_%s_star" % (i + 1))
    for key in save_dict.keys():
        count[i] += 1
        if key in stopword:
            continue
        new_dict[key] = save_dict[key]

    exec("vo_%s_star = new_dict" % (i + 1))

# Form a total word frequency
total_dict = defaultdict(int)
for i in range(5):
    exec("save_dict = vo_%s_star" % (i + 1))
    for key in save_dict.keys():
        if key in stopword:
            continue
        total_dict[key] += save_dict[key]

# The total word frequency.
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

    wc.to_file(pic_name + ".jpg")
    print("Finished writing wordcloud %s"%pic_name)

draw_wordcloud(total_dict, "word_freq", "wordcloud.jpg")
draw_wordcloud(vo_1_star, "vo_1_star", "thumbs_down.jpg")
draw_wordcloud(total_dict, "vo_5_star", "thumbs_up.jpg")

