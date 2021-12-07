import numpy as np
from scipy import stats
import os
import csv

import pandas as pd

os.chdir("D:\\WISC\\stat628\\Module3\\Stat628_Module3_Group11")
print(os.getcwd())
save_path = os.path.join(os.getcwd(), ".\\code\\attributes\\")

all_data = pd.read_csv(os.path.join(save_path,"total_with_review.csv"))

overall_data = pd.read_csv(os.path.join(save_path,"overall_review.csv"))
suggestions = []

def two_sample_unequal_variance_unpaired_t_test(x,x_n,x_std, y,y_n,y_std):
    t = (x - y - 0)/np.sqrt(x_std**2/x_n + y_std**2/y_n)
    df = (x_std**2/x_n + y_std**2/y_n)**2/(x_std**4/(x_n**2*(x_n-1))+y_n**2*(y_n-1))
    return stats.t.pdf(t, df=df), x < y

for i in range(len(all_data)): # test
    ## environment
    environment_sug = False
    environment_pos = True
    rating = all_data["environment"][i]
    if not rating == -1:
        rating_n = all_data["environment_n"][i]
        rating_std = all_data["environment_std"][i]

        overall = overall_data["environment"][0]
        overall_n = overall_data["environment_n"][0]
        overall_std = overall_data["environment_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            environment_sug = True
        elif p_value < 0.05 and not lower:
            environment_pos = True

    ## atmosphere
    atmosphere_sug = False
    atmosphere_pos = False
    rating = all_data["atmosphere"][i]
    if not rating == -1:
        rating_n = all_data["atmosphere_n"][i]
        rating_std = all_data["atmosphere_std"][i]

        overall = overall_data["atmosphere"][0]
        overall_n = overall_data["atmosphere_n"][0]
        overall_std = overall_data["atmosphere_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            atmosphere_sug = True
        elif p_value < 0.05 and not lower:
            atmosphere_pos = True
    ## ambiance
    ambiance_sug = False
    ambiance_pos = False
    rating = all_data["ambiance"][i]
    if not rating == -1:
        rating_n = all_data["ambiance_n"][i]
        rating_std = all_data["ambiance_std"][i]

        overall = overall_data["ambiance"][0]
        overall_n = overall_data["ambiance_n"][0]
        overall_std = overall_data["ambiance_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            ambiance_sug = True
        elif p_value < 0.05 and not lower:
            ambiance_pos = True
    ## noisy
    noisy_sug = False
    rating = all_data["noisy"][i]
    if not rating == -1:
        rating_n = all_data["noisy_n"][i]
        rating_std = all_data["noisy_std"][i]

        overall = overall_data["noisy"][0]
        overall_n = overall_data["noisy_n"][0]
        overall_std = overall_data["noisy_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            noisy_sug = True

    ## noise
    noise_sug = False
    rating = all_data["noise"][i]
    if not rating == -1:
        rating_n = all_data["noise_n"][i]
        rating_std = all_data["noise_std"][i]

        overall = overall_data["noise"][0]
        overall_n = overall_data["noise_n"][0]
        overall_std = overall_data["noise_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            noise_sug = True

    ## dessert
    dessert_sug = False
    dessert_pos = False
    rating = all_data["dessert"][i]
    if not rating == -1:
        rating_n = all_data["dessert_n"][i]
        rating_std = all_data["dessert_std"][i]

        overall = overall_data["dessert"][0]
        overall_n = overall_data["dessert_n"][0]
        overall_std = overall_data["dessert_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            dessert_sug = True
        elif p_value < 0.05 and not lower:
            dessert_pos = True
    ## cake
    cake_sug = False
    cake_pos = False
    rating = all_data["cake"][i]
    if not rating == -1:
        rating_n = all_data["cake_n"][i]
        rating_std = all_data["cake_std"][i]

        overall = overall_data["cake"][0]
        overall_n = overall_data["cake_n"][0]
        overall_std = overall_data["cake_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            cake_sug = True
        elif p_value < 0.05 and not lower:
            cake_pos = True

    ## tiramisu
    tiramisu_sug = False
    tiramisu_pos = False
    rating = all_data["tiramisu"][i]
    if not rating == -1:
        rating_n = all_data["tiramisu_n"][i]
        rating_std = all_data["tiramisu_std"][i]

        overall = overall_data["tiramisu"][0]
        overall_n = overall_data["tiramisu_n"][0]
        overall_std = overall_data["tiramisu_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            tiramisu_sug = True
        elif p_value < 0.05 and not lower:
            tiramisu_pos = True

    ## food
    food_sug = False
    food_pos = False
    rating = all_data["food"][i]
    if not rating == -1:
        rating_n = all_data["food_n"][i]
        rating_std = all_data["food_std"][i]

        overall = overall_data["food"][0]
        overall_n = overall_data["food_n"][0]
        overall_std = overall_data["food_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            food_sug = True
        elif p_value < 0.05 and not lower:
            food_pos = True
    ## drink
    drink_sug = False
    drink_pos = False
    rating = all_data["drink"][i]
    if not rating == -1:
        rating_n = all_data["drink_n"][i]
        rating_std = all_data["drink_std"][i]

        overall = overall_data["drink"][0]
        overall_n = overall_data["drink_n"][0]
        overall_std = overall_data["drink_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            drink_sug = True
        elif p_value < 0.05 and not lower:
            drink_pos = True
    ## coffee
    coffee_sug = False
    coffee_pos = False
    rating = all_data["coffee"][i]
    if not rating == -1:
        rating_n = all_data["coffee_n"][i]
        rating_std = all_data["coffee_std"][i]

        overall = overall_data["coffee"][0]
        overall_n = overall_data["coffee_n"][0]
        overall_std = overall_data["coffee_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            coffee_sug = True
        elif p_value < 0.05 and not lower:
            coffee_pos = True

    ## price
    price_sug = False
    price_pos = False
    rating = all_data["price"][i]
    if not rating == -1:
        rating_n = all_data["price_n"][i]
        rating_std = all_data["price_std"][i]

        overall = overall_data["price"][0]
        overall_n = overall_data["price_n"][0]
        overall_std = overall_data["price_std"][0]
        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            price_sug = True
        elif p_value < 0.05 and not lower:
            price_pos = True
    ## service
    service_sug = False
    service_pos = False
    rating = all_data["service"][i]
    if not rating == -1:
        rating_n = all_data["service_n"][i]
        rating_std = all_data["service_std"][i]

        overall = overall_data["service"][0]
        overall_n = overall_data["service_n"][0]
        overall_std = overall_data["service_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            service_sug = True
        elif p_value < 0.05 and not lower:
            service_pos = True
    ## open
    open_sug = False
    rating = all_data["open"][i]
    if not rating == -1:
        rating_n = all_data["open_n"][i]
        rating_std = all_data["open_std"][i]

        overall = overall_data["open"][0]
        overall_n = overall_data["open_n"][0]
        overall_std = overall_data["open_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            open_sug = True

    ## close
    close_sug = False
    rating = all_data["close"][i]
    if not rating == -1:
        rating_n = all_data["close_n"][i]
        rating_std = all_data["close_std"][i]

        overall = overall_data["close"][0]
        overall_n = overall_data["close_n"][0]
        overall_std = overall_data["close_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            close_sug = True

    ## bubble
    bubble_sug = False
    bubble_pos = False
    rating = all_data["bubble"][i]
    if not rating == -1:
        rating_n = all_data["bubble_n"][i]
        rating_std = all_data["bubble_std"][i]

        overall = overall_data["bubble"][0]
        overall_n = overall_data["bubble_n"][0]
        overall_std = overall_data["bubble_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            bubble_sug = True
        elif p_value < 0.05 and not lower:
            bubble_pos = True

    ## boba
    boba_sug = False
    boba_pos = False
    rating = all_data["boba"][i]
    if not rating == -1:
        rating_n = all_data["boba_n"][i]
        rating_std = all_data["boba_std"][i]

        overall = overall_data["boba"][0]
        overall_n = overall_data["boba_n"][0]
        overall_std = overall_data["boba_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            boba_sug = True
        elif p_value < 0.05 and not lower:
            boba_pos = True
    ## rainbow
    rainbow_sug = False
    rainbow_pos = False
    rating = all_data["rainbow"][i]
    if not rating == -1:
        rating_n = all_data["rainbow_n"][i]
        rating_std = all_data["rainbow_std"][i]

        overall = overall_data["rainbow"][0]
        overall_n = overall_data["rainbow_n"][0]
        overall_std = overall_data["rainbow_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            rainbow_sug = True
        elif p_value < 0.05 and not lower:
            rainbow_pos = True
    ## taro
    taro_sug = False
    taro_pos = False
    rating = all_data["taro"][i]
    if not rating == -1:
        rating_n = all_data["taro_n"][i]
        rating_std = all_data["taro_std"][i]

        overall = overall_data["taro"][0]
        overall_n = overall_data["taro_n"][0]
        overall_std = overall_data["taro_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            taro_sug = True
        elif p_value < 0.05 and not lower:
            taro_pos = True
    ## green_tea
    green_tea_sug = False
    green_tea_pos = False
    rating = all_data["green_tea"][i]
    if not rating == -1:
        rating_n = all_data["green_tea_n"][i]
        rating_std = all_data["green_tea_std"][i]

        overall = overall_data["green_tea"][0]
        overall_n = overall_data["green_tea_n"][0]
        overall_std = overall_data["green_tea_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            green_tea_sug = True
        elif p_value < 0.05 and not lower:
            green_tea_pos = True

    ## oolong_tea
    oolong_tea_sug = False
    oolong_tea_pos = False
    rating = all_data["oolong_tea"][i]
    if not rating == -1:
        rating_n = all_data["oolong_tea_n"][i]
        rating_std = all_data["oolong_tea_std"][i]

        overall = overall_data["oolong_tea"][0]
        overall_n = overall_data["oolong_tea_n"][0]
        overall_std = overall_data["oolong_tea_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            oolong_tea_sug = True
        elif p_value < 0.05 and not lower:
            oolong_tea_pos = True
    ## black_tea
    black_tea_sug = False
    black_tea_pos = False
    rating = all_data["black_tea"][i]
    if not rating == -1:
        rating_n = all_data["black_tea_n"][i]
        rating_std = all_data["black_tea_std"][i]

        overall = overall_data["black_tea"][0]
        overall_n = overall_data["black_tea_n"][0]
        overall_std = overall_data["black_tea_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            black_tea_sug = True
        elif p_value < 0.05 and not lower:
            black_tea_pos = True
    ## matcha
    matcha_sug = False
    matcha_pos = False
    rating = all_data["matcha"][i]
    if not rating == -1:
        rating_n = all_data["matcha_n"][i]
        rating_std = all_data["matcha_std"][i]

        overall = overall_data["matcha"][0]
        overall_n = overall_data["matcha_n"][0]
        overall_std = overall_data["matcha_std"][0]
        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            matcha_sug = True
        elif p_value < 0.05 and not lower:
            matcha_pos = True
    ## herbal
    herbal_sug = False
    herbal_pos = False
    rating = all_data["herbal"][i]
    if not rating == -1:
        rating_n = all_data["herbal_n"][i]
        rating_std = all_data["herbal_std"][i]

        overall = overall_data["herbal"][0]
        overall_n = overall_data["herbal_n"][0]
        overall_std = overall_data["herbal_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            herbal_sug = True
        elif p_value < 0.05 and not lower:
            herbal_pos = True
    ## jasmine
    jasmine_sug = False
    jasmine_pos = False
    rating = all_data["jasmine"][i]
    if not rating == -1:
        rating_n = all_data["jasmine_n"][i]
        rating_std = all_data["jasmine_std"][i]

        overall = overall_data["jasmine"][0]
        overall_n = overall_data["jasmine_n"][0]
        overall_std = overall_data["jasmine_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            jasmine_sug = True
        elif p_value < 0.05 and not lower:
            jasmine_pos = True
    ## taiwanese
    taiwanese_sug = False
    rating = all_data["taiwanese"][i]
    if not rating == -1:
        rating_n = all_data["taiwanese_n"][i]
        rating_std = all_data["taiwanese_std"][i]

        overall = overall_data["taiwanese"][0]
        overall_n = overall_data["taiwanese_n"][0]
        overall_std = overall_data["taiwanese_std"][0]

        p_value, lower = two_sample_unequal_variance_unpaired_t_test(rating,rating_n,rating_std,overall,overall_n,overall_std)
        if p_value < 0.05 and lower:
            taiwanese_sug = True

    # Suggestions

    neg_temp_suggest = ''

    if environment_sug and atmosphere_sug and ambiance_sug:
        neg_temp_suggest += 'Seems like you need to work hard on improving your atmosphere, environment and ambiance etc. '
    elif environment_sug and atmosphere_sug:
        neg_temp_suggest += 'Seems like you need to work hard on improving your environment, atmosphere etc. '
    elif environment_sug and ambiance_sug:
        neg_temp_suggest += 'Seems like you need to work hard on improving your environment, ambiance etc. '
    elif atmosphere_sug and ambiance_sug:
        neg_temp_suggest += 'Seems like you need to work hard on improving your atmosphere, ambiance etc. '
    elif environment_sug:
        neg_temp_suggest += 'You need to improve your environment. '
    elif atmosphere_sug:
        neg_temp_suggest += 'You need to improve your atmosphere. '
    elif ambiance_sug:
        neg_temp_suggest += 'You need to improve your ambiance. '

    if noise_sug or noisy_sug:
        neg_temp_suggest += "The noise level may larger than other shops, consider reduce them."

    if dessert_sug and not cake_sug and not tiramisu_sug:
        neg_temp_suggest += "Some people complained about your desserts, we suggest pay more attention on your desserts. "
    elif dessert_sug and cake_sug and tiramisu_sug:
        neg_temp_suggest += "Some people complained about your desserts. We found that your cake and tiramisu were worse than other shops. We suggest you pay attention on that. "
    elif dessert_sug and cake_sug:
        neg_temp_suggest += "Some people complained about your desserts. We found that your cake was worse than other shops. We suggest you pay attention on that. "
    elif dessert_sug and tiramisu_sug:
        neg_temp_suggest += "Some people complained about your desserts. We found that your tiramisu was worse than other shops. We suggest you pay attention on that. "

    if food_sug:
        neg_temp_suggest += "We found Food quality wasn't good. "

    if drink_sug:
        if not neg_temp_suggest == '':
            neg_temp_suggest += "And drink quality wasn't good. "
        else:
            neg_temp_suggest += "Drink quality wasn't good. "

    if price_sug:
        neg_temp_suggest += "Many people compalned the price. Consider lower the price? "

    if service_sug:
        neg_temp_suggest += "The service was one thing you need to take into account. "

    if open_sug:
        neg_temp_suggest += "We suggest you change your open hour. "

    elif open_sug and close_sug:
        neg_temp_suggest += "We suggest you both adjust your open and close hour. "

    elif not open_sug and close_sug:
        neg_temp_suggest += "We suggest you adjust your close hour. "

    if bubble_sug or boba_sug or rainbow_sug or taro_sug or herbal_sug:
        neg_temp_suggest += "In terms of tea ingredients. "

    if bubble_sug or boba_sug:
        neg_temp_suggest += "A lot of reviews with negative sentiment talked about boba and bubble, considering improve them? "

    if rainbow_sug:
        neg_temp_suggest += "We suggested you to improve rainbow jelly. "

    if taro_sug:
        neg_temp_suggest += "The taro you made was not better than other shops, try to improve the taste of taro. "
    if herbal_sug:
        neg_temp_suggest += "Herbal jelly was not good as expected. We suggest you change the herbal materials. "

    tea_type_sug = []
    if green_tea_sug:
        tea_type_sug.append("green tea")
    if oolong_tea_sug:
        tea_type_sug.append("oolong tea")
    if black_tea_sug:
        tea_type_sug.append("black tea")
    if matcha_sug:
        tea_type_sug.append("matcha tea")
    if jasmine_sug:
        tea_type_sug.append("jasmine tea")


    if not tea_type_sug == []:
        neg_temp_suggest += "In terms of tea type, we found that the following tea types "
        tea_type_sug_str = ''
        for _ in tea_type_sug:
            tea_type_sug_str += _ + ", "
        neg_temp_suggest += tea_type_sug_str[:-2]
        neg_temp_suggest += " was/were not good as other tea shops, we suggest you improve that part. "

    if all_data["weekhour"][i] > 56:
        neg_temp_suggest += 'We suggest you to open less hour in a week. Less than 8 hours a day might be great. '
    if all_data["WiFi"][i] == "no":
        neg_temp_suggest += 'WiFi is an import factor to improve the ratings, consider have a free WiFi in store.'

    ## Positive review
    pos_temp = ''
    if environment_sug and atmosphere_sug and ambiance_sug:
        pos_temp += 'You are doing great at ambiance aspect, keep going! '

    if drink_pos:
        pos_temp += 'The drinks are way above the average. '

    if food_pos:
        pos_temp += 'The food are very delicious. '
        if dessert_pos and cake_pos and tiramisu_pos:
            pos_temp += 'The desserts are great, many customers like your desserts. '
    if price_pos:
        pos_temp += 'The price you set are reasonable, customers praise the price a lot. '
    if service_pos:
        pos_temp += 'Services you provided are great, beyond the average. '

    if (bubble_pos and boba_pos) or rainbow_pos or taro_pos:
        pos_temp += "In terms of tea ingredients. "
    if bubble_pos and boba_pos:
        pos_temp += "Boba and bubble you made are popular. "
    if rainbow_pos:
        pos_temp += "People love your rainbow jelly. "
    if taro_pos:
        pos_temp += "Tora in the tea is delicious. "

    tea_type_pos = []
    if green_tea_pos:
        tea_type_pos.append("green tea")
    if oolong_tea_pos:
        tea_type_pos.append("oolong tea")
    if black_tea_pos:
        tea_type_pos.append("black tea")
    if matcha_pos:
        tea_type_pos.append("matcha tea")
    if jasmine_pos:
        tea_type_pos.append("jasmine tea")

    if not tea_type_pos == []:
        pos_temp += "In the tea type aspect, we found that the following tea types "
        tea_type_pos_str = ''
        for _ in tea_type_pos:
            tea_type_pos_str += _ + ", "
        pos_temp += tea_type_pos_str[:-2]
        pos_temp += " was/were more popular than other shops! "

    if all_data["WiFi"][i] == "free":
        pos_temp += "Having free WiFi is great for improving the rating of reviews, keep going! "

    suggestions.append([neg_temp_suggest, pos_temp])

with open(os.path.join(save_path, "suggestions.csv"), "w", newline="", encoding="utf-8") as wf:
    csv_writer = csv.writer(wf)
    csv_writer.writerow(["Suggestions", "strengths"])
    csv_writer.writerows(suggestions)

f1 = pd.read_csv(os.path.join(save_path, "total(2)(1)_UTF8.csv"))
f2 = pd.read_csv(os.path.join(save_path, "suggestions.csv"))

file = [f1, f2]
total = pd.concat(file, axis = 1)
total.to_csv(os.path.join(save_path, "total_with_suggestions.csv"), index=0, sep=',')
