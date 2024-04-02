import pandas as pd
df = pd.read_csv('HollywoodMovies.csv')

# Loại bỏ các hàng chứa giá trị thiếu
df.dropna(inplace=True)

# Xử lý outliers cho cột Budget
Q1 = df['Budget'].quantile(0.25)
Q3 = df['Budget'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Loại bỏ outliers ở cột Budget
df = df[(df['Budget'] > lower_bound) & (df['Budget'] < upper_bound)]

# Biến đổi kiểu dữ liệu của cột Genre sang dạng category
df['Genre'] = df['Genre'].astype('category')

# Kiểm tra lại thông tin của dữ liệu sau khi tiền xử lý
print(df.info())

# Kiểm tra lại thống kê mô tả của dữ liệu sau khi tiền xử lý
print(df.describe())

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X = df[['RottenTomatoes', 'AudienceScore', 'Budget']]
y = df['WorldGross']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Xây dựng mô hình hồi quy tuyến tính")
model = LinearRegression()
model.fit(X_train, y_train)

# Đưa ra các kết quả và đánh giá mô hình
print("Hệ số chặn:", model.intercept_)
print("Hệ số hồi quy:", model.coef_)
print("\n")

# Đánh giá mô hình trên tập kiểm tra
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Đánh giá mô hình trên tập kiểm tra:", mse)
print("*****************************************************")
from scipy.stats import ttest_ind

# Phân chia dữ liệu thành các nhóm cần so sánh
group1 = df[df['Genre'] == 'Action']['WorldGross']
group2 = df[df['Genre'] == 'Comedy']['WorldGross']

print("Thực hiện kiểm định t-test")
t_statistic, p_value = ttest_ind(group1, group2)

# In kết quả
print("Giá trị t-statistic:", t_statistic)
print("Giá trị p-value:", p_value)

from scipy.stats import f_oneway

# Phân chia dữ liệu thành các nhóm cần so sánh
group1 = df[df['Genre'] == 'Action']['WorldGross']
group2 = df[df['Genre'] == 'Comedy']['WorldGross']
group3 = df[df['Genre'] == 'Drama']['WorldGross']

print("Thực hiện phân tích ANOVA")
f_statistic, p_value = f_oneway(group1, group2, group3)

# In kết quả
print("Giá trị F-statistic:", f_statistic)
print("Giá trị p-value:", p_value)
