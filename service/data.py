# 데이터 불러오는 모듈
import pandas as pd


def load_data():
    train = pd.read_csv("./data/train.csv")
    test = pd.read_csv("./data/test.csv")
    submission = pd.read_csv("./data/submission.csv")

    return train, test, submission
