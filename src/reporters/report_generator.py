import pandas as pd
import matplotlib.pyplot as plt

def generate_report():



    summary = pd.read_csv('summary_by_category.csv')


    with pd.ExcelWriter('category_report.xlsx', engine='xlsxwriter') as writer:
        summary.to_excel(writer, sheet_name='Summary', index=False)
        workbook  = writer.book
        worksheet = writer.sheets['Summary']


        price_fmt = workbook.add_format({'num_format': '£#,##0.00'})
        stock_fmt = workbook.add_format({'num_format': '0'})
        worksheet.set_column('B:B', 20)   # category
        worksheet.set_column('C:C', 15, price_fmt)  # avg_price
        worksheet.set_column('D:D', 15, stock_fmt)  # total_stock

    print("Excel report saved to category_report.xlsx")


    plt.figure(figsize=(10, 6))
    plt.bar(summary['category'], summary['avg_price'])
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Average Price (£)')
    plt.title('Average Book Price by Category')
    plt.tight_layout()
    plt.savefig('avg_price_by_category.png')
    plt.close()

    print("Bar chart saved to avg_price_by_category.png")
