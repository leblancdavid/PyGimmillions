
class StockData:
    def __init__(self, ticker, date, period, open, close, high, low, volume, previous_close) -> None:
        self.ticker = ticker
        self.date = date
        self.period = period
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.volume = volume
        self.previous_close = previous_close
        self.signal = 0.0
     
    def percent_period_change(self):
        if self.open == 0.0:
            return 0.0
        
        return (self.close - self.open) / self.open
    
    def percent_period_range(self):
        if self.low == 0.0:
            return 0.0
        
        return (self.high - self.low) / self.low
    
    def range(self):
        return self.high - self.low
    
    def average(self):
        return (self.high + self.low + self.open + self.close) / 4.0
    
    def percent_change_high_to_open(self):
        if self.open == 0.0:
            return 0.0
        
        return (self.high - self.open) / self.open
    
    def percent_change_high_from_previous_close(self):
        if self.previous_close == 0.0:
            return 0.0
        
        return (self.high - self.previous_close) / self.previous_close
    
    def percent_change_low_from_previous_close(self):
        if self.previous_close == 0.0:
            return 0.0
        
        return (self.low - self.previous_close) / self.previous_close 
    
    def percent_change_open_from_previous_close(self):
        if self.previous_close == 0.0:
            return 0.0
        
        return (self.open - self.previous_close) / self.previous_close 
    
    def percent_change_from_previous_close(self):
        if self.previous_close == 0.0:
            return 0.0
        
        return (self.close - self.previous_close) / self.previous_close 
        