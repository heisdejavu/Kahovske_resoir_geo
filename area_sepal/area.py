import pandas as pd

df_change = pd.read_csv('area_sepal/k_class_change.csv')
df_2022_classify = pd.read_csv('area_sepal/2022_class.csv')
df_2024_classify = pd.read_csv('area_sepal/2024_class.csv')


def area_per_class_change():

    name = {   0: 'non-def',
            1: 'forest -> forest', 3: 'forest -> water', 4: 'forest -> land',         
            9: 'water -> forest', 11: 'water -> water', 12: 'water -> land',         
            13: 'land -> forest', 15: 'land -> water', 16: 'land -> land'
        }
    df_change['DN'] = df_change['DN'].replace(name)
    area_change = df_change.groupby('DN')['area_ha'].sum().round(2)

    non_def_area_change = area_change.get('non-def', 0)

    total_area_change = area_change.sum() - non_def_area_change
    percent_change = (area_change / total_area_change * 100).round(2)


    df_result_change = pd.DataFrame({
        'Class Change': area_change.index,
        'Area Change (ha)': area_change.values,
        'Percent Change (%)': percent_change.values
    })

    return area_change, percent_change, total_area_change, df_result_change

def area_classify_2024():
    area_2024 = df_2024_classify.groupby('Class')['area'].sum().round(2)

    non_def_area_2024 = area_change.get('non-def', 0)
    total_area_2024 = area_2024.sum() - non_def_area_2024
    percent_2024 = (area_2024 / total_area_2024 * 100).round(2)

    # Формуємо таблицю
    df_result_2024 = pd.DataFrame({
        'Class': area_2024.index,
        'Area 2024 (ha)': area_2024.values,
        'Percent 2024 (%)': percent_2024.values
    })

    return area_2024, percent_2024, total_area_2024, df_result_2024


def area_classify_2022():
    area_2022 = df_2022_classify.groupby('class')['area_ha'].sum().round(2)

    non_def_area_2022 = area_change.get('non-def', 0)
    total_area_2022 = area_2022.sum() - non_def_area_2022
    percent_2022 = (area_2022 / total_area_2022 * 100).round(2)

    df_result_2022 = pd.DataFrame({
        'Class': area_2022.index,
        'Area 2022 (ha)': area_2022.values,
        'Percent 2022 (%)': percent_2022.values
    })

    return area_2022, percent_2022, total_area_2022, df_result_2022

print('//////////////////////////////////////')
print('Class Change 2022/2024')
# print(area_per_class_change())
area_change, percent_change,  total_area_change, df_result_change = area_per_class_change()
# print(area_change)
# print(percent_change)
print(df_result_change)
print('//////////////////////////////////////')

print('//////////////////////////////////////')
print('Area per class 2024')
# print(area_classify_2024())
area_2024, percent_2024,  total_area_2024, df_result_2024 = area_classify_2024()
# print(area_2024)
# print(percent_2024)
print(df_result_2024)
print('//////////////////////////////////////')

print('//////////////////////////////////////')
print('Area per class 2022')
# print(area_classify_2022())
area_2022, percent_2022,  total_area_2022, df_result_2022 = area_classify_2022()
# print(area_2022)
# print(percent_2022)
print(df_result_2022)
print('//////////////////////////////////////')



