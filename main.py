import pandas as pd
from tqdm import trange


def _first_description(df: pd.DataFrame):
    print(df.head())
    print(df.describe())
    print(df.shape)


if __name__ == '__main__':
    events = pd.read_csv(r"events.csv")
    applicants = pd.read_csv(r"applicants.csv")
    sessions = pd.read_csv(r"sessions.csv")
    # encoder = LabelEncoder()
    # events["event_type"] = encoder.fit_transform(events["event_type"])

    sessions["gender"] = None
    for i in trange(sessions.shape[0]):
        sessions["gender", i] = applicants["gender", sessions["applicant_id"] == applicants["applicant_id"]]
