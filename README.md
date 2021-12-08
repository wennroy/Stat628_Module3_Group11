# Stat628 Module3 Group11
## How to raise your rating on Yelp - for bubble tea shop

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

## Summary
`Module3_Group11_Summary_Report.pdf` is the final summary report.

## Presentations
`Preliminary_Module3_Group11_Slides.pdf` is the slides of preliminary presentation.

`Final_Module3_Group11_Slides.pdf` is the slides of final presentations.

# Contributions

1. QZ (Qilu Zhou) was mainly responsible for business attributes analysis, wrote the related code such as ANOVA analysis on business attributes and data cleaning based on missing value in Business Attributes. QZ also wrote the first three sections (Introduction, Data Cleaning and Business Attributes Analysis), had partial contribution on Shiny app and the last section in this summary report. QZ completed the most of the work for presentation slides based on our summary report.
2. (Zhengyuan Wen) was mainly responsible for reviews analysis, built the Bert model to obtain sentiment scores for each sentence, wrote the related codes for extracting the bubble tea stores/reviews, reviews analysis, writing the suggestions and strengths for specific bubble tea shops. ZW also wrote the fourth part Review Analysis in this summary, and had a little contribution on presentation slides based on the version of QZ provided.
3. JJ (Jiaying Jia) was mainly in charge of Shiny App Design, wrote all the codes related to shiny app design such as bar plot, UI design and back end implementation. JJ also did some adjustment on the final data for easier interpretation on Shiny App. JJ wrote the fifth part Shiny App Design in our summary report, and was responsible for polishing the whole summary report.
    
# Shiny App link
[https://uadvip-jiaying-jia.shinyapps.io/shinyapp/](https://uadvip-jiaying-jia.shinyapps.io/shinyapp/)
Backup Link: [http://www.wennroy.com:3838/sample-apps/bubble_tea/](http://www.wennroy.com:3838/sample-apps/bubble_tea/)
