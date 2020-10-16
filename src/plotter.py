import matplotlib.pyplot as plt

class Plot:
    def __init__(self, datas, perc_good, perc_bad):
        self.datas = datas
        self.perc_good = perc_good
        self.perc_bad = perc_bad
        self.width = 0.35       # the width of the bars: can also be len(x) sequence

    def build(self):
        fig, ax = plt.subplots()

        ax.bar(self.datas, self.perc_good, self.width, label='Boa')
        ax.bar(self.datas, self.perc_good, self.width, label='Ruim')

        ax.set_ylabel('Percentual')
        ax.set_title('Percentual entre aguas boas e ruins')
        ax.legend()

        plt.show()