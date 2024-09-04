#!/usr/bin/env python
# coding: utf-8

# In[3]:


df = pd.read_csv('C:\\Users\\Lenovo\\Downloads\\HRDataset_v14.csv')


# In[65]:


df.head(5)


# In[38]:


df.tail(3)


# In[10]:


#set_option is used to manage the display and warnings 
pd.set_option('display.max_rows',100)
pd.set_option('display.max_columns', 100)


# In[11]:


#getting the counting of rows and columns 
num_rows, num_columns = df.shape 
print("number of rows in the table", num_rows)
print("number of the columns in table ", num_columns)


# In[67]:


#ANSI code in python for the bold and underline :
b = '\033[1m' #for bolding the text
u = '\033[4m' # for underlining the text
r = '\033[0m' # for reseting the txt 
         
print(f"{b}{u}Columns in DataFrame: ", df.columns.to_list())
print(f"{b}list of the number of unique values in each columns ")
for col in df.columns:
    print(f"{b}{u}{col}{r}: {df[col].nunique()}")
    

        


# In[24]:


print("data type of columns ", df.dtypes)
#INFORAMTION ABOUT THE DATAFRAMES USING DF.INFO()
print(f"{b}{u}Information about the datframes")
df.info()


# In[28]:


df.describe()
#df.duplicated().sum()


# In[29]:


df.duplicated()


# In[30]:


df.duplicated().sum()


# # ANALYSING
# 

# In[86]:


#plt.figure(figsize=(10, 6))
#plt.bar(x="Salary",y ="Position", data = df)
#plt.show()
plt.figure(figsize=(10, 6))
plt.bar(df['Position'], df['Salary'])
plt.xlabel('Position')
plt.ylabel('Salary')
plt.title('Salary by Position')
plt.xticks(rotation = 90)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# In[46]:


import warnings
warnings.filterwarnings("ignore")

sns.distplot(df["Salary"])
plt.show



# In[54]:


# Create a boxplot
plt.figure(figsize=(12, 8))  # Increase size for better visibility

# Create a boxplot for salaries by position
df.boxplot(column='Salary', by='Position', grid=True)

# Set the title and labels
plt.title('Position-Wise Salary Distribution', fontdict={'fontsize': 14, 'fontweight': 'bold', 'color': 'blue'},   family='serif')
plt.suptitle('')  # Remove the default title to avoid overlap
plt.xlabel('Position')
plt.ylabel('Salary')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Adjust layout to fit labels
plt.tight_layout()

# Show the plot
plt.show()


# In[64]:


# Average Salary by POSITION 
plt.figure(figsize=(10, 6))
sns.barplot(x="Position", y="Salary", data=df[df["Department"]!= "Executive Office"], estimator=np.mean)
plt.title("Average Salary by Position")
plt.xlabel("POSITION")
plt.ylabel("Average Salary")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# In[75]:


# Create a scatter plot
plt.figure(figsize=(12, 8))
plt.scatter(df['Department'], df['Salary'], color='skyblue')

# Set the title and labels
plt.title("Salary Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Salary")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()


# In[102]:


plt.figure(figsize=(10,6))
plt.bar(df['Department'], df['Salary'])
plt.title("SALARY DISTRIBUTION BY DEPARTMENT",fontdict={'fontsize':16,'color': 'blue'})
plt.xlabel("DEPARTMENT",fontdict={'fontsize':14,'color': 'blue'})
plt.ylabel("SALARY",fontdict={'fontsize':14,'color': 'blue'})

plt.show()


# In[94]:


#BOXPLOTTING TO ANALYSING 
plt.figure(figsize=(12,8))
sns.boxplot(x='Department',y='Salary', data=df)
plt.show()


# In[99]:


# Average Salary by department
plt.figure(figsize=(6, 4))
sns.barplot(x="Department", y="Salary", data=df[df["Department"]!= "Executive Office"], estimator=np.mean)
plt.title("Average Salary Department wise ")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=60)
plt.show()


# In[7]:


#SALARY DISTRIBUTION BY SEX 
plt.figure(figsize=(10,6))
sns.boxplot(x="Sex", y="Salary", data=df)
plt.title("SALARY DISTRIBUTION BY SEX", fontdict={'fontsize': 14, 'color':'blue'})
plt.xlabel("SEX", fontdict={'fontsize': 9})
plt.ylabel("SALARY", fontdict={'fontsize': 9})


plt.show()


# In[20]:


#AVERAGE SALARY DISTRIBUTION BY SEX
plt.figure(figsize=(8,6))
sns.barplot(x="Sex", y="Salary", data=df[df["Department"]!= "Executive Office"], estimator=np.mean)
#plt.bar(x="Sex", y="Salary",height=10, data=df[df["Department"]!= "Executive Office"], estimator=np.mean)
plt.title("AVERAGE SALARY DISTRIBUTION BY SEX ", fontdict={'fontsize':14, 'color':'blue'})
plt.show()


