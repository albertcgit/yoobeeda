import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score

def load_data():
    # 1. Load
    df = pd.read_csv("Iris.csv")
    print("Shape:", df.shape)
    print(df.head())
    return df

def clean_data(df):
    # 2. Clean
    df.drop(columns=["Id"], inplace=True)
    df.drop_duplicates(inplace=True)
    print("\nMissing values:\n", df.isnull().sum())
    return df

def visualise(df):
    # 3. Visualise - Scatter Plots (Petal and Sepal)
    colours = {"Iris-setosa": "blue", "Iris-versicolor": "green", "Iris-virginica": "red"}

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    for species, colour in colours.items():
        subset = df[df["Species"] == species]
        axes[0].scatter(subset["PetalLengthCm"], subset["PetalWidthCm"], label=species, color=colour)
        axes[1].scatter(subset["SepalLengthCm"], subset["SepalWidthCm"], label=species, color=colour)

    axes[0].set_xlabel("Petal Length (cm)")
    axes[0].set_ylabel("Petal Width (cm)")
    axes[0].set_title("Iris Petals")
    axes[0].legend()

    axes[1].set_xlabel("Sepal Length (cm)")
    axes[1].set_ylabel("Sepal Width (cm)")
    axes[1].set_title("Iris Sepals")
    axes[1].legend()

    plt.tight_layout()
    plt.savefig("scatter_plot.png")
    plt.show()

def train(df):
    # 4. Prepare data
    X = df.drop(columns=["Species"])
    y = df["Species"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test  = scaler.transform(X_test)

    # 5. Train SVM - Linear Kernel
    model = SVC(kernel="linear")
    model.fit(X_train, y_train)

    return model, X_test, y_test

def evaluate(model, X_test, y_test):
    # 6. Evaluate
    y_pred = model.predict(X_test)

    print("\nAccuracy :", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred, average="weighted"))
    print("Recall   :", recall_score(y_test, y_pred, average="weighted"))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

def main():
    df = load_data()
    df = clean_data(df)
    visualise(df)
    model, X_test, y_test = train(df)
    evaluate(model, X_test, y_test)

if __name__ == "__main__":
    main()