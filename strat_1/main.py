# main.py 
from objectCreator import createTechAnalysisObject

'''
This file will be the brains of the trading strategy
'''

def main():
    tech_analysis_count = int(input("Technical Analysis Quantity: "))

    tech_analysis_list = []

    for _ in range(tech_analysis_count):
        print(menu())
        tech_analysis_list.append(createTechAnalysisObject(int(input("Enter technical analysis id")))) 

    onTick(tech_analysis_list) 

def onTick(tech_analysis_list):
    pass 

"""
    Overview: Prints the menu options for technical analysis object creation 
"""
def menu():
    print("Menu")
    print("SD Technical Analysis ID: 1")
    print("Stochastic Oscillator Technical Analysis ID: 2")