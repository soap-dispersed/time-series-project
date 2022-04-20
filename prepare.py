from imports import *

def prep_data(df):
    
    # rename columns: lower case, remove space
    for col in df.columns:
        df = df.rename(columns={col: col.lower().replace(' ', '_')})
        
    # cast date columns as datetime type
    df.order_date = pd.to_datetime(df.order_date)
    df.ship_date = pd.to_datetime(df.ship_date)
        
    # make datetime index
    df.index = df.order_date
    
    # add profit per product column
    df['profit_per_product'] = df.profit / df.quantity
    
    # add sales per product
    df['sales_per_product'] = df.sales / df.quantity
    
    return df

def split_data(df):
    '''
    Splits data into train and test based on year.
    '''
    train = df['2014':'2016']
    test = df['2017']
    return train, test