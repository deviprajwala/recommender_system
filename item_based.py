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

def similarity(rate, items, users,simili):
    numerator = 0
    denominator1 = denominator2 = 0
    check_list=[ ]
    for i in range(items):
        for j in range(users):
            a=[]
            x=max(i,j)
            y=min(i,j)
            a.append(x)
            a.append(y)


            if(i != j and not check_sublist(a,check_list)):
                for k in range(users):
                    #print(i,j,k)
                    numerator += rate[k][i] * rate[k][j]
                    #print(numerator, "=" ,rate[k][i], "*" ,rate[k][j] )
                    denominator1 += pow(rate[k][i],2)
                    denominator2 += pow(rate[k][j],2)                                              
                simi = numerator / ( math.sqrt(denominator1) * math.sqrt(denominator2))
                #print(simi,numerator,denominator1,denominator2)
                x=max(i,j)
                y=min(i,j)
                check_list.append([x,y])
                #print(check_list)
                #print(listi)
                simili.append([simi,i,j])
                #print(simili)
                numerator = denominator1 = denominator2 = 0
                
    #print(check_list)
    return simili

def check_sublist(a,check_list):
    for i in check_list:
        if(i[0]==a[0] and i[1]==a[1]):
            return True
    return False
    
def predict(matrix):
    max_similarity = matrix[0][0]
    item1 = item2 = 0
    for i in matrix:
        if(max_similarity < i[0]):
             max_similarity = max( max_similarity, i[0])
             item1 = i[1]
             item2 = i[2]
    print("item", item1+1,"and item" , item2+1, "are in cloooj simiarity!!!")
    
def cosine_similarity_measure(rating, attributes, users):
    simili=[]
    rate = mean_adjusted_matrix(rating, attributes, users)
    simili = similarity(rate, attributes, users, simili)
    #print(simili)
    #print(rate)
    #check_list = [[1,2],[2,3]]
    #a=[2,3]
    #print(check_sublist(a,check_list))

    predict(simili)
cosine_similarity_measure(rating, 5, 4)