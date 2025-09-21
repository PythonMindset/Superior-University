import csv
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

train=pd.read_csv("train.csv")
train=train.drop(["PassengerId","Ticket","Name"],axis=1)
test=pd.read_csv("test.csv")
test=test.drop(["PassengerId","Ticket","Name"],axis=1)

y_train=train["Survived"]
x_train=train.drop(["Survived"],axis=1)
x_test=test.copy()

# Filling missing values in Embarked
x_train["Embarked"]=x_train["Embarked"].fillna(x_train["Embarked"].mode()[0])
x_test["Embarked"]=x_test["Embarked"].fillna(x_test["Embarked"].mode()[0])

# Filling missing values in Age
x_train["Age"]=x_train["Age"].fillna(x_train["Age"].median())
x_test["Age"]=x_test["Age"].fillna(x_test["Age"].median())

# Changing Cabin to Cabin desk and filling missing values
x_train["CabinDeck"]=x_train["Cabin"].astype(str).str[0]
x_train["CabinDeck"]=x_train["CabinDeck"].replace("n","Missing")
x_train=x_train.drop("Cabin",axis=1)

x_test["CabinDeck"]=x_test["Cabin"].astype(str).str[0]
x_test["CabinDeck"]=x_test["CabinDeck"].replace("n","Missing")
x_test=x_test.drop("Cabin",axis=1)

le=LabelEncoder()
# Encoding categorical features
x_train["Embarked"]=le.fit_transform(x_train["Embarked"])
x_test["Embarked"]=le.transform(x_test["Embarked"])

x_train["CabinDeck"]=le.fit_transform(x_train["CabinDeck"])
x_test["CabinDeck"]=le.transform(x_test["CabinDeck"])

x_train["Sex"]=le.fit_transform(x_train["Sex"])
x_test["Sex"]=le.transform(x_test["Sex"])

rf_model=RandomForestClassifier(random_state=42)
rf_model.fit(x_train,y_train)
prediction=rf_model.predict(x_test)

# output_prediction
psid=pd.read_csv("test.csv")["PassengerId"]
with open("submission.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["PassengerId","Survived"])
    for i in range(len(prediction)):
        writer.writerow([psid[i],prediction[i]])