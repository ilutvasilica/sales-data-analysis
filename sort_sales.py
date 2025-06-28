# sort_sales.py

def sort_by_revenue(sales_data):
    return sorted(sales_data, key=lambda x: x['revenue'], reverse=True)
