# Import the client
from td.client import TDClient
from datetime import datetime
import json

from stocks.stock_data_access_service import StockDataAccessService

class AmeritradeAccessService(StockDataAccessService):
    def __init__(self) -> None:
        self.is_initialized = False
        self.is_authenticated = False
        super().__init__()
    
    def initialize(self, configFileName):
        configFile = open(configFileName)
        configData = json.load(configFile)

        # Create a new session, credentials path is required.
        self.TDSession = TDClient(
            client_id = configData['clientId'],
            redirect_uri = configData['redirectUri'],
            credentials_path = configData['credentials']
        )

        configFile.close()
        
        self.is_initialized = True
        
    def authenticate(self): 
        # Login to the session
        self.is_authenticated = self.TDSession.login()
    
    def get_daily_stock_data(self, ticker, years = 1):
        if not self.is_authenticated: 
            return []
        
        price_history = self.TDSession.get_price_history(ticker, period_type='year', period=str(years), frequency_type='daily',frequency='1')
        
        return price_history

# Grab real-time quotes for 'MSFT' (Microsoft)
#msft_quotes = TDSession.get_quotes(instruments=['MSFT'])

# Grab real-time quotes for 'AMZN' (Amazon) and 'SQ' (Square)
#multiple_quotes = TDSession.get_quotes(instruments=['AMZN','SQ'])