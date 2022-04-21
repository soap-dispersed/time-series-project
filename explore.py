from imports import *

canva_palette = ['#FFB000', '#375F00', '#707E00', '#B39B00', '#002729']


def sales_volume_by_category(train):
    plt.figure(figsize=(12,8))
    sns.barplot(data=train, x='category', y='quantity', 
                estimator=sum, ci=None, ec='black', palette=canva_palette)
    plt.title('Sales Volume by Category', fontsize=24)
    plt.ylabel('Total Sales Volume', fontsize=18)
    plt.xlabel('Product Category', fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.savefig('sales_volume_by_category.jpeg')
    plt.show()

def profit_per_product_by_category(train):
    plt.figure(figsize=(12,8))
    sns.barplot(data=train, x='category', y='profit_per_product', 
                ci=None, ec='black', palette=canva_palette)
    plt.title('Average Profit-per-Product by Category', fontsize=24)
    plt.ylabel('Average Profit-per-Product', fontsize=18)
    plt.xlabel('Product Category', fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.savefig('profit_per_product_by_category.jpeg')
    plt.show()

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