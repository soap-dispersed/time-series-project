# Time Series Project

## About the Project

The goal is to recommend a product line to the VP of Product fit for expansion. Through thoughtful analysis, we would like to explore if there is a product category that might be particularly profitable and stands out in terms of sales volume. If so, we will attempt to forecast potential gains in profit.

### Project Description

> "Superstore's mission is to be the preferred supplier of workspace solutions; from home-office to cooperate office, we aspire to be the leading expert in workplace solutions for everyone! For this reason, it is important to know whether we are reaching everyone with our products and services. This project will use exploration, modeling, and statistics to identify the best product line for Superstore in regards to expansion efforts and will provide recommendations on where to shift our company focus in order to maintain happy loyal customers while continuing to grow our product base."

Rachel Robbins-Mayweather  
CEO - Superstore

### Project Goals

Answer the VP of Products' question:

    which product line should we expand?

Maximize effectiveness of product line expansion by identifying the product line with:

1. the highest profitability, and
1. the largest amount of room for growth in terms of sales volume.

### Initial Questions

- Is there a product category that has significantly higher profit margins than the others?

- Is there a product category that has significantly lower sales volume than the others?

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
profit_per_item *     |  Profit margin per item  |  float64    |
| * | feature engineered | |

### Steps to Reproduce

1. You will need an env.py file that contains the hostname, username and password of the mySQL database that contains the Superstore database. The env.py should also contain a function named get_db_url() that establishes the string value of the database url. Store that env file locally in the repository. 
2. clone my repo (including the acquire.py, prepare.py, explore.py, and model.py modules) (confirm .gitignore is hiding your env.py file)
3. libraries used are pandas, matplotlib, seaborn, numpy, sklearn, math.

### The Plan

Method:

- Imports used can be found in `imports.py`. (Please ensure libraries are installed for package support).
- Acquire data using SQL. Query Codeup MySQL database.
- Prepare data using time-analysis techniques which frames the data in terms of date of order as the index.
- Explore data using the keen eyes of weathered data scientist and premier tools such as Pandas, Python, Statsmodels, etc...
- Model qualitative predictions based on current trend forecasting.

1. Acquisition

- In this stage, we obtained Superstore customer data by querying the Codeup MySQL database hosted at data.codeup.com. The original source of this data was db.codeup.com.

2. Preparation

- We cleaned and prepped the data by:
    - removing all observations that included null values
    - renaming columns for readability
    - changing data types where appropriate
    - adding a feature: profit_per_item
    - adding a feature: sales_per_item

3. Exploration

- We conducted an initial exploration of the data by examing relationships between each of the features and treated profit as a target
- then explored further, to answer the initial questions posed above
- findings:
    - The Technology product category has higher profit margins than either Office Supplies or Furniture, yet has a much lower total sales volume. We expect that this means there is both high profit potential and room for growth in this category. 

4. Forecasting

- We used data from 2014 - 2016 to determine which product category has the most potential for expansion, then modeled what might have happened if we expanded this category in 2017, and compared those projected profits to the actual 2017 profits. 

### How did we do?

If we had increased technology sales as suggested for the year 2017, it likely would have resulted in an average **monthly increase in profits of 63%**, yielding a **96% increase in total profit for the year**. 

Therefore, we strongly recommend conducting a similar analysis to determine which product line to expand in future years.

### Key Findings

We determined that the technology market has the best oppurtunity for expansion due to:

- highest profits per item
- lowest sales volume

### Recommendations

Profits on technology sales are higher than other markets. Additionally, sales volume is among the lowest categories. Based on profitability and projected room for growth, expansion efforts should be targeted on the technology sector.

### Next Steps

Given more time, I would examine additional features as drivers of product demand. Some factors that I would expect to have significant influence include:

    - regional effects on profits
    - regional effects on profits per market
    - explore office supplies as a secondary contender for expansion
    - predict 2018 values using time-series-analysis

These features could be explored directly, through visualization and statistical testing, or they could be identified through automated features selection techniques such as Recursive Feature Elimination.
