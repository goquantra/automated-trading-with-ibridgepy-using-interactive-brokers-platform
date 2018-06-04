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
        order(symbol('AMZN'), -2, style=LimitOrder(1600))         
        context.place_order = False      
    
    # open_orders is a dictionary 
    #    keyed by security object, 
    #    with values that are lists of orders object.
    open_orders = get_open_orders()
    
    if open_orders:
        # iterate over the dictionary 
        # iterate over each securities
        for security in open_orders:            
            print "Open Orders for %s" % (security.symbol)
            # iterate over the open orders  
            for oo in open_orders[security]:            
                message = '{filled}/{amount} shares filled'  
                print message.format(amount=oo.amount, filled=oo.filled)
                
    else:
        print "No Open Orders"    
    end()


    


    
    




  