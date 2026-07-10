import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import(
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
import matplotlib.pyplot as plt
df=pd.read_csv("datasets/student_dataset.csv")

X=df[["G2","G1","failures"]]
Y=df["G3"]
X_train,X_test,Y_train,Y_test=train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
    )
model=LinearRegression()
model.fit(X_train,Y_train)
Prediction=model.predict(X_test)
result=pd.DataFrame({
      "Results":Y_test,
      "Predictions":Prediction
      })
print(result)
mae=mean_absolute_error(Y_test,Prediction)
mse=mean_squared_error(Y_test,Prediction)
rmse=mse**0.5
r2=r2_score(Y_test,Prediction)
train_score=model.score(X_train,Y_train)
test_score=model.score(X_test,Y_test)
print(f" MAE: {mae:.3f} RMSE: {rmse:.3f} R2 Score: {r2:.3f} Train Score: {train_score:.3f} Test Score: {test_score:.3f}")
plt.scatter(Y_test,Prediction)
plt.xlabel("Actual G3")
plt.ylabel("Predicted G3")
plt.title("Actual G3 VS Predicted G3")
plt.show()
