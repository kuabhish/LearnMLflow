import mlflow
import sys

with mlflow.start_run():
    if(sys.argv[1]):
        alpha = sys.argv[1]
    else:
        alpha = 1
    mlflow.log_param('alpha', alpha)
    print('The number you entered is:',alpha)
print('a')
print(mlflow.get_tracking_uri())
print('b')
