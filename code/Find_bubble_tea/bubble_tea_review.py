import os
import json
from collections import defaultdict
import csv

os.chdir("D:\\WISC\\stat628\\Module3\\Stat628_Module3_Group11")
print(os.getcwd())
dataset_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset")
save_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset_Bubble_Tea")
review_save_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset_review")


rating_dict = defaultdict(int)

for file_name in os.listdir(review_save_path):
    if os.path.isfile(os.path.join(review_save_path, "%s" % file_name)):
        os.remove(os.path.join(review_save_path, "%s" % file_name))

file_name = "review.json"

with open(os.path.join(save_path, "bubble_tea_%s" % file_name), 'r', encoding="utf-8") as f:
    for line in f:
        dict_json = json.loads(line)
        sentence = dict_json["text"]
        sentence = sentence.replace("\n"," ")
        # print(sentence)
        rating = round(float(dict_json["stars"]))

        save_file = str(rating) + ".txt"
        with open(os.path.join(review_save_path, "%s" % save_file), "a", encoding="utf-8") as wf:
            wf.write(sentence + "\n")
        rating_dict[str(rating)] += 1

print(rating_dict)

'''
Great spot. Comfortable little joint smack dab in the middle of Harvard Square. Drop in on a hot day and grab a bubble tea while shootin' the breeze with the staff. You can also challenge Harvard students to a game of Street Fighter 2 if you feel the need, but personally I like to just relax and keep the peace. 

The only place that rivals this is a bubble tea shop in Calgary that I walked into awkwardly while they were still under construction. They told me to come back in and gave me a free bubble tea though so they are scoring points stricly on being nice and not charging anything (I still tipped though, I'm not a scumbag.) 

Boston Tea Stop (clever name especially with the MBTA map on the wall) is a valuable addition to the ever diminishing Harvard Square area. Pretty soon that neighborhood will be nothing but boring chain restaurants and mediocre bars so try and support the little guys while you can. 

Also the staff deserves a shout-out. They can talk about the Rival Mob with the best of them.

# Make sure there are only integer on ratings.
with open(os.path.join(save_path, "bubble_tea_%s" % file_name), 'r', encoding="utf-8") as f:
    for line in f:
        dict_json = json.loads(line)
        sentence = dict_json["text"]
        sentence = sentence.replace("\n"," ")
        # print(sentence)
        rating = float(dict_json["stars"])
        if rating == 5 or rating == 4 or rating == 3 or rating == 2 or rating == 1:
            continue
        print(rating)
'''