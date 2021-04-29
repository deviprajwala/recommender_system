# recommender_system

This repositary contains the code for the two main recommender systems which is user based recommendation and item based recommendation system.These two alogorithms can be imported from 
the package named recommender_systems, which is published by me.The function call and reagarding its attributes are present in the test.py file and the dataset used is also present in 
the repositary.This is the first version of the project and more alogorithms can be expected in the upcoming versions.

User based recommendation
Here we calculate the pearson's similarity measure which is needed to determine the closely related users i.e whose likes and dislikes follow the same pattern.The computational 
operations are based on the formula of pearson similarity. The ratings of two different users are subtracted by the mean value and multiplied in the numerator and in the denominator the 
ratings are squared and summation is calculated for each. After getting the summation values they are divided to get the similarity measure

Item based recommendation
Initial aim is obtaining the mean adjusted matrix, mean adjusted matrix is used in the prediction of rating of new user using the item based to reduce the error which caused by the 
users as some tend to give very high ratings most of the time and some tend to give very low ratings most of the time. So to reduce this inconsistency we subtract the mean value from 
each of tthe user.

Next step is the calculation of the similarity measure between the items, here we make use of the cosine similarity matrix. We also check for the repetition of the items i.e 
similarity between item A and B is same as that of between item B and A , so we perform the computation on the above condition only once.The computational operations are based 
on the formula of cosine similarity. The ratings of different users on two items are multiplied in the numerator and in the denominator the ratings are squared and summation is 
calculated for each. After getting the summation values they are divided to get the similarity measure.

Final step is about making the prediction of the rating of the item which is not seen by the user by making use of the cosine similarity which was computed earlier. The concept of 
weighted average mean is used for making the prediction where weight is the similarity measure.

We have also ploted the graph of items and thier similarity, here the two items are along the xaxis and similarity measure is taken along the y axis.

This package can be imported and the functions can be called to implement the above techniques.

The code for user based recommendation: https://github.com/deviprajwala/recommender_system/blob/main/user_based.py
The code for item based recommendation: https://github.com/deviprajwala/recommender_system/blob/main/item_based.py
The data set used : https://archive.ics.uci.edu/ml/datasets/Tarvel+Review+Ratings
The program which show demo of the implementation: https://github.com/deviprajwala/recommender_system/blob/main/test.py
The graph obtained for the cosine similarity: https://github.com/deviprajwala/recommender_system/blob/main/graph.png
The vedio clip which shows the code implementation: https://drive.google.com/file/d/1sCk65fYUHtF9B7aCspU9j3d8SfQp2mQH/view?usp=sharing

References:
https://www.tutorialsteacher.com/python/python-package
https://pandas.pydata.org/docs/getting_started/overview.html
https://realpython.com
Recommender System with Machine Learning and Artificial Intelligence Practical Tools and Applications in Medical, Agricultural and Other Industries by Sachi Nandan Mohanty (editor), 
Jyotir Moy Chatter 
Recommender Systems An Introduction by Dietmar Jannach, Markus Zanker, Alexander Felfernig, Gerhard Friedrich 
