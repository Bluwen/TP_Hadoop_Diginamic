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

## 2.1 Les services Hadoop nécessaires pour notre analyse

### HDFS ou Hadoop Distributed File System
C'est le système de fichiers distribué de Hadoop, donc sa couche de stockage.

Il a comme caractéristiques principales :
- d'avoir une forte tolérance aux pannes via la redondance des données
- d'être optimisé pour le traitement rapide de données volumineuses.
- de permettre le stockage et l'analyse de volumes importants de données via sa scalabilité.

### YARN ou Yet Another Resource Negotiator
C'est le gestionnaire de ressource de Hadoop.

Il permet à plusieurs application de partager les ressources d'un cluster Hadoop, en assurant une gestion efficace des ressources.

Il est composé de plusieurs élements :
- **Ressource Manager** coordonne l'utilisation des ressources du cluster
- **Node Manager** gère les ressources de chaque noeud individuel
- **Application Master** dirige l'exécution de chaque application

### Zookeeper
C'est un service pour la coordination et la gestion notamment ici du cluster HBase.

Il permet de surveiller et gérer l'état des noeuds dans un cluster. Il assure également la communication entre les différents composants et garantit la synchronisation et la cordination des actions dans un cluster. 

### HBase
C'est une base de données distribuée, open source, non relationnelle et orienté colonnes. Hbase utilise HDFS comme système de stockage, lui d'écrire et de lire des grands volumes de données.

Il est composé de deux noeuds :
- **Master** qui gère les opérations du cluster et utilise **Zookeeper** pour la coordination
- **RegionServer** qui héberge les tables HBase et gère les opérations de lecture et d'écriture

## 2.2 Liste des commandes pour lancer les conteneurs et services Hadoop
### 2.2.1

Lancer les conteneurs dockers sur la machine distante : 
```bash
./start_docker_digi.sh
```
```bash
./bash_hadoop_master.sh
```

### 2.2.2
Pour démarrer les services HDFS et YARN :
```bash
./start-hadoop.sh
```

### 2.2.3
Lancer les services HBase et Zookeeper :
```bash
start-hbase.sh
```

### 2.2.4
Enfin pour pouvoir utiliser happybase avec HBase il faut lancer la librarie Thrift:
```bash
hbase-deamon.sh start thrift
```

# 3. Importer les données dans HDFS
- Décrivez la manière dont vous allez importer les données pour qu'elles puissent être traitées avec MapReduce.
- Précisez où stocker les fichiers

# 4. Créer et exécuter un job MapReduce
- Expliquer la structure d'un job MapReduce (mapper, reducer)
- Donnez les commandes à exécuter pour soumettre le job sur Hadoop

# 5. Visualiser les résultats
- Décrivez comment récupérer les résultats que se soit MapReduce ou Hbase.
- Indiquez comment trouver les données générées comme avec Matplotlib, Pandas...

# 6.Récupérer les résultats
- Expliquez comment récupérer les fichiers de sortie du job MapReduce depuis HDFS pour le mettre sur la partie linux de votre container hadoop-master.
- Donnez la procédure pour récupérer les données du container jusque son pc local.