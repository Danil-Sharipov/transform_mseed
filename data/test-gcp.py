from obspy import read
st = read("01/dbkge2_20221001_0000e.gcf")
for k, v in sorted(st[0].stats.gcf.items()):
    print("'%s': %s" % (k, str(v)))
print(st)
st2 = read("01/dbkge2_20221001_0015e.gcf")
print(st2)
print((st+st2).merge(method=-1)) 
# в конце нейм по 3 каналам проверка по названию? 