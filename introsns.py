import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

height = [1,5,7,8,9,5,4,34]

weight = [65,56,4,6,7,4,8,55]

df = pd.read_csv("C:/Users/kanak/OneDrive/Desktop/data/googleplaystore.csv")
# print(df.head())
# scatterplot
# sns.scatterplot(x=height,y=weight)

# count plot
# sns.countplot(x=height)

# for data frame
# sns.countplot(x="Category", data=df)

palette_colors = {"Rural": "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x="Category", data=df, col="Rating")
plt.show()


#data seeing
df.head() # to see top 5
df.head(10) # to see top 10
df.tail() # to see last 5
df.tail(10) # to see last 10
df[10470:10475] # to see from given index





# data cleaning 

# note : df.col and df["col"] both are same

df.isnull() # it will show all df in true or false in table format

df.isnull().sum() # it will show df in col format with sum of null values of each coloum

df.shape # it will show df's totla no of col and row

df.drop("Rating", axis="columns", inplace=True) # it will remove a column from df compltly

df.drop([10472],inplace=True) # droping a row with it's index

df.dropna(subset=["col1","col2"], inplace=True) # dropna will drop only the row where given col are null

df.col.dtype # to check the data type

df["col1"] = df.col1.astype('float') # it will chnage th data type to float
df['Price'] = df['Price'].apply(lambda x: float(x))# it will chnage th data type to float

# replace $ with '' from a string
df['Price'] = df['Price'].apply(lambda x: str(x).replace('$', '') if '$' in str(x) else str(x))

# replacing '/' with '-' in a string
df.date.str.replace('/','-')

# combinting two col (sep=' ' means it will give space bw two col)
combined = df.date.str.cat(df.time, sep=' ')

# it will convert datetime format and store in new col (date_and_time)
df["date_and_time"]= pd.to_datetime(combined)

# setting a col as index 
df.set_index('date_and_time', inplace=True)

# to see index 
df.index

# to count number of value repeted in a col
df.col.value_counts()

# it will show total number rows which ill be equal to df.shape
df.col.value_counts().sum()

# it will divide count of repeated value / total no of row
df.col.value_counts(normalize=True)

# new df with filted data
newdf = df[df.col == "human"]
newdf.head()
