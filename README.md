<h2>This project aims to get a polarity and subjectivity score of any Yelp (website) product review.</h2>

<p>Most of us think should we buy a product or not or maybe should we hire a particular electrician or not? This project helps you out by getting a sentiment analysis of all the reviews of that particular service on Yelp and NLP technique to provide you a score of polarity and subjectivity. But a layman cannot infer scores of such a prediction and here comes Gemini API that uses the score to provide a layman terms understanding of the scores and a suggesting action of whether you should buy it or not. Also using a database you can see the top 5 services with descending order of polarity scores that other users have viewed.</p>
Tech stacks used:
<ul>
  <li>Python</li>
  <li>Flask</li>
  <li>Flask WTForms</li>
  <li>SQLAlchemy</li>
  <li>Gemini API</li>
  <li>NLTK</li>
  <li>Core ML libraries</li>
</ul>
The code oprates in 3 primary modules: 
<ul>
  <li>It web scrapes all reviews of a particular product on Yelp. </li>
  <li>It uses Machine Learning model provided by TextBlob to provide inference on the sentiment metrics.</li> 
  <li>Finally it passes the sentiment metrics to Google Gemini API to get a detailed inference.</li>
</ul>
<br>
Link: https://sentimento-vvpx.onrender.com/
<br>
The project is operating stably but improvements and suggestions are welcome.
