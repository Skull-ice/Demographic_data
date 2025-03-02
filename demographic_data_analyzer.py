import pandas as pd

#charger les données
df = pd.read_csv('adult.data.csv')

#réponse aux questions
race_count = df['race'].value_counts()
average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)
percentage_bachelors = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0] * 100).round(1)higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
higher_education_rich = (higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0] * 100).round(1)
lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
lower_education_rich = (lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0] * 100).round(1)
min_work_hours = df['hours-per-week'].min()
num_min_workers = df[df['hours-per-week'] == min_work_hours]
rich_percentage = (num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0] * 100).round(1)
country_stats = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100).round(1)
highest_earning_country = country_stats.idxmax()
highest_earning_country_percentage = country_stats.max()
top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()
