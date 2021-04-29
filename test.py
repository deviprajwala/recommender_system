from recommender_systems import user_based,item_based

import pandas as pd 
review = pd.read_csv(r"C:\\Users\\Devi Prajwala B S\\Downloads\\recommenders\\recommender_systems\\ratings.csv")
rating = pd.read_csv(r"C:\\Users\\Devi Prajwala B S\\Downloads\\recommenders\\recommender_systems\\google review ratings.csv")

new=[1,2,3,4,5,4,3,2,1]
no_of_attributes = 10
no_of_users = 5456
user_based.pearsons_measure ( rating, new, no_of_attributes, no_of_users )

no_of_items = 10
no_of_users = 5456
new_user = [1,3,3,5,3,4,5,5,2]
item_based.cosine_similarity_measure(rating, no_of_items, no_of_users, new_user )