# # ANALYSING THE COUNTS OF THE EMPLOYEES WORKING

# In[53]:


#COUNTING THE ACTIVE EMPLOYEE DEPARTMENT WISE 
plt.figure(figsize=(10,6))
active = df[df['EmploymentStatus'] == 'Active']
#counting values
Department_wise = active['Department'].value_counts()
a = Department_wise.plot(kind='bar')

# Add counts to each bar
for p in a.patches:
    height = p.get_height()
    a.text(p.get_x() + p.get_width() / 2, height + 0.5,  # Position the text slightly above the bar
            f'{height}',  # Display the count
            ha='center', va='bottom', color='black')

#plotting the values and analysing 
Department_wise.plot(kind='bar')
plt.title("COUNTING THE ACTIVE EMPLOYEES DEPARTMENT-WISE",fontsize=14, color='blue')
plt.xlabel("DEPARTMENT", fontsize=10, color='blue')
plt.ylabel("ACTIVE EMPLOYEE", fontsize=10, color='blue')

plt.show()


# In[58]:


#COUNTING THE TERMINATED EMPLOYEE BY THE MANAGER
plt.figure(figsize=(10,6))
terminated = df[df['EmploymentStatus'] == 'Terminated for Cause']
counting = terminated['ManagerName'].value_counts()
a = counting.plot(kind='bar')
# Add counts to each bar
for p in a.patches:
    height = p.get_height()
    a.text(p.get_x() + p.get_width() / 2, height + 0.5,  # Position the text slightly above the bar
            f'{height}',  # Display the count
            ha='center', va='bottom', color='black')
plt.title("counting of terminted employee for cause by the manager")
plt.xlabel("TERMINATED EMPLOYEE")
plt.ylabel("MANAGER")


plt.show()


# In[62]:


#COUNTING THE TERMINATED EMPLOYEE BY THE MANAGER
plt.figure(figsize=(10,6))
terminated = df[df['EmploymentStatus'] == 'Voluntarily Terminated']
counting = terminated['ManagerName'].value_counts()
a = counting.plot(kind='bar')
# Add counts to each bar
for p in a.patches:
    height = p.get_height()
    a.text(p.get_x() + p.get_width() / 2, height + 0.5,  # Position the text slightly above the bar
            f'{height}',  # Display the count
            ha='center', va='bottom', color='black')
plt.title("counting of Voluntarily Terminated employee for cause by the manager")
plt.xlabel("MANAGER")
plt.ylabel("Voluntarily Terminated")


plt.show()


# In[67]:


plt.figure(figsize=(10,6))
a = sns.countplot(x="ManagerName", hue = "Termd", data=df)
# Add counts to each bar
for p in a.patches:
    height = p.get_height()
    a.text(p.get_x() + p.get_width() / 2, height + 0.5,  # Position the text slightly above the bar
            f'{height}',  # Display the count
            ha='center', va='bottom', color='black')
plt.title("counting of employee")
plt.xlabel("MANAGER")
plt.ylabel("Count of Terminated Employees")
plt.legend(title="STATUS", labels=["Active","Terminated"])
plt.xticks(rotation=90)
plt.show()


# In[76]:


#Visualize the distribution of employee satisfaction 
plt.figure(figsize =(10,6))
plt.hist(df['EmpSatisfaction'],bins=5, edgecolor = 'black')
plt.xlabel("satisfaction level")
plt.ylabel("Frequency")
plt.title("satisfaction level", fontsize = 14)
plt.show()


# In[81]:


#Visualize the distribution of employee performance score
plt.figure(figsize =(10,6))
sns.countplot(x='PerformanceScore', data = df)
plt.xlabel("Performance Status")
plt.ylabel("Frequency")
plt.title("PERFORMANCE STATUS OF EMPLOYEE", fontdict = {'color': 'blue', 'fontsize' : 14})
plt.xticks(rotation = 30)
plt.show()


# In[82]:


#creating the cross table 
cross_table = pd.crosstab(df["EmpSatisfaction"],df["PerformanceScore"])
print(cross_table)


# In[84]:


sns.heatmap(cross_table)
plt.title("CROSS_TABLE OF PERFORMANCE STATUS AND SATISFACTION LEVEL")
plt.show()


# In[102]:


#visualize the distribution of the performance score by manager 
plt.figure(figsize=(10,6))
sns.countplot(x='ManagerName', hue='PerformanceScore', data=df, palette='viridis',edgecolor='black' )
plt.title("PERFORMANCE SCORE BY MANGER ", fontdict = {'fontsize': 14, 'color':'blue'})
plt.xticks(rotation = 90)
plt.show()
#contigency table of above 
c_table = pd.crosstab(df["ManagerName"], df["PerformanceScore"])
#printing the table 
print(c_table)
sns.heatmap(c_table, cmap='Blues', fmt='d',annot=True)
plt.title("contigency table of performance score by manager")

