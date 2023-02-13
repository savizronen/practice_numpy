import numpy as np
from matplotlib import pyplot as plt

np.set_printoptions(suppress=True)  # כדי לא לקבל תוצאות ברישום מדעי ( scientific notation)

# 1-	צרו מילון שמכיל כמפתח את מספר הארץ וכערך את שמה
# Q1
countries = {
    1: 'Australia',
    2: 'Canada',
    3: 'China',
    4: 'France',
    5: 'Germany',
    6: 'Greece',
    7: 'India',
    8: 'Italy',
    9: 'Japan',
    10: 'New Zealand',
    11: 'Norway',
    12: 'Russian Federation',
    13: 'Singapore',
    14: 'South Africa',
    15: 'United Kingdom',
    16: 'United States'
}

# 2-	תצרו מערך numpy  בשם gdp
# Q2
gdp = np.genfromtxt('gdp.csv', delimiter=',', skip_header=1)
# print(gdp)

# 3-	כמה שורות ועמודות יש במערך
# Q3
# shape[0] is the number of rows , shape[1] is the number of columns

print(f'The number of rows is {gdp.shape[0]} and the number of columns is {gdp.shape[1]}')

# 4-	הוסף עמודה למערך שמציגה עבור כל ארץ את ממוצע ה- gdp  לכל השנים . תעגלו את הממוצע לשתי ספרות אחרי הנקודה
# Q4
# gdp[:,1:12]
# מכיל את כל השורות והעמודות מהעמודה עם אינדקס 1 (עמודה שניה ) עד העמודה  עם האינדקס 11 (עמודה אחרונה)

# mean(axis=1)
# : מחשב את הממוצע של העמודות 1 עד 11 עבור כל שורה

x = gdp[:, 1:12].mean(axis=1)  # מקבלים מערך עם שורה 1 ו-16 ערכים
x = np.around(x, 2)  # מעוגל לשתי ספרות אחרי הנקודה
x = x.reshape(16, 1)  # מקבלים מערך עם 16 שורות ועמודה 1
print(x)
gdp = np.hstack([gdp, x])   # מחברים בין המערך gdp לעמודה החדשה שיצרנו
print(gdp)

# # 5-	לאיזה ארץ יש gdp  הכי נמוך ב- 2022 . הציגו את שם הארץ ואת ה- gdp
# # Q5
min2022 = gdp[:, 11].min()  # מינימום עבור 2022 (עמודה עם אינדקס 11 )
print(min2022)
x = int(gdp[gdp[:, 11] == min2022, 0])  # מספר הארץ הנמצא בעמודה 0
print(countries[x])  # שם הארץ מהמילון
#
# # 6-	הציגו את כל השורות שיש להם ב- 2020  gdp  גבוה יותר מממוצע ה- gdp  של אותה שנה.
# # Q6
avg = gdp[:, 9].mean()
print(gdp[gdp[:, 9] > avg])
#
# # 7-	הוסיפו עמודה המציגה את גידול ה- gdp  של 5 שנים אחרונות (בין 2017 ל- 2022)
# # Q7
x = gdp[:, 11] - gdp[:, 7]  # חישוב ההפרש בין שתי השנים
x = x.reshape(16, 1)
gdp = np.hstack([gdp, x])
print(gdp)
#
# # 8-	לאיזה ארצות יש גידול שלילי. הצג את שם הארץ  ואת ה- gdp  ב- 2017 וב- 2022
# # בניית מעדך של שורות עם גידול על פי העמודה החדשה
gdp_negative = gdp[gdp[:, 13] < 0]
#
print(gdp_negative)
for x in gdp_negative:
    country_id = x[0]  # מספר הארץ
    country_name = countries[country_id]  # שם הארץ על פי המילון
    print(country_name, x[7], x[11])    # x[7] - 2017 | x[11] - 2022

# # 9-	בנה דיאגרמת מקלות (bar) שמציגה עבור כל ארץ את ה- gdp  של 2022  ואת ה- gdp  של 2021 באותו גרף (שני מקלות עבור כל ארץ כל אחר בצבע אחר). הצג בציר ה- x את שם הארץ.
# # Q9
lx = list(countries.values())
ly1 = list(gdp[:, 11])
ly2 = list(gdp[:, 10])
#
x_axis = np.arange(len(lx))
plt.xticks(rotation=90)  # Rotates X-Axis Ticks by 90-degrees
# # בכדי ליצור הפרדה ביו העמודות את הנתונים של הגרף הראשון נוריד ב 0.2 והגרף השני נעלה ב0.2
# # כך יווצר רווח בתצוגה שלהם
# # אם נוריד את ההפרשים האלו העמודות יהיו אחת על השנייה
plt.bar(x_axis - 0.2, ly1, color='red', width=0.25, label='2022')
plt.bar(x_axis + 0.2, ly2, color='blue', width=0.25, label='2021')
plt.legend()

plt.show()
