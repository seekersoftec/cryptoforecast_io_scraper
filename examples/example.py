from cryptoforecast_io_scraper.request import DataReq


# Login to Google. Only need to run this once, the rest of requests will use the same session.
# Instantiate the object
data_req = DataReq()

# Sync Get data in JSON format
get_data = data_req._get_data()

print(get_data)
