def prep_data(df):
    for col in df.columns:
        df = df.rename(columns={col: col.lower().replace(' ', '_')})
    return df