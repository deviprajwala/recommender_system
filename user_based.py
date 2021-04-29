# implementation of user based recommnder system

import pandas as pd 
import math
#we have imported few packages which include pandas and math. pandas for reading the data, math for the square root function

#review = pd.read_csv(r"C:\\Users\\Devi Prajwala B S\\Downloads\\recommenders\\recommender_systems\\google review ratings.csv")
#The above line is for reading the datast from the path specified

def pearsons_measure ( review, new_user, no_of_attributes, no_of_users ):
    '''function to calculate the pearson's similarity measure which is needed to determine the closely related users i.e whose likes and dislikes
    follow the same pattern '''

    mean_of_each_users = review.mean(axis = 1)
    #the mean value of ratings of each of the user is calculated which is further needed for the calculation of similarity measure
    #print(mean_of_each_users)

    mean = 0 
    #initialisation of the variable

    for count, value in enumerate( new_user ):
        mean = mean + value
    new_user_mean = mean / (count+1) 
    #calculation of the mean for the new user
    
    similarity_measure = []
    #list initialisation

    for i in range ( no_of_users ):
        for count, value in enumerate( new_user ):
            r_user_p = review.loc[i].iat[ count + 1 ]
            numerator = ( float( value ) - new_user_mean ) * ( float( r_user_p ) - mean_of_each_users[i] )
            denominator = math.sqrt( ( value - new_user_mean ) * ( value - new_user_mean ) ) + math.sqrt( ( ( r_user_p - mean_of_each_users[i]) ) * ( ( r_user_p - mean_of_each_users[i]) ) )
        
        similarity_measure.append( numerator / denominator )
    '''the above computational operations are based on the formula of pearson similarity. The ratings of two different users are subtracted by the 
    mean value and multiplied in the numerator and in the denominator the ratings are squared and summation is calculated for each. After getting the
    summation values they are divided to get the similarity measure'''
                    
    max_value = max( similarity_measure )
    #the maximum similarity is computed

    max_index = similarity_measure.index( max_value )
    #index of the maximum value is calculated

    if( review.loc[max_index].iat[10] >= 2.5 ):
        '''if the user whoose pattern of likes and dislikes are in close similarity is found and if his rating for the 10th place is greater than 2.5 there
        are chances that new user may also like the 10th place'''
       
        print("yes the 10th place can be recommended")
    else:
         print("no the 10th place cannot be recommended")
    

       
#new=[1,2,3,4,5,4,3,2,1]
#no_of_attributes = 10
#no_of_users = 5456
#pearsons_measure ( rating, new, no_of_attributes, no_of_users )
''' this is how the function has to be called for the implementation of the user based similarity, rating the dataframe, 10 is the number of items,
5456 is the number of users and new_user is the list containing the rating for the nine items'''