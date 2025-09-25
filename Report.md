# 1. Connexion à la machine virtuelle

## 1.1 Ligne de commande :

Initialisé la connection en entrant la commande.

```bash
ssh [user_name]@[url/IP] -p [port]
```
Puis entrer le mots de pass de l'utilisateur.

![ssh](./ScreenShot/ssh.png)

## 1.2 PuTTY :

Entrer l'url/ip et le port public,
puis appuyez sur "Open".

![PuTTY](./ScreenShot/putty.png)

Ensuite précisé le nom utilisateur et le mots de passe du compte auquel vous vous connecté.

![PuTTY2](./ScreenShot/putty2.png)

# 2. Lancer les conteneurs et services Hadoop
- Expliquez les services nécessaires pour Hadoop (HDFS, YARN, Zookeeper, HBase)
- Indiquez les commandes nécessaire pour démarrer ces services sur la machine virtuelle.


# 3. Importer les données dans HDFS

Pour traiter des données avec MapReduce, il faut d’abord les importé dans le hdfs.
Pour ce faire, il faut exécuter la commande:

```bash
hdfs dfs -put path_to_data target_dir_in_hdfs
```

Vous pouvez ensuite afficher le dossier cible avec:
```bash
hdfs dfs -ls target_dir_in_hdfs
```


![Hdfs put](./ScreenShot/hdfs_put.png)



# 4. Créer et exécuter un job MapReduce
- Expliquer la structure d'un job MapReduce (mapper, reducer)
- Donnez les commandes à exécuter pour soumettre le job sur Hadoop

# 5. Visualiser les résultats

## 5.1 HBase

### 5.1.1 Interface en ligne de commande (CLI)

Pour interroger une table HBase via le CLI, commencez par lancer le shell :

```bash
hbase shell
```

Pour lister toutes les tables existantes dans HBase :

```bash
list
```

Utilisez la commande suivante pour afficher toutes les lignes d'une table :

```bash
scan "nom_de_la_table"
```

![Résultat scan HBase](./ScreenShot/hbase_result.png)

Chaque ligne sera affichée avec ses familles de colonnes, colonnes, timestamps et valeurs.

Vous pouvez aussi limité le nombre de résultat

```bash
scan "nom_de_la_table", {LIMIT => 10}
```

Pour afficher une ligne précise à partir de sa clé :

```bash
get "nom_de_la_table", "clé_de_ligne"
```

Pour afficher la définition d'une table (colonnes, familles, etc.) :

```bash
describe "nom_de_la_table"
```

### 5.1.1 python (happybase)

Pour interagir avec HBase en Python, on peut utiliser la bibliothèque `happybase`, qui permet de se connecter à HBase via Thrift.

Exemple de récupération des données depuis une table nommée `dance_energy_stats` :

Ce script établit une connexion avec le serveur HBase et de récupéré la table voulu.
```python
try:
    connection = happybase.Connection('hadoop-master')
    table = connection.table('dance_energy_stats')
except Exception as e:
    print("Connetion error: {0}".format(e), file=sys.stderr)
    sys.exit(1)
```

Ce script scanne la table ligne par ligne, extrait la valeur de la colonne `cf:mean_streams`, et stocke les résultats dans une liste Python.
```python
data = []
for key, row in table.scan():
    try:
        mean_streams = float(row[b'cf:mean_streams'])
        key = key.decode()
        data.append((key, mean_streams))
    except Exception as e:
        print('Parsing error: {0}'.format(e))

connection.close()
```

## 5.2 hdfs

### 5.2.1 shell

Après un traitement MapReduce, les résultats sont généralement stockés dans un répertoire HDFS, souvent sous forme de fichiers `part-00000`, `part-00001`, etc.

Pour vérifier leur présence :

```bash
hdfs dfs -ls target_hdfs_output_dir
```

Pour lire rapidement le contenu :

```bash
hdfs dfs -cat target_hdfs_output_dir/part-00000
```

Pour les extraire en local pour une visualisation avec Pandas ou Matplotlib :

```bash
hdfs dfs -get target_hdfs_output_dir/part-00000 target_output
```

### 5.2.2 python (pydoop.hdfs)

Pour lire directement les résultats MapReduce depuis HDFS en Python :

```python
import pydoop.hdfs as hdfs

with hdfs.open('target_hdfs_output_dir/part-00000') as f:
    contenu = f.read().decode()
```

Le contenu peut ensuite être parsé ou converti en DataFrame selon le format attendu.

# 6.Récupérer les résultats
- Expliquez comment récupérer les fichiers de sortie du job MapReduce depuis HDFS pour le mettre sur la partie linux de votre container hadoop-master.
- Donnez la procédure pour récupérer les données du container jusque son pc local.