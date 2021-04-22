#user based recommnder system
import pandas as pd 
import math
rating = pd.read_csv(r"C:\\Users\\Devi Prajwala B S\\Downloads\\recommenders\\recommender_systems\\item_rating.csv")
#rating.iat[1,4] = rating.iat[1,4].astype(float)
#no_of_attributes = input( " Enter the number of attributes " )

mean_of_each_users = rating.mean(axis = 1)
#print(rating)

def mean_adjusted_matrix( no_of_attributes, no_of_users ):
    '''for i in range(no_of_users):
        for j in range(1,no_of_attributes+1):
            rating.loc[i].iat[j] = float(rating.loc[i].iat[j]) - mean_of_each_users[i]
            #print(i,j)'''

    rating.drop ('Users', axis='columns', inplace=True)
    rate = rating.transpose(copy = 'True')  
    #print(rate)
    for x in rate.columns:
        rate[x] = rate[x] - rate[x].mean()
 
    print(rating)

mean_adjusted_matrix(5,4)