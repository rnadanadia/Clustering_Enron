# Clustering_Enron


## Team:
- Tim Strauven
- Kivanc Gunduz
- Anjali Tiwari
- Rosyidah Nadia

## Description:

Analize the Enron email dataset, this is a set of :
- 500 000 messages
- 150 users, mostly senior management of Enron
- Organized into mailbox folders
- 2.5 GB uncompressed
- link: https://www.cs.cmu.edu/~enron/
---
## Deliverables:

 Facilitate the exploration of the dataset by:
-  Organising it by topic (clustering, topic modeling)
- Without being overwhelming (small number of clusters)
- Remaining as relevant as possible
- In practice, the clustering may need to be hierarchical:
- Start fuzzy and specify more and more
- Build a tool as user friendly and demonstrable as possible:
- (deployed) web interface > command line > notebook (still good though)
- 10 minutes demo / per team on Friday @ 14.00
- Everybody will present
---

## Project Roadmap (Backlog):

- [X] Download data
- [X] Create Github Repo
- [X] First look at data
- [ ] Add literature research in fraud business to provide a different perspective or an additional analysis of the current project. This can help identify gaps in the current knowledge and highlight future directions. 
- [ ] Data cleaning from half of million emails. 
- [ ] Data preprocessing 
- [ ] Decide on what algorithm to use: Kmeans or LDA (topic modeling) look like good candidates
- [ ] user interface

 - https://github.com/rnadanadia/Clustering_Enron/wiki 
## Daily sprint items:

### 1. Monday
   ***General***
   - [X] Download data
   - [X] Create Github Repo
   - [X] First look at data
   - [X] Brainstorm for ideas and approach at12h05
   
   ***Jobdesk***
   - [X] Tim : Creating dataset in CSV 
   - [X] Kivanc : Analysing K-means Clustering and vectorization
   - [X] Anjali : Exploring Enron Case and the structure of Topic Modelling 
   - [X] Nadia : Research in Clustering and Topic Modelling
   
   ***Challenge for today***
   - Which clustering method to use? --answer : topic modelling and K- means.
   - What is the expectancy of the end result? --answer :  data visualization of topic modelling and K-means.
   
### 2. Tuesday
   ***General***
   - [X] Brainstorming at 09.00 and 12.00
   - [X] Data cleaning
   - [X] Literature review in Clustering method
   
   ***Jobdesk***
   - [X] Tim : Literature review and applying Clustering method in csv file
   - [X] Kivanc : Literature review and applying Clustering method in csv file
   - [X] Anjali : Providing a clear stepstone to reach the goal and data cleaning, topic modelling (preprocessing, model application and evaluation)
   - [X] Nadia : Data Cleaning and visualization
   - [X] In the afternoon all member is working on data visualization based on Kmeans and LDA models. 
   
   ***Challenge for today***
   - Tim : To create a first cluster, using Kmeans and plotting and to understand clustering process. 
   - Kivanc : To implemente time and understanding clustering.
   - Anjali: Overall understand all steps of preprocessing for topic modelling but facing some issue in  visualizing  model (showing some error).
   - Nadia : Data visualization in LDA is empty, might caused by the data process.
   
   ***Next day goal **
   - Taking out insights from that (improvement in data processing if required) and compare insights of both models (how it is making sense)  and done with modelling part and start user interface (if possible) 
   
   - [X] Tim : taking out insights from that (improvement in data processing if reauired) .......
   - [X] Kivanc : taking out insights from that (improvement in data processing if reauired) .....
   - [X] Anjali : solving visualization issue, taking out insights from that (improvement in data processing if reauired), find optimal no. of topics 
   - [X] Nadia : taking out insights from that (improvement in data processing if reauired) ...... 
   
### 3. Wednesday
   ***General***
   - [X] Brainstorming at 09.00 and 12.00
   - [ ] Deadline : 2 model run  and comparing/ analysing both models outcome based on visulaization (improve model if required)

   ***Jobdesk***
   - [X] Tim : Get AgglomerativeClustering to work for the whole dataset and review the LDA codes to improve the code
   - [X] Kivanc : Implemented the KMeans Clustering for whole dataset
   - [X] Anjali : Topic modelling visualisation and start the user interface
   - [X] Nadia : Better visualisation of the the first 10.000 rows of dataset 
   
   ***Challenge for today***
   - Tim : Hyperparameter tuning of LDA model
   - Kivanc : Mananging whole dataset
   - Anjali : Challenge in model output 
   - Nadia : Got some error for visualisation but solved with restarting Vscode
   
   ***Next day goal **
   - Preparing the powerpoint user interface 
   
### 4. Thursday
   ***General***
   - [ ] Brainstorming at 09.00 and 12.00
   - [ ] Deadline : User interface 

   ***Jobdesk***
   - [X] Tim : Agglomerative Clustering to make a connection between tokenize words and email and user interface using Streamlit
   - [X] Kivanc : User interface and LDA data visualization
   - [X] Anjali : Data visualisation for 50,000 dataset and slide presentation.
   - [X] Nadia : Working on bigger size of dataset and slide presentation. Compared to yesterday, the Topic Modelling's result is less interesting. In rough conclusion, smaller 
                 dataset will give a better overview
   
   ***Challenge for today***
   - Data visualization, bigger dataset means longer time to proces, and user interface preparation
   
   ***Next day goal **
   - Preparing the user interface 
    
### 5. Friday
   ***General***
   - [X] Brainstorming at 09.00 and 12.00
   - [X] Deadline : Presentation 

   ***Jobdesk***
   - [X] Tim : User Interface
   - [X] Kivanc : User Interface
   - [X] Anjali : Powerpoint
   - [X] Nadia : Powerpoint
   
   ***Challenge for today***
   - To deliver good and understandable content for audience
    
## Technologies

- Programming Language: Pyhton
- IDE: VS Code
- Presentation: Jupyter Notebook
- Communication: Discord
