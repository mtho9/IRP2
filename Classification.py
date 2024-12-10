import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn import svm
from matplotlib.colors import ListedColormap

file_path = "prepared_SVM_dataset.csv"
data = pd.read_csv(file_path)

# prep features (X) and the labels (y)
X = data.drop(columns=['Query', 'Label']).values  # using all features for training
y = data['Label'].values

# split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# train model
svm_clf = svm.SVC(kernel='linear', random_state=42)  # Using a Linear Kernel
svm_clf.fit(X_train, y_train)

# predictions
y_predict = svm_clf.predict(X_test)

# eval model
print("Accuracy: ", accuracy_score(y_test, y_predict))
print("Precision: ", precision_score(y_test, y_predict))
print("Recall: ", recall_score(y_test, y_predict))
print("F1-Score: ", f1_score(y_test, y_predict))

# visuals
def train_and_plot_decision_boundaries(X, y, feature_indices, feature_names):
    X_vis = X[:, feature_indices]

    X_vis[:, 1] = np.log1p(X_vis[:, 1])

    # training the model on the feats specified
    svm_vis = svm.SVC(kernel='linear', random_state=42)
    svm_vis.fit(X_vis, y)

    # gen the grid
    x_min, x_max = X_vis[:, 0].min() - 0.1, X_vis[:, 0].max() + 0.1
    y_min, y_max = X_vis[:, 1].min() - 0.1, X_vis[:, 1].max() + 0.1
    xx, yy = np.meshgrid(
        np.arange(x_min, x_max, 0.01),
        np.arange(y_min, y_max, 0.01)
    )

    # predict points
    Z = svm_vis.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, levels=[-1, 0, 1], alpha=0.8, cmap=ListedColormap(('blue', 'yellow')))
    plt.scatter(X_vis[:, 0], X_vis[:, 1], c=y, edgecolor='k', cmap=ListedColormap(('blue', 'red')))
    plt.title("SVM Decision Boundary with Decision Function")
    plt.xlabel(feature_names[0])
    plt.ylabel(feature_names[1])
    plt.show()


# using these as feats for visual: ACF_12 and Summer_winter_ratio
feature_indices = [13, 14]
feature_names = ['ACF_12', 'Summer_winter_ratio']

# plot
train_and_plot_decision_boundaries(X, y, feature_indices, feature_names)