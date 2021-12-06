import os
import csv
import numpy as np

os.chdir("D:\\WISC\\stat628\\Module3\\Stat628_Module3_Group11")
print(os.getcwd())
save_path = os.path.join(os.getcwd(), "..\\yelp_dataset\\yelp_dataset_business_review\\__Overall")

file_names = os.listdir(save_path)

for file in file_names:
    if file[:3] == 'Avg':
        continue
    avg_score = []
    avg_n = []
    avg_std = []
    with open(os.path.join(save_path,file), "r", encoding="utf-8") as f:
        csv_reader = csv.reader(f)
        label = csv_reader.__next__()
        n = len(label)
        for i in range(n):
            next_line = csv_reader.__next__()
            print(next_line)
            temp = np.array(next_line, dtype=np.float32)
            avg_score.append(temp.mean())
            avg_n.append(len(temp))
            avg_std.append(np.std(temp))

        with open(os.path.join(save_path,"Avg_" + file), "w", newline="", encoding="utf-8") as wf:
            csv_writer = csv.writer(wf)
            csv_writer.writerow(label)
            csv_writer.writerow(avg_score)
            csv_writer.writerow(avg_n)
            csv_writer.writerow(avg_std)

## Special items

# Combine Bubble and boba
# Combine Noisy and Noise

with open(os.path.join(save_path,"Tea_Ingredients.csv"), "r", encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    label = csv_reader.__next__()
    next_line = csv_reader.__next__()
    temp = np.array(next_line, dtype=np.float32)
    next_line = csv_reader.__next__()
    temp = np.hstack([temp, np.array(next_line, dtype=np.float32)])

with open(os.path.join(save_path, "Atmosphere.csv"), "r", encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    label = csv_reader.__next__()
    for i in range(4):
        drop = csv_reader.__next__()
    next_line = csv_reader.__next__()
    temp2 = np.array(next_line, dtype=np.float32)
    next_line = csv_reader.__next__()
    temp2 = np.hstack([temp, np.array(next_line, dtype=np.float32)])

with open(os.path.join(save_path,"Avg_" + "Special_items.csv"), "w", newline="", encoding="utf-8") as wf:
    csv_writer = csv.writer(wf)
    csv_writer.writerow(["Bubble_and_Boba","Noise_and_Noisy"])
    csv_writer.writerow([temp.mean(), temp2.mean()])
    csv_writer.writerow([len(temp), len(temp2)])
    csv_writer.writerow([np.std(temp), np.std(temp2)])
