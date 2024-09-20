import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


conn = sqlite3.connect('veritabani.db')  

query = """
SELECT fiyat, kampanya, satis_miktari
FROM satislar
"""
df = pd.read_sql_query(query, conn)


conn.close()


X = df[['fiyat', 'kampanya']]  # Özellikler
y = df['satis_miktari']        # Hedef


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

# Tahmin yap
y_pred = model.predict(X_test)

# Performansı değerlendir
mse = mean_squared_error(y_test, y_pred)
print(f"Ortalama Kare Hata (MSE): {mse}")

# Sonuçları görselleştir
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue', label='Tahmin Edilen', alpha=0.5)
plt.scatter(y_test, y_test, color='red', label='Gerçek', alpha=0.5)
plt.xlabel('Gerçek Satış Miktarı')
plt.ylabel('Tahmin Edilen Satış Miktarı')
plt.title('Gerçek ve Tahmin Edilen Satış Miktarı')
plt.legend()
plt.show()
