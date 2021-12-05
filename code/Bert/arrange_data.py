import os

os.chdir("D:\\WISC\\stat628\\Module3\\Stat628_Module3_Group11")
print(os.getcwd())
dataset_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset")
file_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset_review")
save_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset_review_classification")


for i in range(5):
    cur_save_path = os.path.join(save_path, str(i+1))
    review_path = os.path.join(file_path, str(i+1) + ".txt")
    review_count = 0
    with open(review_path, 'r', encoding="utf-8") as f:
        for line in f:
            review_count += 1
            file_name = str(i+1) + '_' + str(review_count) + ".txt"
            with open(os.path.join(cur_save_path,file_name), "w", encoding="utf-8") as wf:
                wf.write(line)
