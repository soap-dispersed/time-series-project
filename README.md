# Time Series Project

## About the Project 

Answering a stakeholder question. 

### Project Description

Dolla, dolla, dolla bills, yall.


### Project Goals

acquire
prep
explore
model

Answer stakeholder question.

### Initial Questions

- Is there a significant correlation between 

- Is there a significant correlation between 

- Is there a significant correlation between 

- Which has a greater effect on _____ values,

- ____ : Could this be a useful categorical feature? 


### Data Dictionary

| Variable          | Meaning                                                                   | values          |
| -----------       | -----------                                                               | -----------     |
|    order_id      | The order number from the order              | N/A |


### Steps to Reproduce

1. You will need an env.py file that contains the hostname, username and password of the mySQL database that contains the Superstore database. The env.py should also contain a function named get_db_url() that establishes the string value of the database url. Store that env file locally in the repository. 
2. clone my repo (including the acquire.py, prepare.py, explore.py, and model.py modules) (confirm .gitignore is hiding your env.py file)
3. libraries used are pandas, matplotlib, seaborn, numpy, sklearn, math. 

### The Plan

1. Acquisition
- In this stage, I obtained Superstore customer data by querying the Codeup MySQL database hosted at data.codeup.com. The original source of this data was db.codeup.com.
2. Preparation
- I cleaned and prepped the data by:
    - removing all observations that included null values
    - renaming columns for readability
    - changing data types where appropriate
    - adding a feature: age (represents age of the property in years)
3. Exploration
- I conducted an initial exploration of the data by examing relationships between each of the potential features and the target
- then explored further, to answer the initial questions posed above
4. Modeling 
- Using varying combinations of features, I tested multiple Ordinary Least Squares (OLS) Regression models. 
- I then chose the model which performed with the smallest error on unseen data.

### How did we do?

We expect that our model will typically predict a value that is within approximately 

### Key Findings:

We determined that the following factors are significant drivers ____:
- number of ___
- number of ___

### Recommendations:

Git money! 

### Next Steps: 

Given more time, I would examine additional features as drivers of home value. Some factors that I would expect to have significant influence include:

    - ball a lot
    - skrrt, skrrrt
    - the size of the garage
    - all day, e'ery day
    
These features could be explored directly, through visualization and statistical testing, or they could be identified through automated features selection techniques such as Recursive Feature Elimination. 

Additionally, since customers are different, I might expect models to perform better which individually focus on a distinct groups.