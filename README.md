#  Similar Innings Finder using K-Nearest Neighbors (KNN)

This project applies **Machine Learning** to analyze **Virat Kohli's ODI batting performances** and find innings that are similar to a given score using the **K-Nearest Neighbors (KNN)** algorithm.

---

##  Project Objective

Given a target score (e.g., `150`), the program identifies the top 10 most similar ODI innings by Virat Kohli using distance-based similarity (Euclidean distance).

It also creates a **visual summary image** using OpenCV, listing those similar innings with match details.

---

## Dataset

- CSV file: `virat_kohli_odi_data.csv`
- Columns include:
  - `Runs`: Number of runs scored
  - `VS`: Opponent team
  - `Place`: Venue
  - `Date`: Match date

---

##  Technologies Used

- `Python`
- `pandas` for data preprocessing
- `scikit-learn` for the KNN algorithm
- `OpenCV` for custom image generation
- `NumPy` for numerical operations

---

## ⚙ How It Works

1. Load the ODI data from CSV.
2. Preprocess the `Runs` column (handle not-outs marked by `*`).
3. Convert scores to numeric format.
4. Fit a `KNeighbors` model to the `Runs` data.
5. Predict the top 10 innings most similar to a given score.
6. Display results both in the terminal and as a saved image (`similar_innings_output.png`).


