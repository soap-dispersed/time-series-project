# Time Series Project

## About the Project 

The goal is to make a reccomendation to VP of Product as to which product line would be best to invest effort into expanding.
Through thoughtful analysis, we would like to conclude on whether there is a product category that might be particularly profitable, stands out in terms of sales volume, and how different customer segments respond to each, respectively.

### Project Description




### Project Goals

acquire
prep
explore
model

Answer stakeholder question.

### Initial Questions

- Which product line should we expand?

- Is there a product category that is particularly profitable for us?

- Does one or another stand out in terms of sales volume?

- Does this vary by customer segment?

### Data Dictionary

|  Variables             |    Definition                              |    DataType             |
| :--------------------:   | :----------------------------------------: | :--------------------: |
order_date (index)    |  Date order was placed                          |  datetime64[ns]    |
order_id              |  Order identifier assigned to each product name for each order | object |
ship_date             |  Date order was shipped                         | datetime64[ns]       |
ship_mode             |  Mode of shipping for delivery:  'Standard Class', 'First Class', 'Second Class', 'Same Day'  | object      |
segment               |  Customer type: Consumer, Cooperate, Home Office  |  object     |
country               |  Country to which shipment was delivered: 'United States'  |    object   |
city                  |  City to which shipment was delivered  |  object    |
state                 |  State to which shipment was delivered  |  object    |
postal_code           |  Postal code to which shipment was delivered   |  float64   |
sales                 |  Sale total for product id * quantity in given order ($USD)  | float64     |
quantity              |  Total number of specified product ordered  | float64     |
discount              |  Percentage of discount applied to order in decimal form  | float64     |
profit                |  Sales - Product Cost  | float64     |
category              |  Category the product belongs to  | object    |
sub-category          |  Subcategory the product belongs to  |  object    |
customer_name         |  Name of customer   | object     |
product_name          |  Name of product  |  object    |
region_name           |  General area of US where order was placed: 'Central', 'South', 'East', 'West'  |  object    |
days_to_ship *        |  Number of days from order_date to ship_date  |  int64    |
* feature engineered

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
    - adding a feature: profit_per_item
3. Exploration
- I conducted an initial exploration of the data by examing relationships between each of the features and the treated profit as a target
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