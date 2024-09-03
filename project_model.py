import pickle

import pandas as pd
import sklearn.metrics

df = pd.read_csv(r"C:/Users/latif/Downloads/Medical_insurance.csv")
df=df.drop_duplicates()
df['sex'] = df['sex'].replace({'female': 0, 'male': 1})
df['smoker'] = df['smoker'].replace({'no': 0, 'yes': 1})
df['region'] = df['region'].replace({'southeast': 0, 'southwest': 1, 'northwest': 2, 'northeast': 3})

x = df.drop('charges', axis=1)
y = df['charges']


def remove_outliers_iqr(df, bmi):
    Q1 = df['bmi'].quantile(0.25)
    Q3 = df['bmi'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df['bmi'] >= lower_bound) & (df['bmi'] <= upper_bound)]


df_cleaned = remove_outliers_iqr(df, 'bmi')

df_cleaned.to_csv('fileis_data_cleaned.csv', index=False)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(x_train)

x_train_scaled = pd.DataFrame(scaler.transform(x_train), columns=x_train.columns)
x_test_scaled = pd.DataFrame(scaler.transform(x_test), columns=x_test.columns)

from sklearn.ensemble import RandomForestRegressor

rfr_model = RandomForestRegressor()
rfr_model.fit(x_train, y_train)

y_pred = rfr_model.predict(x_test)
print(f"Accuracy on Test Data: {sklearn.metrics.r2_score(y_test, y_pred) * 100:.2f}")

model_path = 'rf_model.pkl'

scaler_path = 'scaler.pkl'

with open(model_path, 'wb') as f:
    pickle.dump(rfr_model, f)

with open(scaler_path, 'wb') as f:
    pickle.dump(scaler, f)

print("Model and scaler saved successfully!")