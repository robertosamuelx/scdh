# 6 a 7, agua boaaa 
# 2 a 5, ruim 
# 8 a 10 ruim tambem

agua_um = [1]
agua_dois = [1]
agua_tres = [1]

agua_quatro = [0]
agua_cinco = [0]
agua_seis = [0]

agua_sete = [0]
agua_oito = [0]
agua_nove = [0]

aguas_boas = [agua_um, agua_dois, agua_tres]
aguas_boas_classf = [1, 1, 1]
aguas_ruins = [agua_quatro, agua_cinco, agua_seis, agua_sete, agua_oito, agua_nove]
aguas_ruins_classf = [0, 0, 0, 0, 0, 0]
todas_aguas = aguas_boas + aguas_ruins
todas_aguas_classf = aguas_boas_classf + aguas_ruins_classf

print(aguas_boas)
print(aguas_ruins)
print(todas_aguas)

print(aguas_boas_classf)
print(aguas_ruins_classf)
print(todas_aguas_classf)

from sklearn.svm import LinearSVC

model = LinearSVC()
model.fit(todas_aguas, todas_aguas_classf)

agua_x = [0]
agua_y = [1]
agua_z = [1]

predict = model.predict([agua_x, agua_y, agua_z])

print(predict)