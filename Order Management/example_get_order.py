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
        context.orderId = order(symbol('AAPL'), 20, style=MarketOrder())             
        context.place_order = False      
          
    order_aapl = context.portfolio.orderStatusBook[context.orderId]    
    message = '{status}: {filled}/{amount} shares filled'  
    print message.format(status=order_aapl.status, 
                         amount=order_aapl.amount, 
                         filled=order_aapl.filled)
    
    if order_aapl.status == 'Filled':
        print "The order is filled with average price of %s price" % (order_aapl.avgFillPrice)
        end()
    


    
    




  