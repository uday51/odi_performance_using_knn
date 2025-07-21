import pandas as pd
from sklearn.neighbors import NearestNeighbors
import cv2
import numpy as np





csv_path = r""


#readfile
df=pd.read_csv(csv_path)





#Converting to int
df['Runs']=df['Runs'].astype(str).str.replace('*','',regex=False)
df=df[df['Runs'].str.isnumeric()]
df['Runs']=df['Runs'].astype(int)





X=df['Runs'].values.reshape(-1, 1)


knn=NearestNeighbors(n_neighbors=10)
knn.fit(X)


current_score=150
distance,indices=knn.kneighbors([[current_score]])
print(distance)
print(indices)
similar_innings=df.iloc[indices[0]]

print(f"\n Similar Innings to {current_score}:\n")
for idx, row in similar_innings.iterrows():
    print(f"{row['Runs']} vs {row['VS'].replace('v ', '')} at {row['Place']} on {row['Date']} ")



width, height = 1000, 600
img = np.zeros((height, width, 3), dtype=np.uint8)

# Title
title = f"Similar Innings to Score: {current_score}"
cv2.putText(img, title, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

# Add similar innings text
y = 100
for i, row in enumerate(similar_innings.itertuples(), start=1):
    line = f"{i}. {row.Runs} vs {row.VS.replace('v ', '')} at {row.Place} on {row.Date}"
    cv2.putText(img, line, (30, y), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 1)
    y += 40

# Save image
cv2.imwrite("similar_innings_output.png", img)
print("Image saved as similar_innings_output.png")
    












