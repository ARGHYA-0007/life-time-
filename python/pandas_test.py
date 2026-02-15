import pandas as pd
import matplotlib.pyplot as plt
import os
data = {'Subject Name': ['English', 'Bengali', 'Physics','Chemistry','Mathematics','Computer Science'], 'Marks': [92,80,90,82,97,86]}
df = pd.DataFrame(data)

print(df)
plt.pie(df['Marks'], labels=df['Subject Name'], autopct='%1.1f%%', startangle=90)
plt.title('Marks Distribution')
plt.axis('equal')
plt.show()
df.to_excel("arghya.xlsx",index=False)
os.rename("arghya.xlsx","12th_percentage.xlsx")
print("Excel file created successfully!")