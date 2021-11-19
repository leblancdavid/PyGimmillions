from stocks import ameritrade_access_service

service = ameritrade_access_service.AmeritradeAccessService()

service.initialize('C:/Stocks/td_config.json')

service.authenticate()

service.get_daily_stock_data('GNUS')