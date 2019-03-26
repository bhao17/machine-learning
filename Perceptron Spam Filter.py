'''
Created on Feb 13, 2019

@author: brian
'''
#read in file
data = []
with open("spam_train.txt") as file:
    data = file.readlines()


#split into validation and train and write to files

#define validation file
validation = data[0:1000]
v = open("validation.txt", 'w')
for line in validation:
    v.write(line)
v.close()

#define train list
train = data[1000:5000]
#train is a list of emails, each email is a string


#create dictionary
def words (data, x):
    dictionary = {}
    usedwords = []
    words = []
    for e in data:
        words = set(e.split())
        words = list(words)
        #print(words[1:4])
        for w in words:
            if w in dictionary:
                if w == "1" or w == "0":
                    dictionary[w] = 0
                else:                        
                    dictionary[w] += 1
            else:
                dictionary[w] = 1
    for y in dictionary:
        if dictionary[y] >= x:
            usedwords.append(y) 
    return usedwords


#dotproduct (no numpy)
def dotproduct(a, b):
    return sum(c*d for c,d in zip(a, b))
 

#create label list
def labellist (data):
    y = []
    for email in data:
        if email[0][0] == "1":
            y.append(1)
        elif email[0][0] == "0":
            y.append(-1)
    return y


#creating feature vectors
def feature_vector(email, dictionary):
    fvect= []
    #temp = words(train, 26)
    for word in dictionary:
        if word in email:
            fvect.append(1)
        else:
            fvect.append(0)
    return fvect
    
#create list of feature vectors
def fvectlist(data, dictionary):
    x = []
    temp = []
    counter = 0
    for email in data:
        temp = feature_vector(email.split(), dictionary)
        x.append(temp)
        counter += 1
    print("done w/ feature vector list population") #just to show runtime of populating the feature vector list
    return x
#taking way too long
#passing dictionary through feature_vector shortens runtime CONSIDERABLY
#passing a list of words instead of the actual email string also shortens runtime CONSIDERABLY


#training perceptron classifier
def perceptron_train(data):   
    
    mydictionary = words(data, 26)  
    
    w = [0]*len(mydictionary) #weight vector correct length
    
    #label list
    y = labellist(data)
    
    #creating the feature vector list
    x = fvectlist(data, mydictionary)
    
    k = 0 #mistakes
    iter1 = 0 #passes through data
    
    #actual algorithm
    i = 0
    wrong = 0
    while i == 0:
        for j in range(len(x)):
            if y[j]*dotproduct(w, x[j])>0:
                w = w
            else:
                for v in range(len(w)):
                    w[v] = w[v] + y[j]*x[j][v]
                k += 1
                wrong = 1
        iter1 += 1
        if wrong == 0:
            i = 1
            print(str(k) + " " + str(iter1))
            return [w, k, iter1]
        else:
            wrong = 0

def perceptron_error(w, data):
    y = labellist(data)
    thisdictionary = words(train, 26)
    x = fvectlist(data, thisdictionary)
    right = 0
    wrong = 0
    for i in range(len(y)):
        if y[i]*dotproduct(w, x[i]) > 0:
            right += 1
        else:
            wrong += 1
    return wrong/(right+wrong)


#Test Code
testvectoryuh = perceptron_train(train)

yuhtest = []
with open("spam_test.txt") as file:
    yuhtest = file.readlines()

print(perceptron_error(testvectoryuh[0], validation))
print(perceptron_error(testvectoryuh[0], yuhtest))

#END















