import pandas as pd
import numpy as np
import os
import csv

os.chdir("D:\\WISC\\stat628\\Module3\\Stat628_Module3_Group11")
print(os.getcwd())
review_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset_business_review\\")
save_path = os.path.join(os.getcwd(), ".\\code\\attributes\\")

with open(os.path.join(save_path, "totalUTF8.csv"), "r", encoding="utf-8") as total_f:
    csv_reader = csv.reader(total_f)
    label = csv_reader.__next__()
    business_id_order = []
    for line in csv_reader:
        business_id_order.append(line[1])

print(len(business_id_order))

files_names = os.listdir(review_path)

label = ['environment', 'atmosphere', 'ambiance', 'books', 'noisy', 'noise', 'dessert', 'cake', 'tiramisu', 'food',
         'drink', 'coffee',
         'price', 'service', 'open', 'close', 'ceremony', 'bubble', 'boba', 'rainbow', 'taro', 'green_tea',
         'oolong_tea', 'black_tea', 'red_tea', 'matcha', 'herbal', 'jasmine', 'taiwanese', 'Atmosphere_Rating',
         'Food_Rating', 'Price_Rating', 'Service_Rating', 'Tea_Ingredients_Rating', 'Tea_Types_Rating','Overall',
         'Atmosphere_Rating_n',
         'Food_Rating_n', 'Price_Rating_n', 'Service_Rating_n', 'Tea_Ingredients_Rating_n', 'Tea_Types_Rating_n',
        'environment_n', 'atmosphere_n', 'ambiance_n', 'books_n', 'noisy_n', 'noise_n', 'dessert_n', 'cake_n', 'tiramisu_n', 'food_n',
         'drink_n', 'coffee_n',
         'price_n', 'service_n', 'open_n', 'close_n', 'ceremony_n', 'bubble_n', 'boba_n', 'rainbow_n', 'taro_n', 'green_tea_n',
         'oolong_tea_n', 'black_tea_n', 'red_tea_n', 'matcha_n', 'herbal_n', 'jasmine_n', 'taiwanese_n',
'environment_std', 'atmosphere_std', 'ambiance_std', 'books_std', 'noisy_std', 'noise_std', 'dessert_std', 'cake_std', 'tiramisu_std', 'food_std',
         'drink_std', 'coffee_std',
         'price_std', 'service_std', 'open_std', 'close_std', 'ceremony_std', 'bubble_std', 'boba_std', 'rainbow_std', 'taro_std', 'green_tea_std',
         'oolong_tea_std', 'black_tea_std', 'red_tea_std', 'matcha_std', 'herbal_std', 'jasmine_std', 'taiwanese_std',
         ]
def categorical_score(ratings_temp, n_temp):
    atmosphere = np.nansum(ratings_temp[:3] * n_temp[:3]) / np.sum(n_temp[:3]) # Environment atmosphere ambiance
    food = np.nansum(ratings_temp[9:11] * n_temp[9:11]) / np.sum(n_temp[9:11])# Food Drink
    price = np.nansum(ratings_temp[12] * n_temp[12]) / np.sum(n_temp[12]) # Price
    service = np.nansum(ratings_temp[13] * n_temp[13])/np.sum(n_temp[13]) # Service
    tea_ingredients = np.nansum(ratings_temp[17:21] * n_temp[17:21])/np.sum(n_temp[17:21]) # all tea ingredients
    tea_types = np.nansum(ratings_temp[21:] * n_temp[21:])/np.sum(n_temp[21:]) #All tea types
    overall = np.nanmean([atmosphere,food,price,service,tea_ingredients,tea_types])

    if atmosphere is np.nan:
        atmosphere = -1
    if food is np.nan:
        food = -1
    if price is np.nan:
        price = -1
    if service is np.nan:
        service = -1
    if tea_ingredients is np.nan:
        tea_ingredients = -1
    if tea_types is np.nan:
        tea_types = -1

    return [atmosphere, food, price, service, tea_ingredients, tea_types, overall, np.sum(n_temp[:3]), np.sum(n_temp[9:11]), np.sum(n_temp[12]), np.sum(n_temp[13]), np.sum(n_temp[17:21]),np.sum(n_temp[21:])]

data_review = []
for i in range(len(business_id_order)):
    cur_business_id = business_id_order[i]
    if not cur_business_id in files_names:
        print("warning: %s is not in review list" % cur_business_id)
        continue

    cur_business_path = os.path.join(review_path, cur_business_id)
    review_files = os.listdir(cur_business_path)
    ratings_temp = []
    n_temp = []
    std_temp = []
    for review_file in review_files:
        with open(os.path.join(cur_business_path, review_file), "r", encoding="utf-8") as review_f:
            label_temp = review_f.__next__()
            nxt_line = review_f.__next__()
            nxt_line = "[" + nxt_line[:-1] + "]"
            ratings_temp = np.hstack([ratings_temp, eval(nxt_line)])
            nxt_line = review_f.__next__()
            nxt_line = "[" + nxt_line[:-1] + "]"
            n_temp = np.hstack([n_temp, eval(nxt_line)])
            nxt_line = review_f.__next__()
            nxt_line = "[" + nxt_line[:-1] + "]"
            std_temp = np.hstack([std_temp, eval(nxt_line)])
    temp_overall = categorical_score(ratings_temp, n_temp)
    temp_overall = np.hstack([ratings_temp,temp_overall])
    temp_overall = np.hstack([temp_overall, n_temp])
    temp_overall = np.hstack([temp_overall, std_temp])
    data_review.append(temp_overall)

with open(os.path.join(save_path, "total_review.csv"), 'w', encoding="utf-8", newline='') as wf:
    csv_writer = csv.writer(wf)
    csv_writer.writerow(label)
    csv_writer.writerows(data_review)

# Overall

data_review = []
cur_business_path = os.path.join(review_path, '__Overall')
review_files = os.listdir(cur_business_path)
ratings_temp = []
n_temp = []
std_temp = []
for review_file in review_files:
    if not review_file[:3] == 'Avg':
        continue
    if review_file == 'Avg_Special_items.csv':
        continue
    with open(os.path.join(cur_business_path, review_file), "r", encoding="utf-8") as review_f:
        label_temp = review_f.__next__()
        nxt_line = review_f.__next__()
        nxt_line = "[" + nxt_line[:-1] + "]"
        ratings_temp = np.hstack([ratings_temp, eval(nxt_line)])
        nxt_line = review_f.__next__()
        nxt_line = "[" + nxt_line[:-1] + "]"
        n_temp = np.hstack([n_temp, eval(nxt_line)])
        nxt_line = review_f.__next__()
        nxt_line = "[" + nxt_line[:-1] + "]"
        std_temp = np.hstack([std_temp, eval(nxt_line)])
temp_overall = categorical_score(ratings_temp, n_temp)
temp_overall = np.hstack([ratings_temp, temp_overall])
temp_overall = np.hstack([temp_overall, n_temp])
temp_overall = np.hstack([temp_overall, std_temp])
data_review.append(temp_overall)

with open(os.path.join(save_path, "overall_review.csv"), 'w', encoding="utf-8", newline='') as wf:
    csv_writer = csv.writer(wf)
    csv_writer.writerow(label)
    csv_writer.writerows(data_review)

f1 = pd.read_csv(os.path.join(save_path, "totalUTF8.csv"))
f2 = pd.read_csv(os.path.join(save_path, "total_review.csv"))
file = [f1,f2]
train = pd.concat(file,axis = 1)
train.to_csv(os.path.join(save_path,"total_with_review.csv"), index=0, sep=',')