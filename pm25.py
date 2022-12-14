import pandas as pd

url = 'https://data.epa.gov.tw/api/v2/aqx_p_02?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=CSV'


def get_pm25():
    df = pd.read_csv(url).dropna()['county	site    pm25	datacreationdate'.split()]
    # print(df)

    return df.columns.tolist(), df.values.tolist()


if __name__ == '__main__':

    print(get_pm25())
