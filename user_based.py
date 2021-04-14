#user based recommnder system
import pandas as pd 
review = pd.read_csv(r"C:\\Users\\Devi Prajwala B S\\Downloads\\recommenders\\recommender_systems\\ratings.csv")

#no_of_attributes = input( " Enter the number of attributes " )



def pearsons_measure ( review, new_user ):
    '''function to calculate the pearson's similarity measure which is needed to determine the closely related users i.e whose likes and dislikes
    follow the same pattern '''
    mean_of_each_users = review.mean(axis = 1)
    #the mean value of ratings of each of the user is calculated which is further needed for the calculation of similarity measure
    print(mean_of_each_users)

new=[1,2,3,4,5,6,7,8,9,10]
pearsons_measure ( review,new )