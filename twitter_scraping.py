import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()

veri = trends.trending_searches(pn="turkey")  
print(veri.head(20)) #türkiyede en popüler aramalar 

'''
trends.build_payload(kw_list=["Data Science"])
data = trends.interest_by_region()
print(data['Data Science'].nlargest(10) ) #en yüksek değere sahip 10 ülke gelecek
#print(data.sample(10))  rastgele 10 tane yazdirir


df = data.sample(15)
df.reset_index().plot(x="geoName", y="Data Science", figsize=(120,16), kind="bar")
plt.show()
'''
'''
keyword = trends.suggestions(keyword="Programming")
data = pd.DataFrame(keyword)
print(data.head())
'''