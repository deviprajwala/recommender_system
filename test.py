from recommender_systems import user_based
import pandas as pd 
review = pd.read_csv(r"C:\\Users\\Devi Prajwala B S\\Downloads\\recommenders\\recommender_systems\\ratings.csv")


new=[1,2,3,4,5,4,3,2,1]
user_based.pearsons_measure ( review, new, 10, 4 )