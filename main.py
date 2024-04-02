import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('HollywoodMovies.csv')


#1
plt.hist(df['AudienceScore'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Điểm đánh giá từ khán giả')
plt.ylabel('Số lượng')
plt.title('Phân phối điểm đánh giá từ khán giả')
plt.show()
#2
plt.hist(df['TheatersOpenWeek'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Số rạp chiếu phim mở cửa trong tuần đầu')
plt.ylabel('Số lượng')
plt.title('Phân phối số rạp chiếu phim mở cửa trong tuần đầu')
plt.show()

#3
plt.xlabel('Doanh thu nội địa của bộ phim')
plt.ylabel('Doanh thu nước ngoài của bộ phim')
plt.title('Phân phối doanh thu nội địa và doanh thu nước ngoài của bộ phim')
plt.xticks(rotation=45)
plt.hist([df['DomesticGross'], df['ForeignGross']], bins=10, color=['skyblue', 'orange'], edgecolor='black', label=['Doanh thu nội địa', 'Doanh thu nước ngoài'])
plt.legend()
plt.show()

#4
plt.plot(df['Year'], df['Profitability'], marker='o', color='skyblue', linestyle='-')
plt.xlabel('Năm')
plt.ylabel('Lợi nhuận')
plt.title('Biến đổi của giá trị lợi nhuận theo thời gian')
plt.grid(True)
plt.show()



#5
# Tính toán số lượng phim theo năm
year_counts = df['Year'].value_counts().sort_index()

# Vẽ biểu đồ đường
plt.figure(figsize=(12, 6))
plt.plot(year_counts.index, year_counts.values, marker='o', linestyle='-')
plt.title('Sự biến đổi của năm phát hành có sức hút với bộ phim theo thời gian')
plt.xlabel('Năm')
plt.ylabel('Số lượng phim')
plt.grid(True)
plt.show()

#6
df['Story'] = df['Story'].astype(str)

plt.figure(figsize=(11, 6))
plt.bar(df['Story'], df['WorldGross'])
plt.title('Mức độ hấp dẫn từ câu chuyện của bộ phim')
plt.xlabel('Câu chuyện')
plt.ylabel('Doanh thu thế giới')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#7. Liệu điểm đánh giá từ Rotten Tomatoes và Audience Score có ảnh hưởng đến doanh thu của bộ phim không?
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='RottenTomatoes', y='WorldGross', label='RottenTomatoes')
sns.scatterplot(data=df, x='AudienceScore', y='WorldGross', label='AudienceScore')
plt.title('Liệu điểm đánh giá từ Rotten Tomatoes và Audience Score có ảnh hưởng đến doanh thu của bộ phim')
plt.xlabel('Điểm đánh giá')
plt.ylabel('Doanh thu thế giới')
plt.legend()
plt.show()

#8. Thể loại phim nào thường mang lại doanh thu cao nhất?
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Genre', y='WorldGross', ci=None)
plt.title('Thể loại phim nào thường mang lại doanh thu cao nhất?')
plt.xlabel('Thể loại phim')
plt.ylabel('Doanh thu thế giới trung bình')
plt.xticks(rotation=45)
plt.show()

#9. Ngân sách sản xuất (Budget) ảnh hưởng đến doanh thu của bộ phim như thế nào?
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Budget', y='WorldGross')
plt.title('Ngân sách sản xuất (Budget) ảnh hưởng đến doanh thu của bộ phim như thế nào?')
plt.xlabel('Ngân sách sản xuất')
plt.ylabel('Doanh thu thế giới')
plt.show()

# 10. Mối quan hệ giữa doanh thu nội địa (Domestic Gross) và doanh thu quốc tế (Foreign Gross)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='DomesticGross', y='ForeignGross')
plt.title('Mối quan hệ giữa Doanh thu nội địa với Doanh thu quốc tế')
plt.xlabel('Doanh thu nội địa')
plt.ylabel('Doanh thu quốc tế')
plt.show()

# 11. Sự khác biệt về doanh thu giữa các năm phát hành
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Year', y='WorldGross')
plt.title('Sự khác biệt về doanh thu giữa các năm phát hành')
plt.xlabel('Năm phát hành')
plt.ylabel('Doanh thu thế giới')
plt.show()

# 12. Liệu doanh thu mở màn có ảnh hưởng đến lợi nhuận của các bộ phim không?
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='OpeningWeekend', y='Profitability')
plt.title('Liệu doanh thu mở màn có ảnh hưởng đến lợi nhuận của các bộ phim ')
plt.xlabel('Doanh thu mở màn')
plt.ylabel('Lợi nhuận')
plt.show()

#13
plt.figure(figsize=(10, 6))
plt.scatter(df['OpeningWeekend'], df['BOAvgOpenWeekend'], alpha=0.5, color='skyblue')

# Thiết lập tiêu đề và nhãn trục
plt.title('Phân phối Doanh thu mở màn của bộ phim với Doanh thu trung bình mở màn của một rạp')
plt.xlabel('Doanh thu mở màn của bộ phim')
plt.ylabel('Doanh thu trung bình mở màn của một rạp')

# Hiển thị biểu đồ
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#14
genre_counts = df['Genre'].value_counts(normalize=True) * 100

# Vẽ biểu đồ hình tròn
plt.figure(figsize=(8, 8))
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%')
plt.title('Tỉ lệ phần trăm của mỗi thể loại phim')
plt.show()

#15
# Tạo danh sách các thể loại xuất hiện trong cột Genre
available_genres = df['Genre'].unique()

# Tạo dict màu sắc ban đầu
genre_colors = {'Drama': 'blue', 'Horror': 'red', 'Mystery': 'green', 'Musical': 'purple', 'Comedy': 'yellow',
                'Biography': 'orange', 'Documentary': 'pink', 'Action': 'brown', 'Adventure': 'cyan',
                'Fantasy': 'magenta', 'Thriller': 'lime', 'Crime': 'gray', 'Animation': 'olive', 'Romance': 'teal'}

# Tạo dict mới chỉ chứa các thể loại có trong danh sách available_genres
filtered_genre_colors = {genre: color for genre, color in genre_colors.items() if genre in available_genres}

# Thiết lập kích thước của biểu đồ
plt.figure(figsize=(10, 6))

# Vẽ histogram với phân loại
sns.histplot(data=df, x='AudienceScore', bins=20, kde=True, hue='Genre', palette=filtered_genre_colors)

# Thiết lập tiêu đề và nhãn trục
plt.title('Phân phối định lượng Điểm đánh giá từ khán giả theo Thể loại')
plt.xlabel('Điểm đánh giá từ khán giả')
plt.ylabel('Số lượng')

# Hiển thị chú thích với tên thể loại và màu sắc tương ứng
handles = [plt.Rectangle((0,0),1,1, color=filtered_genre_colors[label]) for label in filtered_genre_colors]
plt.legend(handles, filtered_genre_colors.keys(), title='Thể loại')

# Hiển thị biểu đồ
plt.tight_layout()
plt.show()

#16
# Giá trị dự đoán và giá trị thực tế của lợi nhuận mà bộ phim thu về (ví dụ)
predicted_values = [100000, 200000, 150000, 180000, 220000]
actual_values = [95000, 210000, 140000, 170000, 230000]
film_titles = ['Film 1', 'Film 2', 'Film 3', 'Film 4', 'Film 5']

# Vẽ biểu đồ điểm
plt.figure(figsize=(10, 6))
plt.scatter(film_titles, predicted_values, color='red', label='Giá trị dự đoán')
plt.scatter(film_titles, actual_values, color='blue', label='Giá trị thực tế')

# Đặt tên cho trục và tiêu đề
plt.xlabel('Tên bộ phim')
plt.ylabel('Lợi nhuận')
plt.title('So sánh giá trị dự đoán và giá trị thực tế của lợi nhuận bộ phim')
plt.xticks(rotation=45)
plt.legend()

# Hiển thị biểu đồ
plt.tight_layout()
plt.show()