plt.show()


# In[6]:


# Calculate mean and standard deviation
stats1 = df.groupby('ManagerName')['EmpSatisfaction'].agg(['mean']).reset_index()
stats2 = df.groupby('ManagerName')['EmpSatisfaction'].agg(['std']).reset_index()

# Merge the stats DataFrames for easier plotting
stats = pd.merge(stats1, stats2, on='ManagerName')
stats.columns = ['ManagerName', 'MeanEmpSatisfaction', 'StdDevEmpSatisfaction']

# Create a figure with 3 subplots
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Plot 1: Mean EmpSatisfaction by ManagerName
sns.barplot(x='ManagerName', y='MeanEmpSatisfaction', data=stats, ax=axs[0])
axs[0].set_xlabel('Manager Name')
axs[0].set_ylabel('Mean Employee Satisfaction')
axs[0].set_title('Mean Employee Satisfaction by Manager')
axs[0].tick_params(axis='x', rotation=90)

# Plot 2: Standard Deviation of EmpSatisfaction by ManagerName
sns.barplot(x='ManagerName', y='StdDevEmpSatisfaction', data=stats, ax=axs[1])
axs[1].set_xlabel('Manager Name')
axs[1].set_ylabel('Standard Deviation of Employee Satisfaction')
axs[1].set_title('Standard Deviation of Employee Satisfaction by Manager')
axs[1].tick_params(axis='x', rotation=90)

# Plot 3: Distribution of EmpSatisfaction by ManagerName
sns.boxplot(x='ManagerName', y='EmpSatisfaction', data=df, ax=axs[2])
axs[2].set_xlabel('Manager Name')
axs[2].set_ylabel('Employee Satisfaction')
axs[2].set_title('Distribution of Employee Satisfaction by Manager')
axs[2].tick_params(axis='x', rotation=90)

# Adjust the layout to avoid overlapping labels
plt.tight_layout()

# Show the plot
plt.show()


# In[13]:


#COUNTING THE RECRUITMENT SOURCE 
recruite = df['RecruitmentSource'].value_counts()
print("counting the recruitment sources ")
print(recruite)
recruite.plot(kind='bar')
plt.title("COUNTING THE RECRUITMENT SOURCE ")
plt.ylabel("NUMBERS")
plt.xlabel("RECRUITMENT SOURCES")
plt.show()


# In[8]:


import seaborn as sns
import matplotlib.pyplot as plt

# Define the columns for the pairplot
cont_col = ['SpecialProjectsCount', 'Salary', 'PositionID', 'EmpSatisfaction']

# Create the pairplot
sns.pairplot(df[cont_col + ['Sex']], kind="reg", diag_kind="kde", hue='Sex')

# Show the plot
plt.show()


# In[5]:


print(df.columns)


# In[4]:


# Convert 'DOB' to datetime format
df['DOB'] = pd.to_datetime(df['DOB'])

# Calculating the age of the employee 
current_date = pd.Timestamp.now()
df['Age'] = (current_date - df['DOB']).astype('<m8[Y]')

print(df)


# #  pie charts 

# In[15]:


#couting the gender
gender_counts = df['Sex'].value_counts()
#ploting the pie charts 
plt.figure(figsize =(7,5))
plt.title("PIE CHART FOR GENDER")
plt.pie(gender_counts, labels = gender_counts.index,autopct='%1.1f%%', colors=['#ff9999','#66b3ff'], startangle=90)
plt.legend(gender_counts.index, title="GENDER")
plt.show()


# In[29]:


#couting the department
Department_counts = df['Department'].value_counts()
#ploting the pie charts 
plt.figure(figsize =(7,5))
plt.title("Department")
plt.pie(Department_counts, labels = Department_counts.index,autopct='%1.1f%%', startangle=180)
#plt.legend(Department_counts.index, title="Department", loc='best')
plt.show()


# In[27]:


#couting the department RecruitmentSource
recruite_counts = df['RecruitmentSource'].value_counts()
#ploting the pie charts 
plt.figure(figsize =(7,5))
plt.title("RecruitmentSource")
plt.pie(recruite_counts, labels = recruite_counts.index,autopct='%1.1f%%', startangle=180)
#plt.legend(recruite_counts.index, title="RecruitmentSource")
plt.show()


# In[28]:


#couting the departmentEmploymentStatus
EmploymentStatus_counts = df['EmploymentStatus'].value_counts()
#ploting the pie charts 
plt.figure(figsize =(7,5))
plt.title("EmploymentStatus")
plt.pie(EmploymentStatus_counts, labels = EmploymentStatus_counts.index,autopct='%1.1f%%', startangle=180)
#plt.legend(recruite_counts.index, title="RecruitmentSource")
plt.show()


# In[ ]:




