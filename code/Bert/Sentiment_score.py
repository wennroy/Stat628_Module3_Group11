import os
import json
import sys
import shutil
import csv
import numpy as np

os.chdir("D:\\WISC\\stat628\\Module3\\Stat628_Module3_Group11")
print(os.getcwd())
dataset_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset_Bubble_Tea")
save_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset_business_review")

import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

dataset_name = 'yelp_mse_final'
saved_model_path = './code/Bert/Save_model/{}_bert_'.format(dataset_name.replace('/', '_') + '20211204-224451')
reloaded_model = tf.saved_model.load(saved_model_path)
classifier_model = reloaded_model
print("Loaded model %s" % (saved_model_path))
# examples = ["This is an awesome ice cream shop with an awesome staff. The place is clean and the ice cream and boba is superb. they even have a fruity pebbles flavor boba tea that one of the staff members created on accident!  This place is a true experience. I've never had ice cream like this and the staff really know what they're doing. It's perfect every time! the flavors are awesome! the strawberry cheesecake is my favorite. They chop up fresh strawberries and a slice of cheese cake and put it in the ice cream! It's awesome! I usually don't get strawberry flavored ice cream because I'm not too keen on the artificial taste, but there is nothing artificial about this taste. its freshly chopped strawberries!!  The shop is in an excellent location if you live in the west side of orlando or are on vacation at our local theme parks! Even if you do live a bit farther I would say it's well worth the trip.  This place is also incredibly service dog friendly! they always make me and my service dog feel welcomed! I will never go to another ice cream shop again, and i am an avid twistee treat lover.  I can't wait to try the food sometime!",
#             "Dumplings here are delish! The service was decent too. The chilli wontons and pork/chive dumplings were tasty. Note: if it's raining outside (which it often is in this town) the floors are very slippery. I stepped in and almost bailed on the tiles, then I watched a few others do the same.",
#             "I've been craving some bubble tea, so after dinner at Com we made our way over to indulge. I ordered the green tea bubble tea, which actually came out like a green tea milkshake, which I was a little unprepared for. It was almost a frappacino like consistency, but still pretty tasty.  We also perused the bakery and picked up some green tea sponge cake, and some white bean cakes, both were really light and not as sickeningly sweet as most pastries are.  Free wifi and huge booth seating are nice touches as well!",
#             "If you are Chinese, there is nothing worth coming for here. The dumplings are very americanized, their boba drinks are pitiful. At more than a dollar per dumpling, you can do better anywhere in Chinatown, or even buying a frozen bag at a grocery store for 1/4 of the cost.",
#             "I don't know what happened to this place, but the mochi was very stale when I visited. Also, the staff were really unfriendly, and I'm wondering since it's a cash only business -- is it a front for something illegal? Maybe the BBB should investigate them?"
#             ]
#
# results_examples = classifier_model(tf.constant(examples)) + 1
# print(results_examples)

interests = ["Tea_Types", "Tea_Ingredients", "Atmosphere", "Price", "Service", "Food"]

Tea_Types = [["green", "tea"], ["oolong", "tea"], ["black", "tea"], ["red", "tea"], ["matcha"], ["herbal"], ["jasmine"],
             ["taiwanese"]]
Tea_Ingredients = [["bubble"], ["boba"], ["rainbow"], ["taro"]]
Food = [["dessert"], ["cake"], ["tiramisu"], ["food"], ["drink"], ["coffee"]]
Atmosphere = [["environment"], ["atmosphere"], ["ambiance"], ["books"], ["noisy"], ["noise"]]
Price = [["price"]]
Service = [["service"],["open"],["close"], ["ceremony"]]


def find_words_in_review(review, words, tea=False):
    sentence_with_words = []
    sentences = []
    tokenized_sentences = []
    for single_review in review:
        for single_sentence in sent_tokenize(single_review.lower()):
            sentences.append(single_sentence)
            tokenized_sentences.append(word_tokenize(single_sentence))
    for sen_i, tokenized_sentence in enumerate(tokenized_sentences):
        for i, word in enumerate(tokenized_sentence):
            if word == words[0]:
                if tea:
                    if i == len(tokenized_sentence) - 1:
                        continue
                    elif not tokenized_sentence[i + 1] == words[1]:
                        continue
                sentence_with_words.append(sentences[sen_i])
                break
    # print("predicting...")
    if sentence_with_words == []:
        return -1, 0, 0, None
    # print("Lens of sentence with words %s"%(len(sentence_with_words)))
    ratings = classifier_model(tf.constant(sentence_with_words)) + 1  # tf type
    ratings = ratings.numpy()
    for i, rating in enumerate(ratings):
        if rating[0] > 5:
            print("Rating %f exceeds 5, adjust to 5." % (rating[0]))
            ratings[i] = [5]
        if rating[0] < 1:
            print("Rating %f belows 1, adjust to 1." % (rating[0]))
            ratings[i] = [1]
    return ratings.mean(), len(ratings), np.std(ratings), ratings

