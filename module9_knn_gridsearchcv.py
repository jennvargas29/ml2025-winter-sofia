import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Function to read data (x, y) pairs
def read_data(num_pairs):
    data = []
    for _ in range(num_pairs):
        x = float(input("Enter x value (real number): "))
        y = int(input("Enter y value (non-negative integer): "))
        data.append([x, y])
    return np.array(data)

# Main program
def main():
    # Step 1: Read training data
    N = int(input("Enter number of training data points (N): "))
    print("Enter training data (x, y) pairs:")
    train_data = read_data(N)
    X_train, y_train = train_data[:, 0].reshape(-1, 1), train_data[:, 1]

    # Step 2: Read test data
    M = int(input("Enter number of test data points (M): "))
    print("Enter test data (x, y) pairs:")
    test_data = read_data(M)
    X_test, y_test = test_data[:, 0].reshape(-1, 1), test_data[:, 1]

    # Step 3: Try different k values and find best k (max k <= min(N, M))
    best_k, best_accuracy = None, 0
    max_k = min(N, M)  # Limit k to the smaller of N or M
    for k in range(1, max_k + 1):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = k

    # Output the best k and accuracy
    print(f"The best k is: {best_k}")
    print(f"The corresponding test accuracy is: {best_accuracy * 100:.2f}%")

if __name__ == "__main__":
    main()
