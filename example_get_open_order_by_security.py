# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:49:59 2018

@author: Quantra
Tested on Python Version 2.7
"""

def initialize(context):
    context.place_order = True
    
def handle_data(context, data):
    if context.place_order == True:  
        order(symbol('AAPL'), 20, style=LimitOrder(175))         
        order(symbol('AAPL'), -10, style=LimitOrder(180))         
        context.place_order = False      
  
    # Get open orders for a AAPL    
    open_orders = get_open_orders(symbol('AAPL'))    
    if open_orders:          
        print "Open Order(s)"
        # iterate over the open orders
        for oo in open_orders:  
            message = 'AAPL: {filled}/{amount} shares filled'  
            print message.format(amount=oo.amount, filled=oo.filled)            
    else:
        print "No Open Orders"    
    end()

    


    
    




  