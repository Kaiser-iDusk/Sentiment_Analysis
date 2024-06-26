import google.generativeai as genai
import textblob
from textblob import TextBlob
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
stop = stopwords.words('english')

model = genai.GenerativeModel('gemini-1.5-flash')
api_key = 'AIzaSyCNfiNk7h_UJPSa248MB5WIPiJlzThptSE'
genai.configure(api_key=api_key)

class Pipeline:
    def fetch(self, url):
        req = requests.get(url)
        if req.status_code == 200:
            soup = BeautifulSoup(req.text, 'html.parser')
            divs = soup.find_all('li', attrs={'class': 'y-css-1jp2syp'}, recursive=True)
            reviews = []
            for div in divs:
                review = div.find('p', recurive = False)
                if review:
                    reviews.append(review.text)
            if len(reviews) == 0:
                return False, None
            return True, pd.DataFrame(reviews, columns=['reviews'])
        else:
            return False, None
        
    def clean(self):
        self.df['lower'] = self.df['reviews'].apply(lambda x: " ".join(word.lower() for word in x.split())) 
        self.df['no_stop'] = self.df['lower'].apply(lambda x: " ".join(word for word in x.split() if word not in (stop)))
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        self.df['no_punct'] = self.df['no_stop'].apply(lambda x: "".join(char for char in x if char not in punc))
        self.df['clean_reviews'] = self.df['no_punct'].apply(lambda x: " ".join(lemmatizer.lemmatize(word) for word in x.split()))
        self.df['polarity'] = self.df['clean_reviews'].apply(lambda x: TextBlob(x).sentiment[0])
        self.df['subjectivity'] = self.df['clean_reviews'].apply(lambda x: TextBlob(x).sentiment[1])
        self.df.drop(columns=['lower', 'no_stop', 'no_punct', 'clean_reviews'], inplace=True)
    
    def predict(self, url):
        _, ret = self.fetch(url)
        if not _:
            return None
        self.df = ret 
        self.clean()
        output = self.generate()
        return str(output)
    
    def generate(self):
        pol, sub = self.df['polarity'].mean(), self.df['subjectivity'].mean()
        response = model.generate_content(f'Write a feedback report for a product (around 50-75 words) that has following sentiment metrics: polarity={pol} , subjectivity= {sub}. The feedback should be to the point and should not reveal any metric. Also try to decide whether you would have brought the product seeing the scores and why?')
        return response.text 