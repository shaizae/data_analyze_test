import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


def _first_description(df: pd.DataFrame):
    print(df.head())
    print(df.describe())
    print(df.shape)


if __name__ == '__main__':
    events = pd.read_csv(r"events.csv")
    applicants = pd.read_csv(r"applicants.csv")
    sessions = pd.read_csv(r"sessions.csv")
    encoder = LabelEncoder()
    events["event_type"] = encoder.fit_transform(events["event_type"])

    sns.barplot(data=sessions, x="applicant_id", y="session_status")
    plt.show()
