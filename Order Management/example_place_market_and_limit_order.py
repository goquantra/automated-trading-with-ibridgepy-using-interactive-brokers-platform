# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:49:59 2018

@author: Quantra
Tested on Python Version 2.7
"""

def initialize(context):
    context.place_order=True     
    
def handle_data(context, data):
    if context.place_order:               
        # Market Order to buy 2 shares of AAPL
        order(symbol('AAPL'), 2)
        
        # Market Order to sell 1 share of AAPL
        order(symbol('AAPL'), 1)
        
        # Limit Order to buy 2 shares of AAPL at limit price of 170
        order(symbol('AAPL'), 2, style=LimitOrder(170))
        
        # Limit Order to sell 2 shares of AAPL at limit price of 180
        order(symbol('AAPL'), -2, style=LimitOrder(180))        
    
        context.place_order=False

    else:
        time.sleep(10)
        display_all()
        end()
     