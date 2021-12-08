# Stat628 Module3 Group11
## What makes a good bubble tea shop? Based on Yelp Data

We are Thursday group11. Team members are Qilu Zhou, Jiaying Jia, Zhengyuan Wen.

These are the codes, reports and the figures we used in our analysis.

## Files Summary
### code
The code file includes all the codes we used in our analysis. 

`attributes` is related to business attributes analysis. And several final merged csv file with all the information we need.

`Bert` contains bert related files, including original pre-train Bert model, preprocessing layers, final model we used and all the bert related codes.

`Find_bubble_tea`, `Preview` includes an early stage work that extract the reviews and business attributes of whose categories contain "Bubble Tea".

`Wordcloud` consists codes of the TF-IDF analysis and wordcloud generation.

`Combine_attributes_and_review.py` is the code that combines the attributes results and sentiments scores together into two merged csv file `overall.csv` and `total.csv` in `attributes/`.

`write_suggestion.py` writes all the suggestion into the merged csv file.

## shinyapp
The `shinyapp` contains all the codes and related merges csv files. `ui.R` is the front end interface can be decoded into `html` file by `Rshiny`. And `server.R` is the back end of our webpage.

## wordcloud_pic
It contains all the wordcloud and tf-idf figures we used in the preliminary presentations.

# Contributions

# Shiny App link
[https://uadvip-jiaying-jia.shinyapps.io/shinyapp/](https://uadvip-jiaying-jia.shinyapps.io/shinyapp/)
