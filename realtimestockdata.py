from requests_html import HTMLSession
import pandas as pd
import csv
from datetime import date


# Collecting the stock data from yahoo finance table
def real_time_stock_data(link_url, summary, stock_name):
    url = link_url
    session = HTMLSession()

    r = session.get(url).html

    data = r.find(summary, first=True).text.split()

    # Header of data
    pc_header = ' '.join(data[0:2])
    op_header = data[3]
    bid_header = data[5]
    ask_header = data[9]
    day_range_header = ' '.join(data[13:15])
    year_week_header = ' '.join(data[18:21])
    volume_header = data[24]
    avg_volume_header = ' '.join(data[26:28])
    market_cap_header = ' '.join(data[29:31])
    beta_header = ' '.join(data[32:35])
    pe_ratio_header = ' '.join(data[36:39])
    eps_header = ' '.join(data[40:42])
    earnings_date_header = ' '.join(data[43:45])
    forward_dividend_header = ' '.join(data[52:56])
    ex_dividend_header = ' '.join(data[58:60])
    one_year_target_header = ' '.join(data[63:66])

    header = ['Date', pc_header, op_header, bid_header, ask_header, day_range_header, year_week_header, volume_header,
              avg_volume_header, market_cap_header,
              beta_header, pe_ratio_header, eps_header, earnings_date_header, forward_dividend_header,
              ex_dividend_header, one_year_target_header]

    # Data values
    previous_close = data[2]
    open = data[4]
    bid = ' '.join(data[6:9])
    ask = ' '.join(data[10:13])
    day_range = ' '.join(data[15:18])
    year_week_range = ' '.join(data[21:24])
    volume = data[25]
    avg_volume = data[28]
    market_cap = data[31]
    beta_fiveYear_monthly = data[35]
    PE_ratio_TTM = data[39]
    EPS_TTM = data[42]
    earnings_date = ' '.join(data[45:52])
    forward_dividend_and_yield = ' '.join(data[56:58])
    ex_dividend_date = ' '.join(data[60:63])
    one_year_target_estimate = data[66]
    date_val = str(date.today())

    resultList = [date_val, previous_close, open, bid, ask, day_range, year_week_range, volume, avg_volume, market_cap,
                  beta_fiveYear_monthly, PE_ratio_TTM, EPS_TTM, earnings_date, forward_dividend_and_yield,
                  ex_dividend_date, one_year_target_estimate]

    data_dict = {}

    for i in range(len(header)):
        data_dict[header[i]] = resultList[i]

    return stock_name, header, data_dict, resultList


# Check the last index from the data that we need
def check_index(data):
    for x, i in enumerate(data):
        if i == 'Est':
            print(x)
        else:
            pass


# Append new data into existing csv file of same stock
def append_data(link_url, summary, stock_name, file_name):
    name, header, coca_cola, values_list = real_time_stock_data(link_url=link_url,
                                                                summary=summary,
                                                                stock_name=stock_name)

    with open(file_name, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writerow({
            header[i]: values_list[i] for i in range(len(header))
        })


# Coca-cola
# Create file
name, header, coca_cola, values_list = real_time_stock_data(link_url='https://finance.yahoo.com/quote/KO/', summary='#quote-summary',
                           stock_name='Coca-cola')
df = pd.DataFrame([coca_cola])
df.to_csv('coca-cola_data.csv')

# Appending new data 
coca_cola = append_data(link_url='https://finance.yahoo.com/quote/KO/', summary='#quote-summary',
                        stock_name='Coca-cola', file_name='coca-cola_data.csv')

# Mcdonalds
# Create new file
name, header, mcdonalds, values_list = real_time_stock_data(link_url='https://finance.yahoo.com/quote/MCD/', summary='#quote-summary',
                           stock_name='Mcdonalds')
df = pd.DataFrame([mcdonalds])
df.to_csv('mcdonalds.csv')

# Appending new data
mcdonalds = append_data(link_url='https://finance.yahoo.com/quote/MCD/', summary='#quote-summary',
                        stock_name='Mcdonalds', file_name='mcdonalds.csv')


# Sunway
# Create new file 
name, header, sunway, values_list = real_time_stock_data(link_url='https://finance.yahoo.com/quote/5211.KL?p=5211.KL', summary='#quote-summary',
                           stock_name='Sunway Berhad')
df = pd.DataFrame([sunway])
df.to_csv('sunway berhad.csv')

# Appending new data
sunway = append_data(link_url='https://finance.yahoo.com/quote/5211.KL?p=5211.KL', summary='#quote-summary',
                     stock_name='Sunway Berhad', file_name='sunway berhad.csv')
