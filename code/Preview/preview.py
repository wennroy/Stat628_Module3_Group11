#coding:utf-8
import os
import json
import re

os.chdir("D:\\WISC\\stat628\\Module3\\Stat628_Module3_Group11")
print(os.getcwd())
dataset_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset")
save_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset_preview")

for file_name in os.listdir(dataset_path):
    if not (re.search("json", file_name)):
        break
    with open(os.path.join(dataset_path, "%s" % file_name), 'r', encoding="UTF-8") as f:
        if os.path.isfile(os.path.join(save_path, "preview_%s" % file_name)):
            os.remove(os.path.join(save_path, "preview_%s" % file_name))

        for i in range(500):
            line = f.__next__()
            dict_json = json.loads(line)

            with open(os.path.join(save_path, "preview_%s" % file_name), 'a') as wf:
                wf.write(json.dumps(dict_json, indent=4))
