# https://www.hackerrank.com/challenges/predicting-house-prices

from sklearn import linear_model
import pandas as pd


def main():
    features_count, feature_line_count = [int(x) for x in raw_input().split()]
    features = []
    for i in xrange(0, feature_line_count):
        features.append([float(x) for x in raw_input().split()])

    training_data = pd.DataFrame(data=features)
    training_target = training_data.iloc[:, -1:]
    training_data = training_data.iloc[:, :-1]

    regression = linear_model.LinearRegression()
    regression.fit(training_data, training_target)

    predictions_line_count = int(input())
    predictions = []
    for i in xrange(0, predictions_line_count):
        predictions.append([float(x) for x in raw_input().split()])
    prediction_data = pd.DataFrame(data=predictions)

    result = regression.predict(prediction_data)
    for line in result:
        print("%.2f" % line[0])


if __name__ == '__main__':
    main()