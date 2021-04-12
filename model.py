#imports to be able to pull data and prepare it for us
import wrangle

#imports for needed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import graphviz
import pydataset

# ignoring warnings
import warnings
warnings.filterwarnings("ignore")

#imports for modeling
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
    #import to be able to do decision tress
from sklearn.neighbors import KNeighborsClassifier
    #import to be able to do KNN
from sklearn.linear_model import LogisticRegression
    #import to be able to do logistic regression
from sklearn.ensemble import RandomForestClassifier
    #import to be able to do random forest
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
df = wrangle.acquire_game_sales()
df = wrangle.clean_game_sales(df)
train, validate, test = wrangle.split_game_sales(df)
X_train, X_validate, X_test, y_train, y_validate, y_test = wrangle.split_train_validate_test(train, validate, test)
df2 = wrangle.focused_game_sales(df)
train2, validate2, test2 = wrangle.split_focused_game_sales(df2)
X_train2, X_validate2, X_test2, y_train2, y_validate2, y_test2 = wrangle.split_train_validate_test(train2, validate2, test2)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def find_baseline(train):
    '''finds baseline accuracy for upcoming models'''
    baseline_accuracy = (train.level_of_success == 'Fairly Successful').mean()
    print(f'My baseline accuracy is: \n', round(baseline_accuracy, 3))
    
def get_logit1(X_train2, X_validate2, X_test2, y_train2, y_validate2, y_test2):
    '''Creates the logistic regression model
    returns its train, validate, and test accuracy'''
    logit1 = LogisticRegression(random_state=123)
    # Fit a model using only these specified features
    # logit.fit(X_train[["age", "pclass", "fare"]], y_train)
    logit1.fit(X_train2, y_train2)
    # Since we .fit on a subset, we .predict on that same subset of features
    y_pred = logit1.predict(X_train2)
    print('Accuracy of Logit 1 Model on Train: \n', round(logit1.score(X_train2, y_train2),4))
    print('Accuracy of Logit 1 Model on Validate: \n', round(logit1.score(X_validate2, y_validate2),4))
    print('Accuracy of Logit 1 Model on Test: \n', round(logit1.score(X_test2, y_test2),4))
    
def decision_tree(X_train2, X_validate2, X_test2, y_train2, y_validate2, y_test2):
    '''creates my decision tree model
    and returns its accuracy for train, test, and validate'''
    # set max depth
    clf1 = DecisionTreeClassifier(max_depth=3)
    # drop target
    X_train2 = train2.drop(columns='level_of_success')
    y_train2 = train2.level_of_success
    # fit it
    clf1.fit(X_train2, y_train2)
    # create predictions
    y_pred = clf1.predict(X_train2)
    # make confusion matrix
    conf = confusion_matrix(y_train2, y_pred)
    # make class report
    class_report = classification_report(y_train, y_pred, output_dict=True)
    print('Accuracy of Decision Tree Model on Train: \n', round(clf1.score(X_train2, y_train2),4))
    print('Accuracy of Decision Tree Model on Validate: \n', round(clf1.score(X_validate2, y_validate2),4))
    print('Accuracy of Decision Tree Model on Test: \n', round(clf1.score(X_train2, y_train2),4))
    
def KNN_model(X_train2, X_validate2, X_test2, y_train2, y_validate2, y_test2):
    '''creates the knn model
    returns the accuracy for train, validate, and test'''
    knn = KNeighborsClassifier()
    # Now let's train the model!
    knn.fit(X_train2, y_train2)
    # Let's check the accuracy
    accuracy = knn.score(X_train2, y_train2)
    print(f"accuracy is {accuracy:.3}")
    # Evaluate the model
    y_pred = knn.predict(X_train2)
    # Obtain the predictions from the model
    y_pred = knn.predict(X_validate2)
    print('Accuracy of KNN Model on Train: \n',round(knn.score(X_train2, y_train2),4))
    print('Accuracy of KNN Model on Validate: \n',round(knn.score(X_validate2, y_validate2),4))
    print('Accuracy of KNN Model on Test: \n',round(knn.score(X_test2, y_test2),4))
    
def random_forest_model(X_train2, X_validate2, X_test2, y_train2, y_validate2, y_test2):
    '''Makes random forest model
    returns Accuracy for train, validate, and test'''
    rf = RandomForestClassifier(bootstrap=True, 
                            class_weight=None, 
                            criterion='gini',
                            min_samples_leaf=3,
                            n_estimators=100,
                            max_depth=3, 
                            random_state=123)
    # fit the model
    rf.fit(X_train2, y_train2)
    # make predictions
    y_pred = rf.predict(X_train2)
    # estimate probability
    y_pred_proba = rf.predict_proba(X_train2)
    print('Accuracy of Random Forest Classifier on Train: \n', round(rf.score(X_train2, y_train2),4))
    print('Accuracy of Random Forest Classifier on Validate: \n', round(rf.score(X_validate2, y_validate2),4))
    print('Accuracy of Random Forest Classifier on Test: \n', round(rf.score(X_test2, y_test2),4))
    
def all_models(X_train2, X_validate2, X_test2, y_train2, y_validate2, y_test2):
    '''recreates all models and returns each train accuracy to help decision making'''
    # baseline
    baseline_accuracy = (train.level_of_success == 'Fairly Successful').mean()
    # logit 1
    logit1 = LogisticRegression(random_state=123)
    # Fit a model using only these specified features
    # logit.fit(X_train[["age", "pclass", "fare"]], y_train)
    logit1.fit(X_train2, y_train2)
    # Since we .fit on a subset, we .predict on that same subset of features
    y_pred = logit1.predict(X_train2)
    # decision tree
    # set max depth
    clf1 = DecisionTreeClassifier(max_depth=3)
    # drop target
    X_train2 = train2.drop(columns='level_of_success')
    y_train2 = train2.level_of_success
    # fit it
    clf1.fit(X_train2, y_train2)
    # create predictions
    y_pred = clf1.predict(X_train2)
    # make confusion matrix
    conf = confusion_matrix(y_train2, y_pred)
    # make class report
    class_report = classification_report(y_train, y_pred, output_dict=True)
    # knn 
    knn = KNeighborsClassifier()
    # Now let's train the model!
    knn.fit(X_train2, y_train2)
    # Let's check the accuracy
    accuracy = knn.score(X_train2, y_train2)
    print(f"accuracy is {accuracy:.3}")
    # Evaluate the model
    y_pred = knn.predict(X_train2)
    # Obtain the predictions from the model
    y_pred = knn.predict(X_validate2)    
    # random forest
    rf = RandomForestClassifier(bootstrap=True, 
                            class_weight=None, 
                            criterion='gini',
                            min_samples_leaf=3,
                            n_estimators=100,
                            max_depth=3, 
                            random_state=123)
    # fit the model
    rf.fit(X_train2, y_train2)
    # make predictions
    y_pred = rf.predict(X_train2)
    # estimate probability
    y_pred_proba = rf.predict_proba(X_train2)
    print(f'The Baseline Accuracy is: \n', round(baseline_accuracy, 4))
    print("________________________________________________")
    print('Accuracy of Logit 1 Model on Train: \n', round(logit1.score(X_train2, y_train2),4))
    print("________________________________________________")
    print('Accuracy of Decision Tree Model on Train: \n', round(clf1.score(X_train2, y_train2),4))
    print("________________________________________________")
    print('Accuracy of KNN Model on Train: \n',round(knn.score(X_train2, y_train2),4))
    print("________________________________________________")
    print('Accuracy of Random Forest Classifier on Train: \n', round(rf.score(X_train2, y_train2),4))