import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def _first_description(df: pd.DataFrame):
    print(df.head())
    print(df.describe())
    print(df.shape)


if __name__ == '__main__':
    events = pd.read_csv(r"events.csv")
    applicants = pd.read_csv(r"applicants.csv")
    sessions = pd.read_csv(r"sessions.csv")

    sessions_and_aplicanst = pd.merge(sessions, applicants, on="applicant_id")

    # df=sessions_and_aplicanst.describe(include="all", exclude = None)
    # encoder = LabelEncoder()
    # sessions_and_aplicanst["agent_name"] = encoder.fit_transform(sessions_and_aplicanst["agent_name"])
    sns.barplot(sessions_and_aplicanst, x="gender", y="session_status", hue="agent_name")
    plt.show()
