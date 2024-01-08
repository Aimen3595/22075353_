

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from CSV files in the local folder
df1 = pd.read_csv('Age-standardized suicide rates.csv')
df2 = pd.read_csv('Crude suicide rates.csv')
df3 = pd.read_csv('Facilities.csv')
df4 = pd.read_csv('Human Resources.csv')

# Extract years from DataFrame columns (excluding 'Country' and 'Sex')
years = [col for col in df1.columns if col not in ['Country', 'Sex']]

# Sum the suicide values across all years for each country
summed_suicide_df = df1.groupby(['Country'])[years].sum().reset_index()

# Find the top 5 countries with the highest total suicide values in 2016
top10_countries_2016 = summed_suicide_df[['Country', '2016']].nlargest(10, '2016')['Country']

# Filter the DataFrame for the top 10 countries in 2016
top10_suicide_df_2016 = summed_suicide_df[summed_suicide_df['Country'].isin(top10_countries_2016)]

# Reshape the DataFrame for plotting
melted_suicide_df_2016 = pd.melt(top10_suicide_df_2016, id_vars=['Country'], var_name='Year', value_name='Suicide')

# Convert 'Year' column to numeric
melted_suicide_df_2016['Year'] = melted_suicide_df_2016['Year'].astype(int)

# Create a line plot for the top 5 countries in 2016
plt.figure(figsize=(12, 8))
# Bold the axis values and label
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
sns.lineplot(x='Year', y='Suicide', hue='Country', data=melted_suicide_df_2016, marker='o')
plt.legend(title='Country', loc='upper right', frameon=False)
# plt.title('Top 5 Countries by Suicide Values in 2016')
plt.xlabel('Year', fontweight='bold')
plt.ylabel('Suicide Values', fontweight='bold')

plt.savefig("22075353.png", dpi=300)
plt.show()

# Continue with the existing code

# Select the top 5 countries
top10_countries = top10_suicide_df_2016['Country']

# Filter the DataFrame for the top 5 countries
df2_top10 = df2[df2['Country'].isin(top10_countries)]

# Melt the DataFrame to convert it from wide to long format
melted_age_df = pd.melt(df2_top10, id_vars=['Country', 'Sex'], var_name='Age_Group', value_name='Count')

# Create a bar plot for the age groups in each sex category
plt.figure(figsize=(15, 8))
sns.barplot(x='Age_Group', y='Count', hue='Sex', data=melted_age_df)
# Bold the axis values and label
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.legend(title='Country', loc='upper right', frameon=False)  # Corrected here
# plt.title('Age Distribution by Sex in Top 10 Countries')
plt.xlabel('Age Group', fontweight='bold')
plt.ylabel('Count', fontweight='bold')

plt.savefig("22075353_age.png", dpi=300)
plt.show()

# Find the top 5 countries with the highest total suicide values in 2016
top10_countries_2016 = summed_suicide_df[['Country', '2016']].nlargest(10, '2016')['Country']
# Filter the facilities DataFrame for the top 5 countries
df3_top10 = df3[df3['Country'].isin(top10_countries_2016)]

# Melt the DataFrame to convert it from wide to long format
melted_facilities_df = pd.melt(df3_top10, id_vars=['Country', 'Year'], var_name='Facility_Type', value_name='Count')

# Create a bar plot for the facilities in each country
plt.figure(figsize=(15, 8))
sns.barplot(x='Facility_Type', y='Count', hue='Country', data=melted_facilities_df)

# Bold the axis values and label
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

# plt.title('Facilities in Top 10 Suicide Countries')
plt.xlabel('Facility Type', fontweight='bold')
plt.ylabel('Count', fontweight='bold')

plt.savefig("22075353_facilities.png", dpi=300)
plt.show()

# Filter the facilities DataFrame for the top 5 countries
df4_top5 = df4[df4['Country'].isin(top10_countries_2016)]

# Melt the DataFrame to convert it from wide to long format
melted_facilities_df = pd.melt(df4_top5, id_vars=['Country', 'Year'], var_name='Facility_Type', value_name='Count')

# Create a bar plot for the facilities in each country
plt.figure(figsize=(15, 8))
sns.barplot(x='Facility_Type', y='Count', hue='Country', data=melted_facilities_df)

# plt.title('Facilities in Top 5 Suicide Countries')
# Bold the axis values and label
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.xlabel('Human Resource', fontweight='bold')

plt.ylabel('Count', fontweight='bold')


plt.show()
