#user based recommnder system
import pandas as pd 
import math
rating = pd.read_csv(r"C:\\Users\\Devi Prajwala B S\\Downloads\\recommenders\\recommender_systems\\item_rating.csv")
#rating.iat[1,4] = rating.iat[1,4].astype(float)
#no_of_attributes = input( " Enter the number of attributes " )

mean_of_each_users = rating.mean(axis = 1)
#print(rating)

def mean_adjusted_matrix( rating, no_of_attributes, no_of_users ):
    '''for i in range(no_of_users):
        for j in range(1,no_of_attributes+1):
            rating.loc[i].iat[j] = float(rating.loc[i].iat[j]) - mean_of_each_users[i]
            #print(i,j)'''

    rating.drop ('Users', axis='columns', inplace=True)
    rate = rating.transpose(copy = 'True')  
    #print(rate)
    for x in rate.columns:
        rate[x] = rate[x] - rate[x].mean()

    return rate

def similarity(rate, items, users):
    listi=[]
    simili=[]
    for i in range(items):
        for j in range(users):
            if(i != j and j > i and i == 0 and j == 4):
                for k in range(items):
                    numerator += rate[i][k] * rate[j][k]
                    denominator1 += pow(rate[i][k],2)
                    denominator2 += pow(rate[j][k],2)

                simi = numerator / ( math.sqrt(denominator1) * math.sqrt(denominator2))
                listi.append(simi)
                listi.append(i)
                listi.append(j)
                print(listi)
                simili.append(listi)
                print(simili)
    return simili

                
    #print(rate[0][0])

def cosine_similarity_measure(rating, attributes, users):
    rate = mean_adjusted_matrix(rating, attributes, users)
    simili = similarity(rate, attributes, users)
    print(simili)
cosine_similarity_measure(rating, 5, 4)