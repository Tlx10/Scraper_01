from gnews import GNews
import os
import pandas as pd
from Scraper import getNews_by_companyNames
from Scraper import getNews_by_topics

world = 'Business'
getNews_by_topics(world, 4, 2024,1 )