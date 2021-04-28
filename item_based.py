# implementation of the item based recommnder system

import pandas as pd 
import math
import pdb
import matplotlib.pyplot as plt
'''we have imported few packages which include pandas math pdb and matplotlib. pandas for reading the data, math for the square root function, pdb 
for debugging by inserting the breakpoints wherever necessary and matplotlib for plotting the similarity graph'''

#pdb.set_trace()
#The above line of code is for setting the break point

#rating = pd.read_csv(r"C:\\Users\\Devi Prajwala B S\\Downloads\\recommenders\\recommender_systems\\google review ratings.csv")
#The above line is for reading the datast from the path specified

def mean_adjusted_matrix( rating, no_of_attributes, no_of_users ):
    '''the function is for obtaining the mean adjusted matrix, mean adjusted matrix is used in the prediction of rating of new user using the item based
    to reduce the error which caused by the users as some tend to give very high ratings most of the time and some tend to give very low ratings most of 
    the time. So to reduce this inconsistency we subtract the mean value from each of tthe user'''

    rating.drop ('Users', axis='columns', inplace=True)
    #to drop the first column from the dataframe

    rate = rating.transpose(copy = 'True')  
    #to obtain the transpose of the rating matrix

    for x in rate.columns:
        rate[x] = rate[x] - rate[x].mean()
    #to subtract the mean of the column from each of the entry in the column

    return rate
    #return the mean adjusted matrix

def similarity(rate, items, users,simili):
    numerator = 0
    denominator1 = 0
    denominator2 = 0
    check_list=[ ]
    for i in range(items):
        for j in range(items):
            a=[]
            x=max(i,j)
            y=min(i,j)
            a.append(x)
            a.append(y)

            #print(rate)
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
                numerator = 0
                denominator1 = 0
                denominator2 = 0
                
    #print(check_list)
    return simili

def check_sublist(a,check_list):
    for i in check_list:
        if(i[0]==a[0] and i[1]==a[1]):
            return True
    return False
    
def predict(matrix, new):
    ''' max_similarity = matrix[0][0]
    item1 = item2 = 0
    for i in matrix:
        if(max_similarity < i[0]):
             max_similarity = max( max_similarity, i[0])
             item1 = i[1]
             item2 = i[2]
    print("item", item1+1,"and item" , item2+1, "are in cloooj simiarity!!!")
    to find the items which has highest similarity'''

    print("Enter the item for which prediction has to be made")
    item = int(input( ))
    item -= 1
    new.insert(item, 0)
    #print(matrix)
    numerator = 0
    denominator = 0
    #print(new)
    for i in matrix:
        if(i[1] == item or i[2] == item):
            if(i[1] != item):
                rating_item = i[1]
            else:
                rating_item = i[2]
            #print(rating_item)
            numerator += abs(i[0] * new[rating_item])
            #print(numerator,"=",i[0],"*",new[rating_item])
            denominator += abs(i[0])
    
    prediction = numerator/ denominator

    print("The  predicted rating of the user is",prediction, "The user may like the item!!" if prediction>=2.5 else "The user may not like the item")       

def plot_graph(simili):
    x = []
    y = []
    #a = 'item'
    a=''
    for i in simili:
        y.append(i[0])
        a += str(i[1]+1)
        a += ','
        a += str(i[2]+1)
        x.append(a)
        #a ='item'
        a=''
    #print(x)
    #print(y)
    plt.plot(x,y)
    plt.figtext(.8, .8, "1,2 here means similarity\n between item 1 and 2")
    plt.grid()
    plt.xlabel('items')
    plt.ylabel('similarity')
    plt.title('graph showing similarity of items')
    plt.scatter(x, y, c='red')
    plt.show()


def cosine_similarity_measure(rating, attributes, users, new):
    simili=[]
    rate = mean_adjusted_matrix(rating, attributes, users)
    simili = similarity(rate, attributes, users, simili)
    #print(simili)
    #print(rate)
    #check_list = [[1,2],[2,3]]
    #a=[2,3]
    #print(check_sublist(a,check_list))

   
    plot_graph(simili)
    predict(simili,new)

new_user = [1,3,3,5,4,3,3,2,1]
cosine_similarity_measure(rating, 10, 5456, new_user)
