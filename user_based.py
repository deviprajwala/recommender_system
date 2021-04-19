#user based recommnder system
import pandas as pd 
import math
review = pd.read_csv(r"C:\\Users\\Devi Prajwala B S\\Downloads\\recommenders\\recommender_systems\\ratings.csv")

#no_of_attributes = input( " Enter the number of attributes " )



def pearsons_measure ( review, new_user, no_of_attributes, no_of_users ):
    '''function to calculate the pearson's similarity measure which is needed to determine the closely related users i.e whose likes and dislikes
    follow the same pattern '''
    mean_of_each_users = review.mean(axis = 1)
    #the mean value of ratings of each of the user is calculated which is further needed for the calculation of similarity measure
    #print(mean_of_each_users)

    mean = 0 
    for count,value in enumerate(new_user):
        mean = mean + value
    new_user_mean = mean / (count+1) 
    #print(mean)
    
    #s = review.loc[0].iat[0]
    #print(s)

    similarity_measure = []
    for i in range (no_of_users):
        #for j in range (1,no_of_attributes+1):
            for count,value in enumerate( new_user ):
                r_user_p = review.loc[i].iat[count+1]
                numerator = ( float(value) - new_user_mean ) * ( float(r_user_p) - mean_of_each_users[i])
                denominator = math.sqrt( ( value - new_user_mean ) * ( value - new_user_mean ) ) + math.sqrt( ( ( r_user_p - mean_of_each_users[i]) ) * ( ( r_user_p - mean_of_each_users[i]) ) )
            similarity_measure.append( numerator / denominator )
    #print(similarity_measure)        
               

    max_value = max( similarity_measure )
    max_index = similarity_measure.index( max_value )

    if( review.loc[max_index].iat[10]>=2.5):
        print("yes the 10th place can be recommended")
       
    


new=[1,2,3,4,5,6,7,8,9]
pearsons_measure ( review, new, 10, 4 )