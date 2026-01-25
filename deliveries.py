import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Matches = pd.read_csv("C:/Users/KSHITIJ/OneDrive/Desktop/task_1_assign/matches.csv")
print(Matches)

Matches.dropna()
Matches.head()
Matches.info()

Matches.isnull().sum()

plt.figure(figsize=(10,5))
sns.countplot(x="seasons",data=Matches)
plt.title("Number of Matches")
plt.show()

grouping = Matches.groupby('team1').count()
print(grouping)



TOSS = pd.DataFrame({ 'toss_decision','toss_winner',}) 
WINS = pd.DataFrame({'win_by_runs', 'win_by_wickets'}) 

result = pd.concat([TOSS, WINS]) 
print(result) 

result1 = pd.concat([result, grouping]) 
result1.dropna()
result1.head() 



plt.figure(figsize=(10,5))
sns.countplot(x="result1",data=Matches)
plt.title("Number of Matches")
plt.show()

result1.head()
result1.tail() 
result1.shape 
result1.columns 
result1.info() 
result1.describe()



