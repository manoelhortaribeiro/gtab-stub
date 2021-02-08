import pandas as pd
import gtab

df = pd.read_csv("./data/country_codes_filtered.csv")


# this creates a new folder to the gtab!
my_path = "./anchorbanks"
t = gtab.GTAB(dir_path=my_path)

for i in df.Code.values[::-1]:
    try:
        t.set_options(pytrends_config={"geo": i,
                                       "timeframe": "2019-01-01 2020-12-31"})
        t.create_anchorbank()  # takes a while to run since it queries Google Trends.
    except:
        print("error", i)
