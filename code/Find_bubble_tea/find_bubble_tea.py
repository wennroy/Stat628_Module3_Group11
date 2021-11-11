import os
import json
import re

os.chdir("D:\\WISC\\stat628\\Module3\\Stat628_Module3_Group11")
print(os.getcwd())
dataset_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset")
save_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset_Bubble_Tea")

file_name = "business.json"
total_num = 0
all_business_id = []

with open(os.path.join(dataset_path, "%s" % file_name), 'r', encoding="UTF-8") as f:
    if os.path.isfile(os.path.join(save_path, "bubble_tea_%s" % file_name)):
        os.remove(os.path.join(save_path, "bubble_tea_%s" % file_name))

    for line in f:
        dict_json = json.loads(line)
        categories = dict_json["categories"]
        is_bubble_tea = False
        if categories:
            for category in categories.split(", "):
                if category.lower() == "bubble tea":
                    is_bubble_tea = True
                    total_num += 1
                    all_business_id.append(dict_json["business_id"])
                    break

        if is_bubble_tea:
            with open(os.path.join(save_path, "bubble_tea_%s" % file_name), 'a') as wf:
                wf.write(json.dumps(dict_json) + '\n')

print(total_num)

with open(os.path.join(save_path, "bubble_tea_business_id.txt"), 'w') as bwf:
    for b_id in all_business_id:
        bwf.write(b_id+"\n")
