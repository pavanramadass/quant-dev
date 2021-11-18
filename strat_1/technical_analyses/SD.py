# SD.py

from dataHandler import DataHandler 

'''
This class will find the nth derivative of the market.
'''

class SD:

    def __init__(self, time_interval, derivative):
        self.time_interval = time_interval 
        self.derivative = derivative 
        self.dataHandler = DataHandler() 
    

    """
        Overview: Sets the time interval for how much data points are needed 

        Parameters:
            - time_interval: (int) the time interval of how many data points are needed from the market
    """
    def setTimeInterval(self, time_interval):
        self.time_interval = time_interval 


    """
        Overview: returns the time interval 

        Returns:
            - (int) the time interval 
    """
    def getTimeInterval(self):
        return self.time_interval
    

    """
        Overview: Calculates the slope of two data points

        Parameters: 
            - point1 = (List) the first data point
            - pint2 = (List) the second data point 
        
        Returns:
            - A list containing the second data point's x-value and the new y 
    """
    def calculateSlope(point1, point2):
        x1, y1, x2, y2 = point1[0], point1[1], point2[0], point2[1]

        numerator = x2 - x1 
        denominator = y2 - y1 

        return [x2, numerator / denominator]


    """
        Overview: Calculates the nth derivative of a list of data

        Parameters: 
            - time_interval = (int) the length of candles 
            - current_time = (int) the current time this function is called by the SD object
            - candle_choice = (str) the choice of candle data to receive from the data handler object
        
        Returns:
            - (List) List of nth derivatives over the stock data 
    """
    def calculateDerivative(self, time_interval, current_time, candle_choice):
        data = self.dataHandler.getData(time_interval + self.derivative, current_time, candle_choice)
        derivative_list = data 

        for i in range(0, self.derivative):
            for j in range(1, len(derivative_list)):
                calculated_derivative = self.calculateSlope(derivative_list[j-1], derivative_list[j])
                derivative_list[j] = calculated_derivative 
            del derivative_list[0] 
        
        return derivative_list 