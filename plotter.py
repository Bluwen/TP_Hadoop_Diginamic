import happybase
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

try:
    connection = happybase.Connection('hadoop-master')
    table = connection.table('dance_energy_stats')
except Exception as e:
    print("Connetion error: {0}".format(e), file=sys.stderr)
    sys.exit(1)

data= []
for key, row in table.scan():
    try:
        mean_streams = float(row[b'cf:mean_streams'])
        key= key.decode()
        data.append((key,mean_streams))
    except Exception as e:
        print('Parsing error: {0}'.format(e))

connection.close()

df = pd.DataFrame(data, columns=["current_danceability:current_energy","mean_streams"])

top_10 =  df.nlargest(10,"mean_streams").reset_index(drop=True)

print(top_10)



plt.figure(figsize=(8, 8))

bar_color = ["#167288",
         "#8cdaec",
         "#b45248",
         "#d48c84",
         "#a89a49",
         "#d6cfa2",
         "#3cb464",
         "#9bddb1",
         "#643c6a",
         "#836394"]


plt.bar(top_10["current_danceability:current_energy"],top_10["mean_streams"],color=bar_color)
plt.grid(True,color = "lightgray", linestyle = "--")

plt.title('Top 10 des meilleurs combinaisons d\' énergie et de caractère dansant')
plt.ylabel("Moyenne du nombre streams")
plt.xlabel("Combinaison d'énergie et caractère dansant")
plt.savefig("./top_10_stream.pdf", format='pdf')