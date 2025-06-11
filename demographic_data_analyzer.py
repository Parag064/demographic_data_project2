import pandas as pd

def calculate_demographic_data(print_data=True):
   
    df = pd.read_csv("adult.data.csv", header=None)
    df.columns = [
    "age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
    "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
    "hours-per-week", "native-country", "salary"
    ]

    race_count = df['race'].value_counts()

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

 
    total_count = len(df)
    bachelors_count = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = round((bachelors_count / total_count) * 100, 1)


    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(advanced_education)]
    lower_education = df[~df['education'].isin(advanced_education)]


    higher_edu_rich = round((len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education)) * 100, 1)

    lower_edu_rich = round((len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education)) * 100, 1)


    min_work_hours = df['hours-per-week'].min()

    
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((len(num_min_workers[num_min_workers['salary'] == '>50K']) / len(num_min_workers)) * 100, 1)

   
    rich_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    total_country = df['native-country'].value_counts()
    rich_country_percentage = (rich_country / total_country) * 100
    highest_earning_country = rich_country_percentage.idxmax()
    highest_earning_country_percentage = round(rich_country_percentage.max(), 1)

  
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()



  

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
