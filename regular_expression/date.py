import re

par="""
    in 10-8-2014 during my  trip to the 09-july-2004 , 
    I had the chance to meet some interesting people in november-2014. 
    One of them was a local artist named Sarah , 
    who told me about her latest exhibition in 10-01-2016. 
    She 02-aug-2001 gave me her number, which , 
    in case I wanted to attend 28-01-2003. 
    While exploring 10-aug-2014 the galleries, I bumped into my old friend Jake, 
    who had recently moved back to town.He mentioned his number, 
    and invited me to sep-2013 grab coffee later 31-december-2024.
"""
rexp=r'\d{2}\D\d{2}\D\d{4}|\d{2}\D\w+\D\d{4}|\w+\D\d{4}'

res=re.findall(rexp,par)
print(res)