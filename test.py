import pandas as pd

Data=[

    {"name":"ashutosh","age":25,"city":"lucknow"},
    {"name":"ram","age":15,"city":"delhi"},
    {"name":"shyam","age":45,"city":"Pune"},
    {"name":"seeta","age":22,"city":"punjab"}
]

data=pd.DataFrame(Data)

data.to_csv("data\data.csv",index=False)