from imports import *

canva_palette = ['#FFB000', '#375F00', '#707E00', '#B39B00', '#002729']

def create_projections_1(test):
    
    hypo_tech_sales_17 = test[test.category == 'Technology']
    hypothetical_17 = pd.concat([test, hypo_tech_sales_17])
    
    projections = pd.DataFrame()
    projections['actual_2017'] = test.resample('M')['profit'].sum()
    projections['projected_2017'] = hypothetical_17.resample('M')['profit'].sum()
    projections['difference'] = projections.projected_2017 - projections.actual_2017
    projections['difference_pct'] = projections.difference / projections.actual_2017
    projections['rolling_total_actual'] = projections.actual_2017.cumsum()
    projections['rolling_total_projected'] = projections.projected_2017.cumsum()
    projections.index = projections.index.strftime('%b')
    projections.index.name = 'month'
    
    return projections

def monthly_profit_barplot(projections):
    projections_melted = projections[['actual_2017', 'projected_2017']].melt(value_name='sales', ignore_index=False)

    plt.figure(figsize=(12,8)) 
    sns.barplot(data=projections_melted, x=projections_melted.index, y='sales', hue='variable', 
                palette=canva_palette, ec='black')
    plt.title('Monthly Profit 2017', fontsize=24, color='#002729')
    plt.ylabel('Profit', fontsize=18, color='#002729')
    plt.xlabel(None)
    plt.xticks(fontsize=14, color='#002729')
    plt.yticks(fontsize=14, color='#002729')
    plt.legend(loc='lower left', fontsize=18)
    ax = plt.gca()
    ax.set_yticklabels([f'${tick:,.0f}' for tick in ax.get_yticks()])
    plt.savefig('fig_monthly_profit_barplot.jpeg')
    plt.show()

def create_projections_2(test):
    hypo_tech_sales_17 = test[test.category == 'Technology']
    hypo_tech_sales_17 = hypo_tech_sales_17[hypo_tech_sales_17.discount <= .35]
    hypothetical_17 = pd.concat([test, hypo_tech_sales_17])
    projections = pd.DataFrame()
    projections['actual_2017'] = test.resample('M')['profit'].sum()
    projections['projected_2017'] = hypothetical_17.resample('M')['profit'].sum()
    projections['difference'] = projections.projected_2017 - projections.actual_2017
    projections['difference_pct'] = projections.difference / projections.actual_2017
    projections['rolling_total_actual'] = projections.actual_2017.cumsum()
    projections['rolling_total_projected'] = projections.projected_2017.cumsum()
    projections.index = projections.index.strftime('%b')
    projections.index.name = 'month'
    
    return projections

def total_profit_barplot(projections):
    plt.figure(figsize=(12,8))
    sns.lineplot(data=projections, x=projections.index, y='rolling_total_actual', 
                 color='#707E00', label='Actual', lw=6)
    sns.lineplot(data=projections, x=projections.index, y='rolling_total_projected', 
                 color='#FFB000', label='Projected', lw=6)
    plt.title('Total Profit 2017', fontsize=24, color='#002729')
    plt.ylabel('Total Profit', fontsize=18, color='#002729')
    plt.xlabel(None)
    plt.xticks(fontsize=14, color='#002729')
    plt.yticks(fontsize=14, color='#002729')
    ax = plt.gca()
    ax.set_yticklabels([f'${tick:,.0f}' for tick in ax.get_yticks()])
    plt.savefig('fig_total_profit_2017.jpeg')
    plt.show()