from technical_analyses import SD 
from main import menu 

# lists the valid object types that can be created 
types = [1]

"""
    Overview: Creates the technical analysis' objects and returns them to the caller

    Parameters:
        - type: (int) the desired technical analysis' object's id 
    
    Returns:
        - (Object) the created technical analysis object 
"""
def createTechAnalysisObject(type):
    while type not in types:
        print(menu())
        type = int(input("Incorrect type. Enter technical analysis type: "))
    if type == 1:
        time_interval = int(input("Enter time interval for SD: "))
        derivative = int(input("Enter derivative for SD: "))
        sd = SD(time_interval, derivative) 
        return sd 