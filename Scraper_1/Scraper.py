from gnews import GNews
import pickle
import os
import json
'''
This scraper here is used to obtain news data, can be imported to another file
and simply call the getNews function to obtain news data of a company.
'''
date_dict = {
        1 : "Jan",
        2 : "Feb",
        3 : "Mar",
        4 : "Apr",
        5 : "May",
        6 : "Jun",
        7 : "Jul",
        8 : "Aug",
        9 : "Sep",
        10 : "Oct",
        11 : "Nov",
        12 : "Dec"
    }

def saveFile(file_content,folder_name,file_name):

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Create and write to the file inside the folder
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, 'w') as file:
        json.dump(file_content, file, indent=4)

def getNews_by_companyNames(name,month,year,num_of_years):
    folder_path = os.path.join("/Users/lixin/Desktop/News Extraction/Scraper_1/NewsDataFolder" , name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    google_news = GNews()

    google_news.max_results = 100000
    target_Period = 12 * num_of_years
    last = 1
    period = "m"
    for i in range(target_Period):

        data_folder_path = os.path.join(folder_path, date_dict[month] + "-" + str(year))
        if not os.path.exists(data_folder_path):
            os.makedirs(data_folder_path)

        google_news.end_date = (year, month, 1) # e.g. 2023,1,1
        if month == 1:
            year = year - 1 # 2022
            month = 12
            google_news.start_date = (year, month, 1) # 2022,12,1
        else:
            month = month - 1
            google_news.start_date = (year, month, 1)
        print("getting data from :",google_news.start_date,google_news.end_date)
        json_resp = google_news.get_news(name)
        for link in range(len(json_resp)):
            try:
                article = google_news.get_full_article(
                json_resp[link]['url'])
                json_resp[link]['content'] = article.text
                #print(article.title)
                #print(json_resp[link]['url'])
                #print(json_resp[link])
                #break
                saveFile(json_resp[link],data_folder_path,article.title + ".json")
            except Exception as e:
                #link cannot be scraped
                print("Fail to obtain content for link. Skipped...")
        last += 1

'''------------------------------------------------------------------------------------------'''

def getNews_by_topics(topic,month,year,num_of_years):
    folder_path = os.path.join("/Users/lixin/Desktop/News Extraction/Scraper_1/NewsDataFolder/gnewspull/Topic" , topic)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    google_news = GNews()
    # google_news.language = 'english'
    # month = 12
    # year = 2016

    google_news.max_results = 100000
    target_Period = 12 * num_of_years
    last = 1
    period = "m"
    for i in range(target_Period):

        data_folder_path = os.path.join(folder_path, date_dict[month] + "-" + str(year))
        if not os.path.exists(data_folder_path):
            os.makedirs(data_folder_path)

        google_news.end_date = (year, month, 1) # e.g. 2023,1,1
        if month == 1:
            year = year - 1 # 2022
            month = 12
            google_news.start_date = (year, month, 1) # 2022,12,1
        else:
            month = month - 1
            google_news.start_date = (year, month, 1)
        print("getting data from :",google_news.start_date,google_news.end_date)
        json_resp = google_news.get_news_by_topic(topic=topic)
        for link in range(len(json_resp)):
            try:
                article = google_news.get_full_article(
                json_resp[link]['url'])
                json_resp[link]['content'] = article.text
                #print(article.title)
                #print(json_resp[link]['url'])
                #print(json_resp[link])
                #break
                saveFile(json_resp[link],data_folder_path,article.title + ".json")
            except Exception as e:
                #link cannot be scraped
                print("Fail to obtain content for link. Skipped...")
        last += 1