overall_name = "__Overall"
if not os.path.exists(os.path.join(save_path, overall_name)):
    os.mkdir(os.path.join(save_path, overall_name))
cur_overall_save_path = os.path.join(save_path, overall_name)


count = 0
all_ratings_Tea_Types = []
[all_ratings_Tea_Types.append([]) for _ in range(len(Tea_Types))]
all_ratings_Tea_Ingredients = []
[all_ratings_Tea_Ingredients.append([]) for _ in range(len(Tea_Ingredients))]
all_ratings_Atmosphere = []
[all_ratings_Atmosphere.append([]) for _ in range(len(Atmosphere))]
all_ratings_Price = []
[all_ratings_Price.append([]) for _ in range(len(Price))]
all_ratings_Service = []
[all_ratings_Service.append([]) for _ in range(len(Service))]
all_ratings_Food = []
[all_ratings_Food.append([]) for _ in range(len(Food))]
with open(os.path.join(dataset_path, "bubble_tea_business_id.txt"), "r", encoding="utf-8") as business_f:
    for business_name in business_f:
        count += 1
        business_name = business_name[:-1]
        print("Current Business id is %s" % (business_name))
        if count % 50 == 0:
            print("Finished %s businesses" % (count))
        if not os.path.exists(os.path.join(save_path, business_name)):
            os.mkdir(os.path.join(save_path, business_name))
        cur_save_path = os.path.join(save_path, business_name)
        for interest in interests:
            file_name = str(interest)
            col_name = []
            avg_all_ratings = []
            n_all_ratings = []
            std_all_ratings = []
            temp_ratings = []
            for words in eval(interest):
                if len(words) == 2:
                    col_name.append(words[0] + "_" + words[1])
                else:
                    col_name.append(words[0])
                all_reviews = []
                with open(os.path.join(dataset_path, "bubble_tea_review.json"), "r", encoding="utf-8") as review_f:
                    for review_json in review_f:
                        dict_json = json.loads(review_json)
                        if not dict_json["business_id"] == business_name:
                            continue
                        all_reviews.append(dict_json["text"])
                avg_rating, n_ratings, std_ratings, ratings = find_words_in_review(all_reviews, words, tea=len(words) == 2)
                avg_all_ratings.append(avg_rating)
                n_all_ratings.append(n_ratings)
                std_all_ratings.append(std_ratings)
                if ratings is None:
                    temp_ratings.append([])
                    continue
                tmp_rating_1 = []
                for i in range(len(ratings)):
                    tmp_rating_1.append(ratings[i][0])
                temp_ratings.append(tmp_rating_1)
            save_list = 'all_ratings_' + file_name
            for i in range(len(temp_ratings)):
                if temp_ratings[i] == []:
                    continue
                for rating in temp_ratings[i]:
                    eval(save_list)[i].append(rating)

            with open(os.path.join(cur_save_path, file_name) + ".csv", "w", encoding="utf-8", newline="") as wf:
                csv_writer = csv.writer(wf)
                csv_writer.writerow(col_name)
                csv_writer.writerow(np.float32(avg_all_ratings))
                csv_writer.writerow(np.float32(n_all_ratings))
                csv_writer.writerow(np.float32(std_all_ratings))

            # test for 3
        # if count == 3:
    for interest in interests:
        file_name = str(interest)
        col_name = []
        for words in eval(interest):
            if len(words) == 2:
                col_name.append(words[0] + "_" + words[1])
            else:
                col_name.append(words[0])
        save_list = 'all_ratings_' + file_name
        with open(os.path.join(cur_overall_save_path, file_name + ".csv"), 'w', encoding="utf-8", newline="") as wf:
            csv_write = csv.writer(wf)
            csv_write.writerow(col_name)
            csv_write.writerows(eval(save_list))




