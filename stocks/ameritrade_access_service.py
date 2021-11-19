# Import the client
from td.client import TDClient
import json

from stocks.stock_data_access_service import StockDataAccessService

class AmeritradeAccessService(StockDataAccessService):
    def __init__(self) -> None:
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
        
    def authenticate(self): 
        # Login to the session
        self.TDSession.login()
        

# Grab real-time quotes for 'MSFT' (Microsoft)
#msft_quotes = TDSession.get_quotes(instruments=['MSFT'])

# Grab real-time quotes for 'AMZN' (Amazon) and 'SQ' (Square)
#multiple_quotes = TDSession.get_quotes(instruments=['AMZN','SQ'])