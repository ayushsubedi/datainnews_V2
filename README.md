# DATA IN NEWS
![](https://github.com/ayushsubedi/datainnews_V2/blob/main/datainnews_v2/static/img/showcase.png?raw=true)

How journalists use data in their reporting or in their writing can be viewed as a reflection of the country’s demand for statistics and data. Back in 2020, I developed an indicator model (for The World Bank) to assess the use of data by Nepali news portals based on the methodology proposed by Klein, Galdin, and Mohamedou 2016. 

The results from the project was used in the research article published at http://documents1.worldbank.org/curated/en/805261601023506163/pdf/Use-of-Data-in-the-Private-Sector-of-Nepal-The-Current-State-and-Opportunities-in-Finance-Education-and-the-Media.pdf

As of 9th February 2020, the results showed that very few news articles indicate the source of data or mention development indicators. However, articles that discuss data, reports, research, statistics, and related topics do critically engage with these ideas.

Unfortunately, the data collection process was halted because we ran out of our AWS Activate for Startups credits. 


![](https://github.com/ayushsubedi/datainnews_V2/blob/main/dataflow.png?raw=true)

## TODOS
- [x] create a simple architecture diagram
- [x] curate a list of twitter handles of Nepali newspapers that put URL to their newspapers
- [x] use twint to create datasets (historic)
- [x] check if url is present, url does not 404, and url belongs to the publisher
- [x] use Newspaper to collect important information (author, etc) and complete the dataset
- [x] research dash, swifter and pandarallel
- [ ] optimize regular expression functions (if possible this should be performed during scraping)
- [ ] create a sqlite database to hold access information (and design schema around other meta)
- [ ] add checkpoints (using twint resume or build it manually)

## POC
- [ ] create a full working version of the product (including Github Actions, using only one newspaper)
- [x] research downloading twint as pandas to merge with previous data

## Twitter handles
- @kathmandupost
- @thehimalayan
- @NepaliTimes
- @OnlineKhabar_En
- @RepublicaNepal


# The Frugal way

- This project leverages on Github Actions for scheduling and scraping purposes.
- This project is hosted on Heroku free tier
- The free domain name is provided by Freenom
- Relies on cloudflare free https or certbot (free)
- Uses amazing open source projects, primariliy (Twint, Newspaper) etc 
