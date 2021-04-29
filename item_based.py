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

    rating.drop ( 'Users', axis='columns', inplace=True )
    #to drop the first column from the dataframe

    rate = rating.transpose( copy = 'True' )  
    #to obtain the transpose of the rating matrix

    for x in rate.columns:
        rate[x] = rate[x] - rate[x].mean()
    #to subtract the mean of the column from each of the entry in the column

    return rate
    #return the mean adjusted matrix

def similarity( rate, items, users, simili ):
    '''This function is for the calculation of the similarity measure between the items, here we make use of the cosine similarity matrix. We also
    check for the repetition of the items i.e similarity between item A and B is same as that of between item B and A , so we perform the computation
    on the above condition only once'''

    numerator = 0
    denominator1 = 0
    denominator2 = 0
    check_list=[ ]
    #initial assignment of the values to the variables

    for i in range( items ):
        for j in range( items ):
            a = []
            x = max( i, j )
            y = min( i, j )  
            a.append( x )
            a.append( y )
            '''here the two item are appended to the list a to check whether the similarity for the pair is computed earlier or not. Here we follow
            the pattern of max item number first and min item number second for the uniformity in checking''' 
            
            if(i != j and not check_sublist ( a, check_list ) ):
                #above condition loop if for the checking of item pairs

                for k in range( users ):
                    numerator += rate[k][i] * rate[k][j]
                    denominator1 += pow( rate[k][i], 2 )
                    denominator2 += pow( rate[k][j], 2 )
                    
                simi = numerator / ( math.sqrt(denominator1) * math.sqrt(denominator2) )
                '''the above computational operations are based on the formula of cosine similarity. The ratings of different users on two items are
                multiplied in the numerator and in the denominator the ratings are squared and summation is calculated for each. After getting the
                summation values they are divided to get the similarity measure'''

                x = max( i, j )
                y = min( i, j )
                check_list.append( [x, y] )
                #the two items for which the similarity measure is calculated is appended to the list named check_list

                simili.append( [simi, i, j] )
                #the similarity measure , item1 and item2 are appended to the list named simili which is needed for further computation

                numerator = 0
                denominator1 = 0
                denominator2 = 0
                #reinitialisation of variables for the further calculation

    return simili
    #list named simili is returned


def check_sublist( a, check_list ):
    '''this function is for checking whether the list 'a' is the sublist of the 'checklist' or not if yes it returns true else it returns false'''
    for i in check_list:
        if( i[0] == a[0] and i[1] == a[1]):
            #checking whether the elements of the list are same or not if yes returns true else returns false
            return True
    return False
    
def predict( matrix, new, attributes ):
    '''here the function is about making the prediction of the rating of the item which is not seen by the user by making use of the cosine similarity
    which was computed earlier. The concept of weighted average mean is used for making the prediction where weight is the similarity measure'''

    ''' max_similarity = matrix[0][0]
    item1 = item2 = 0
    for i in matrix:
        if(max_similarity < i[0]):
             max_similarity = max( max_similarity, i[0])
             item1 = i[1]
             item2 = i[2]
    print("item", item1+1,"and item" , item2+1, "are in cloooj simiarity!!!")'''
    #to find the items which has highest similarity

    print("Enter the item for which prediction has to be made")
    item = int( input( ) )
    #the item for which the raing has to be predicted is taken as input

    
    if(item > int(attributes) or item == 0):
        #if the entered item is zero or larger than the available set
        print("Enter the value less than ", attributes, "and greater than 0")
        return
    
    item -= 1
    #the item number is decreased by one since in our program item number starts from zero
    
    new.insert( item, 0 )
    #0 is inserted for the item which is unseen by the user

    numerator = 0
    denominator = 0
    #initialisation of the variables with the value zero

    for i in matrix:
        if( i[1] == item or i[2] == item ):
            if( i[1] != item ):
                rating_item = i[1]
            else:
                rating_item = i[2]
            
            numerator += abs(i[0] * new[rating_item])
            denominator += abs(i[0])

    prediction = numerator/ denominator
    '''the above lines of code deal with calculation of weighted mean. rating is multiplied by the weight in numerator and summation is calculated for
    both numerator and denominator'''

    print("The  predicted rating of the user is",prediction, "The user may like the item!!" if prediction>=2.5 else "The user may not like the item")       
    #calculated value is printed on the screen and if the rating is greater than 2.5 the user may like th item or else he may not like the item

def plot_graph(simili):
    '''this function if for plotting the graph of items and thier similarity, here the two items are along the xaxis and similarity measure is taken
    along the y axis'''

    x = []
    y = []
    #a = 'item'
    a = ''
    #initialisation of the list and the string

    for i in simili:
        y.append( i[0] )
        #similarity values are appended to the list y

        a += str( i[1] + 1 )
        a += ','
        a += str( i[2] + 1 )
        x.append(a)
        '''the two items are taken as strings and added and these values are appended to the list x, the item values are incremented by 1 as the item
        number begins from zero in our program'''
        #a ='item'
        a = ''
        #reinitialisation of string

    plt.plot(x,y)
    #for plotting the graph

    plt.figtext(.8, .8, "1,2 here means similarity\n between item 1 and 2")
    #for the text which is on the top right corner

    plt.grid()
    #for the presence of grid in the graph

    plt.xlabel('items')
    #for the label along the x axis

    plt.ylabel('similarity')
    #for the label along the y axis

    plt.title('graph showing similarity of items')
    #for the title of the graph

    plt.scatter(x, y, c='red')
    #to highlight the points in red color

    plt.show()
    #to display the graph

def cosine_similarity_measure(rating, attributes, users, new):
    #this function calls the necessary function in the order which is necessary for the item based recommendation 
    simili=[]
    #list for storing the similarity measure and items

    rate = mean_adjusted_matrix(rating, attributes, users)
    #function is calculated for the computation of mean adjusted matrix

    simili = similarity(rate, attributes, users, simili)
    #function to calculate the similarity measure between the items

    plot_graph(simili)
    #function to plot the graph

    predict(simili, new, attributes)
    #function to predict the value of the rating for the unseen item

#new_user = [1,3,3,5,4,3,3,2,1]
#cosine_similarity_measure(rating, 10, 5456, new_user)
''' this is how the function has to be called for the implementation of the item based similarity, rating the dataframe, 10 is the number of items,
5456 is the number of users and new_user is the list containing the rating for the nine items'''