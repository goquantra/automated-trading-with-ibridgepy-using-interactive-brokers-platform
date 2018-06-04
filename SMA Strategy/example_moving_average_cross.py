# -*- coding: utf-8 -*-
'''
There is a risk of loss when trading stocks, futures, forex, options and other
tradeable finacial instruments. Please trade with capital you can afford to 
lose. Past performance is not necessarily indicative of future results. 
Nothing in this computer program/code is intended to be a recommendation and/or 
solicitation to buy or sell any stocks or futures or options or any 
tradable securities/financial instruments. 
All information and computer programs provided here is for education and 
entertainment purpose only; accuracy and thoroughness cannot be guaranteed. 
Readers/users are solely responsible for how to use these information and 
are solely responsible any consequences of using these information.

If you have any questions, please send email to IBridgePy@gmail.com
'''

import pandas as pd

def initialize(context):
    context.run_once=False # To show if the handle_data has been run in a day
    context.security=symbol('AAPL') # Define a security for the following part
    
def handle_data(context, data):
    sTime=get_datetime() 
    # sTime is the IB server time. 
    # get_datetime() is the build-in fuciton to obtain IB server time 
    if sTime.weekday()<=4:
        # Only trade from Mondays to Fridays
        if sTime.hour==13 and sTime.minute==35 and context.run_once==True:
            # 2 minutes before the market closes, reset the flag
            # get ready to trade
            context.run_once=False
        if sTime.hour==13 and sTime.minute==36 and context.run_once==False:
            # 1 minute before the market closes, do moving average calcualtion
            # if MA(5) > MA(15), then BUY the security if there is no order
            # Keep the long positions if there is a long position
            # if MA(5) < MA(15), clear the position
            data=request_historical_data(context.security, '1 day', '20 D')
            mv_5=data.close.rolling(5).mean().iloc[-1]            
            mv_15=data.close.rolling(15).mean().iloc[-1] 
            if mv_5>mv_15:         
                orderId=order_target(context.security, 100)
                order_status_monitor(orderId, target_status='Filled')
            else:
                orderId=order_target(context.security, 0)
                order_status_monitor(orderId, target_status='Filled')
            context.run_once=True    
#       end()