import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    N = int(input("Enter the number of data points (N): "))
    X = np.zeros(N, dtype=int)
    Y = np.zeros(N, dtype=int)
    
    # Collect N (x, y) points
    print("Enter the data points (x, y) one by one:")
    for i in range(N):
        x = int(input(f"Enter x value for point {i+1} (0 or 1): "))
        y = int(input(f"Enter y value for point {i+1} (0 or 1): "))
        X[i] = x
        Y[i] = y
    
    # Compute precision and recall
    precision = precision_score(X, Y)
    recall = recall_score(X, Y)
    
    # Output
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()
