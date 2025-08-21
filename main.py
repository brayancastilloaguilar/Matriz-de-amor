import pandas as pd
import matplotlib.pyplot as plt
import re

df = pd.read_csv("chat_whatsapp.csv")
df_love = df[df["Mensaje"].str.contains("te amo", case=False, na=False)].copy()
df_love.loc[:, "Usuario"] = df_love["Usuario"].str.replace(r'[^\x00-\x7F]+', '', regex=True)

conteo = df_love["Usuario"].value_counts()
print(conteo)

conteo.plot(kind="bar", color="red")
plt.title("Quién dice más 'te amo' ❤️")
plt.ylabel("Veces")
plt.show()

#Brayan Castillo Aguilar
#Preguntas? contactame: brayancastillo062008@gmail.com
#---> B.C.A