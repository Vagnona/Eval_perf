import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_FOLDER = "./res/"

class data:
    def __init__(self, fichier):
        self.fichier = fichier

    def get_data(self, fichier):
        self.fichier = fichier
        self.rtt = int(fichier.split("-")[1].split(".")[0])
        # self.rtt = self.rtt
        self.df = pd.read_csv(self.fichier, delim_whitespace=True, header=None)
        self.df.columns = ["time", "x", "y", "z", "a", "b", "cwnd"]
            
        #On ne garde que la premiere et derniere colone
        self.df = self.df[["time", "cwnd"]]

    def plot(self, ax):
        self.df.plot(kind='line', x='time', y='cwnd', ax=ax, label=self.rtt)

liste_data = []

# Lire tout les fichiers csv dans le dossier DATA_FOLDER
for file in os.listdir(DATA_FOLDER):
    liste_data.append(data(DATA_FOLDER + file))

ax=plt.gca()
for data in liste_data:
    data.get_data(data.fichier)
    data.plot(ax)

plt.show()

# # On crée tout les dataframes
# dfs = []

# # On affiche tout les dataframes dans le meme graphique
# ax = plt.gca()
# for df in dfs:
#     df.plot(kind='line', x='time', y='cwnd', ax=ax, label=)

# plt.show()