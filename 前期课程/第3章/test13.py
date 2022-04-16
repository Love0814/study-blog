# coding = utf-8

"""
如下字典，将键和值对换，即键作为值，值作为键。
d= ("book': ['python', 'datascience'],
'author' :'laoqi', 'publisher':'phei'}
"""

import collections.abc

d = {"book": ["python", "datascience"], "author": "laoqi", "publisher": "phei"}
dd = {}
"""
for k,v in d.items():
    if isinstance(v, collections.abc.Hashable):
        dd[v] = k
    else:
        dd[tuple(v)] = k
"""

dd = {v if isinstance(v, collections.abc.Hashable) else tuple(v): k for k, v in d.items()}

print(dd)