# Overall level with variance
'''
count = 0
overall_name = "_Overall"
if not os.path.exists(os.path.join(save_path, overall_name)):
    os.mkdir(os.path.join(save_path, overall_name))
cur_save_path = os.path.join(save_path, overall_name)
for interest in interests:
    file_name = str(interest)
    col_name = []
    avg_all_ratings = []
    n_all_ratings = []
    std_all_ratings = []
    for words in eval(interest):
        if len(words) == 2:
            col_name.append(words[0] + "_" + words[1])
        else:
            col_name.append(words[0])
        all_reviews = []
        with open(os.path.join(dataset_path, "bubble_tea_review.json"), "r", encoding="utf-8") as review_f:
            for review_json in review_f:
                dict_json = json.loads(review_json)
                all_reviews.append(dict_json["text"])
        print("Total Reviews len %s"%len(all_reviews))
        avg_rating, n_ratings, std_ratings, ratings = find_words_in_review(all_reviews, words, tea=len(words) == 2)
        avg_all_ratings.append(avg_rating)
        n_all_ratings.append(n_ratings)
        std_all_ratings.append(std_ratings)

    with open(os.path.join(cur_save_path, file_name) + ".csv", "w", encoding="utf-8", newline="") as wf:
        csv_writer = csv.writer(wf)
        csv_writer.writerow(col_name)
        csv_writer.writerow(np.float32(avg_all_ratings))
        csv_writer.writerow(np.float32(n_all_ratings))
        csv_writer.writerow(np.float32(std_all_ratings))
'''
'''
# Overall level without variance
# ["Tea_Types", "Tea_Ingredients", "Atmosphere", "Price", "Service"]

def uninstall(mainpath = os.getcwd()):
    filelist = os.listdir(mainpath)
    for filename in filelist:
        if os.path.isfile(os.path.join(mainpath, filename)):
            os.remove(os.path.join(mainpath, filename))
        elif os.path.isdir(os.path.join(mainpath, filename)):
            shutil.rmtree(os.path.join(mainpath, filename))
        else:
            pass

list_Tea_Types = []
list_Tea_Ingredients = []
list_Atmosphere = []
list_Price = []
list_Service = []

overall_dir = "__overall__"
if os.path.exists(os.path.join(save_path,overall_dir)):
    uninstall(mainpath=os.path.join(save_path,overall_dir))
    os.rmdir(os.path.join(save_path,overall_dir))
all_dir = os.listdir(save_path)
for dir in all_dir:
    cur_path = os.path.join(save_path,dir)
    for i in range(len(interests)):
        with open(os.path.join(cur_path, interests[i] + ".csv"), "r", encoding="utf-8") as f:
            csv_reader = csv.reader(f)
            label = csv_reader.__next__()
            mean_val = np.array(csv_reader.__next__(), dtype = np.float32)
            n_val = np.array(csv_reader.__next__(), dtype = np.float32)
            std_val = np.array(csv_reader.__next__(), dtype = np.float32)
            save_list = "list_%s"%(interests[i])
            eval(save_list).append([mean_val,n_val,std_val])

os.mkdir(os.path.join(save_path,overall_dir))
save_overall_path = os.path.join(save_path,overall_dir)

def cal_mean_n_std(list_interests):
    list_sum = [0] * len(list_interests[0][0])
    list_sum_n = [0] * len(list_interests[0][0])
    list_sum_var = [0] * len(list_interests[0][0])
    for i in range(len(list_interests)):
        list_sum += list_interests[i][0] * list_interests[i][1]
        list_sum_n += list_interests[i][1]
    avg_all_ratings = list_sum / list_sum_n
    avg_n = list_sum_n
    avg_std = 0
    return avg_all_ratings,avg_n,avg_std


for interest in interests:
    file_name = str(interest)
    col_name = []
    for words in eval(interest):
        if len(words) == 2:
            col_name.append(words[0] + "_" + words[1])
        else:
            col_name.append(words[0])
    save_list = "list_%s" % (interest)
    avg_all_ratings, avg_n, avg_std = cal_mean_n_std(eval(save_list))
    with open(os.path.join(save_overall_path, file_name + ".csv"), "w", encoding="utf-8", newline = "") as wf:
        csv_writer = csv.writer(wf)
        csv_writer.writerow(col_name)
        csv_writer.writerow(avg_all_ratings)
        csv_writer.writerow(avg_n)
        csv_writer.writerow(avg_std)
'''