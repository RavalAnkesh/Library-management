import re
para="""
    During my recent trip to the city (123) 12-3456, I had the chance to meet some interesting people. 
    One of them was a local artist named Sarah , (123) 234-9081, who told me about her latest exhibition. 
    She gave me her number, which is 9508560231, in case I wanted to attend +91 9102134. 
    While exploring the galleries, I bumped into my old friend Jake, who had recently moved back to town.
    He mentioned his number, (123) 456-7890, and invited me to grab coffee later. 
    Finally, I also connected with a travel blogger named Mark,who shared his experience 
    in the city and left me his mobile number, 9313145643, for future travel tips. 
    It was a 990219090 memorable day filled with creativity +91 9907653490 and old friendship
"""
p=r'\d{10}|(?:\+91\s?\d{10})|\(\d{3}\) \d{3}\D\d{4}'
res=re.findall(p,para)
print(res)