from sklearn.cluster import AgglomerativeClustering
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score 
import scipy.cluster.hierarchy as sch 
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean as dis


"""## Jerárquico divisivo"""


def encodear_en_0(X):
  return [0 for i in range(X.shape[0])]

def lista_cluster(X,labels,c):
  #index = X[:,2]
  #X = X[:,:2]
  lista = []
  for i,p in enumerate(X):
    if labels[i] == c:
      lista.append([p[0],p[1],i])
  return np.array(lista)

def diametro_cluster(x):
  distancias = []
  for i in range(x.shape[0]):
    for j in range(i+1,x.shape[0]):
      distancias.append(dis(x[i],x[j]))
  try:
    return max(distancias)
  except:
    return 0

def max_value(inputlist):
    return max([sublist[0] for sublist in inputlist])

def cluster_mas_grande(X,labels,clusters):
  #clusters_en_lista = []
  max_val = 0
  max_cluster = 0
  for c in clusters:
    #clusters_en_lista.append( lista_cluster(X,labels,c))
    diam = diametro_cluster(lista_cluster(X,labels,c))
    if diam > max_val:
      max_val = diam
      max_cluster = c
  return max_cluster
          #max([ diametro_cluster(x) for x in clusters_en_lista])

def dis_promedio_punto(p,x):
  #if x.shape[0] == 1:
  #  return 0
  punto_en_cluster = False
  suma_distancias = 0
  for punto in x:
    for i in range(len(p)):
      if punto[i] == p[i]:
        punto_en_cluster = True
      else:
        punto_en_cluster = False
      
    suma_distancias += dis(p,punto)

  if punto_en_cluster:
    if len(x) == 1:
          #print('1')
          return 0
    else:
      #print('2')
      return suma_distancias/(len(x) - 1)
  else:
    #print('3')
    return suma_distancias/(len(x)) # le resto 1 porque en x está p también  #! VERIFICAR QUE SIRVE BIEN ¡¡

def disidente(x_i):
  disidente = 0
  max_prom = 0
  for punto in x_i:
    dis_promedio = dis_promedio_punto(punto[:2],x_i[:,:2])
    if dis_promedio > max_prom:
      max_prom = dis_promedio
      disidente = punto[2]
  return int(disidente)

def a_disidente(p,U,D):
  #print(len(p),p.shape,D.shape,U.shape)
  #print(dis_promedio_punto(p,D),dis_promedio_punto(p,U))
  if dis_promedio_punto(p,D) < dis_promedio_punto(p,U):
    return True
  else:
    return False

#X = X.tolist()
#for i in range(len(X)):
#  X[i].append(i)

#X = X[:,:2]
#X

def graficar_labels(X,labels):
  X = np.array(X)
  scatter_x = X[:,0]
  scatter_y = X[:,1]
  group = labels
  cdict = {0:'b', 1:'g', 2:'r', 3:'c', 4:'m', 5:'y', 6:'k', 7:'w'}

  
  #fig, ax = plt.subplots()
  plt.figure(figsize=(13,8))
  plt.xlabel('Midterm', fontsize = 20) 
  plt.ylabel('Final', fontsize = 20)
  for g in np.unique(group):
      ix = np.where(group == g)
      plt.scatter(scatter_x[ix], scatter_y[ix], c = cdict[g])
  plt.show()

def cluster_divisivo(X,k):  
  X = np.array(X)

  labels = encodear_en_0(X)
  #labels = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1]

  clusters = [0]

  #lista_cluster(X,labels,0)
  #diametro_cluster(X)
  #cluster_mas_grande(X,labels,clusters)
  #dis_promedio_punto(X[0],X[1,:])  # usar esta manera de pasar ---> X[:,:]  <---

  for z in range(k-1):

    # Obtengo el mayor cluster
    cluster_mayor_label = cluster_mas_grande(X,labels,clusters)
    cluster_mayor_lista = lista_cluster(X,labels,cluster_mayor_label)
    #print(cluster_mayor_lista.shape)

    # Obtengo el disidente que hace su nuevo cluster
    disi = disidente(cluster_mayor_lista)
    clusters.append(clusters[-1]+1)
    labels[disi] = clusters[-1]
    cluster_mayor_lista = lista_cluster(X,labels,cluster_mayor_label)
    cluster_menor_lista = lista_cluster(X,labels,clusters[-1])
    #print(cluster_mayor_lista.shape,cluster_menor_lista.shape)

    m = cluster_menor_lista.copy()
    M = cluster_mayor_lista.copy()
    #print(M[:,:2],m[:,:2])
    #a_disidente(cluster_mayor_lista[60][1:2],M[:,:2],m[:,:2])

    # Paso los puntos al grupo disidente
    hubo_cambios = True
    max_cambios = 10
    cambios = 0
    while hubo_cambios == True and cambios != max_cambios:
      #print(3)
      hubo_cambios = False
      for i in range(len(cluster_mayor_lista)):
        #print(labels)
        #print()
        if a_disidente(cluster_mayor_lista[i][:2],M[:,:2],m[:,:2]):
          hubo_cambios = True
          #print(int(cluster_mayor_lista[i][2]))
          labels[int(cluster_mayor_lista[i][2])] = clusters[-1]
          #print(int(cluster_mayor_lista[i][2]))
          M = lista_cluster(X,labels,cluster_mayor_label)
          m = lista_cluster(X,labels,clusters[-1])
      cambios += 1
      #input("Press Enter to continue...")
      #graficar_labels(X,labels)
    #print(list(labels))

  return(list(labels))






# Ejemplo de uso que divide en 2 clusters y grafica:

#my_data = pd.read_csv('/content/class-grades.csv')
#X = my_data.drop(columns=['Company','Unnamed: 0'])
#my_data = my_data[['Midterm','Final']]
#X = my_data


#graficar_labels(X,cluster_divisivo(X,2))

