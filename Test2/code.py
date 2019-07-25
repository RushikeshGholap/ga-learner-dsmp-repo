# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#New record
print(data)
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
census = np.concatenate([data , new_record])


# --------------
#Code starts here
import numpy as np
age = np.array([census[:,0]])
max_age = age.max()
min_age = age.min()
age_mean = np.mean(age)
age_std = np.std(age)
print(age,max_age,min_age,age_std,age_mean)


# --------------
#Code starts here
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]

len_0 = np.size(race_0)
len_1 = np.size(race_1)
len_2 = np.size(race_2)
len_3 = np.size(race_3)
len_4 = np.size(race_4)
print(race_0,'\n',race_1,'\n',race_2,'\n',race_3)
print(len_0,len_1,len_2,len_3,len_4)
if len_0 < min(len_1,len_2,len_3,len_4):  
    minority_race = 0
elif len_1 < min(len_2,len_3,len_4):
    minority_race = 1
elif len_2 < min(len_3,len_4):
    minority_race = 2
elif len_3 < len_4:
    minority_race = 3
else :
    minority_race = 4
print(minority_race)

#Code starts here

#Creating new subsets based on 'Age'
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]


#Finding the length of the above created subsets
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

#Printing the length of the above created subsets
print('Race_0: ', len_0)
print('Race_1: ', len_1)
print('Race_2: ', len_2)
print('Race_3: ', len_3)
print('Race_4: ', len_4)

#Storing the different race lengths with appropriate indexes
race_list=[len_0, len_1,len_2, len_3, len_4]

#Storing the race with minimum length into a variable 
minority_race=race_list.index(min(race_list))

#Code ends here



# --------------
    senior_citizens = census[census[:,0]>60]
    working_hours_sum = sum(senior_citizens[:,6])
    senior_citizens_len = len(senior_citizens)
    avg_working_hours = working_hours_sum / senior_citizens_len
    print(avg_working_hours)


# --------------
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])
print(avg_pay_high,'*******************\n',avg_pay_low)


