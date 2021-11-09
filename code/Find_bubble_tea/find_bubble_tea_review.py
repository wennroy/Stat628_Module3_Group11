import os
import json
import re

os.chdir("D:\\WISC\\stat628\\Module3\\Stat628_Module3_Group11")
print(os.getcwd())
dataset_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset")
save_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset_Bubble_Tea")

all_business_id = []

with open(os.path.join(save_path, "bubble_tea_business_id.txt"), 'r') as bwf:
    for line in bwf:
        all_business_id.append(line[:-1])

file_name = "review.json"
num = 0
num_bubble_tea = 0
if os.path.isfile(os.path.join(save_path, "bubble_tea_%s" % file_name)):
    os.remove(os.path.join(save_path, "bubble_tea_%s" % file_name))

with open(os.path.join(dataset_path, "%s" % file_name), 'r', encoding="UTF-8") as f:
    for line in f:
        num += 1
        if num % 10000 == 0:
            print("Loaded %s lines so far." % num)
        dict_json = json.loads(line)
        bid = dict_json["business_id"]
        if not bid in all_business_id:
            continue
        num_bubble_tea += 1
        if num_bubble_tea % 100 == 0:
            print("Found %s reviews about a bubble tea store." % (num_bubble_tea))

        with open(os.path.join(save_path, "bubble_tea_%s" % file_name), 'a') as wf:
            wf.write(json.dumps(dict_json, indent=4))

print("Total %s reviews" % num)
print("Total %s reviews for bubble tea" % num_bubble_tea)