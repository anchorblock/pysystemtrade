import pandas as pd
def buy_and_hold(price):
    pred = pd.Series(1, index = price.index)
    return pred

def buy_and_hold_with_risk_scaling(price, risk):
    std = 0.16
    multiplier = 50
    capital = multiplier * price[0]
    N = (capital * risk) / (multiplier * price * std)
    
    pred = pd.Series(N, index = price.index)
    return pred

def buy_and_hold_with_variable_risk_scaling(price, risk, std=0.1002):
    multiplier = 50
    capital = multiplier * price[0]
    
    ret = price.pct_change()
    weighted_ret = ret.ewm(32).std()
    
    sigma = (0.3 * std) + (0.7 * weighted_ret)
    
    N = (capital * risk ) / (multiplier * price * sigma)
    pred = pd.Series(N, index = price.index)

    return pred