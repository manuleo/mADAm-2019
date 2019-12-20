# -*- coding: utf-8 -*-

"""LP Solver Diet Europe"""

import pandas as pd
import numpy as np
import picos as pic


food_opt_distribution_df = pd.read_pickle('data/processed/food_opt_distribution_df.pkl')
final_prices = pd.read_pickle('data/processed/final_prices.pkl')
prod_diet_final =  pd.read_pickle("data/processed/prod_diet_final.pkl")
prod_diet_final = prod_diet_final.sort_values(by="Product")


def LPSolverDietEurope(eu_country):
    '''
    Solver for Europe diet. Find kilocalories quantities to send to each African countries. It creates the optimal diet
    '''
    country_giveup_val = food_opt_distribution_df.loc[eu_country].values
    country_giveup_index = food_opt_distribution_df.loc[eu_country].index
    
    prices_val = final_prices.loc[eu_country].values.reshape(-1,1)
    prices_index = final_prices.loc[eu_country].index
    
    prod_diet_val = prod_diet_final.to_numpy()/10**-6
    prod_diet_index = prod_diet_final.index
    
    prob = pic.Problem() #initalize convex problem
    Y = prob.add_variable('Y', (prices_val.size,country_giveup_val.size)) #definition of decision matrix of variables nxm
    
    obj = pic.sum(prices_val.T * Y) #define obj function 
    prob.set_objective("min", obj) #set objective function 
    
    #Initialize constraints
    constraints = []

    #Define non-negativity constraint
    constraints.append(prob.add_constraint(Y>=0))

    #Define constraints proteins,carbs and fats
    #Define shares of proteins,carbs and fat as an absolute variable (not subject to optimization)
    shares = np.array([0.55,0.25,0.2])
    for i in range(0,country_giveup_val.size):
         for j in range(0,shares.size):
            constraints.append(prob.add_constraint(Y[:,i].T*prod_diet_val[:,j].reshape(-1,1)==shares[j]*country_giveup_val[i])) 
    #Define constraints to provide an upper bound (every product has to be sent at most to cover the 20% of the final demand) 
    for i in range(0,country_giveup_val.size):
        for j in range(0,prices_val.size):
            constraints.append(prob.add_constraint(pic.sum(Y[j,i]*prod_diet_val[j,:].reshape(1,-1))<=0.355*country_giveup_val[i])) 
            constraints.append(prob.add_constraint(pic.sum(Y[j,i]*prod_diet_val[j,:].reshape(1,-1))>=0.0001*country_giveup_val[i]))

    #Solving problem with gurobi solver (License available for free academic use)
    solution = prob.solve(verbose=0, solver = 'gurobi')
    Y_opt_diet = Y.value   
    
    result_diet = np.array(Y_opt_diet)
    result_diet_df= pd.DataFrame(data=result_diet, index = prod_diet_index)
    result_diet_df.columns = country_giveup_index
    return result_diet_df
