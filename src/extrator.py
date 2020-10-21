f = open("./assets/base.csv","w")
f.write("data_amostra;ph;status\n2020-10-15;6.8;BOA\n2020-10-14;2.5;RUIM\n2020-10-13;9;RUIM\n")
f.close()

f = open("./config/base.csv", "r")

from plotter import Plot

datas = []
perc_good = []
perc_bad = []

pl = Plot( ['15/out','14/out'] , [70,30] , [45, 56])
pl.build()

for line in f:
    datas.append(line.split(";")[0])
    perc_good.append(line.split(";")[1])
    perc_bad.append(line.split(";")[2])