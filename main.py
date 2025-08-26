try:
    import pandas as pd
except ImportError:
    print("Pandas library is not installed. Please install it to proceed.")
    exit()
df = pd.read_csv("student_scores.csv")
print(df.info())
#calculate the mean score
mean_score = df['Scores'].mean()
print(f"The mean score is: {mean_score}")

top5_score = df.nlargest(5, 'Scores')
print("Top 5 scores:")
print(top5_score)