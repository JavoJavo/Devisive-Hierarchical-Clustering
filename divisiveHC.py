import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean as dis


"""## Jerárquico divisivo"""


def encodear_en_0(X):
  # Given a dataframe
  # Makes a list of ceros which are the initial labels
  return [0 for i in range(X.shape[0])]

def lista_cluster(X,labels,c):
  # Given a dataframe, their respective labels and a single label
  # Returns a list of points (x, y) which have label 'c' and their respective index
  #index = X[:,2]
  #X = X[:,:2]
  lista = []
  for i,p in enumerate(X):
    if labels[i] == c:
      lista.append([p[0],p[1],i])
  return np.array(lista)

def diametro_cluster(x):
  # Given a dataframe
  # Returns the maximum distance between two points in it
  distancias = [0] # Initialized with a cero for clusters of 1 point that won´t enter the loop below
  for i in range(x.shape[0]):
    for j in range(i+1,x.shape[0]):
      distancias.append(dis(x[i],x[j]))
  return max(distancias)

#def max_value(inputlist):
#    return max([sublist[0] for sublist in inputlist])

def cluster_mas_grande(X,labels,clusters):
  # Given a dataframe, its labels, and a list of unique labels contained in labels
  # Returns the label of the biggest cluster (the one with the biggest diameter)
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
  # Given a point and a dataframe
  # Returns the mean distance between the point and each point in the dataframe
  punto_en_cluster = False

  suma_distancias = 0
  for punto in x:
    for i in range(len(p)):
      if punto[i] == p[i]:
        punto_en_cluster = True
    suma_distancias += dis(p,punto)

  if punto_en_cluster:
    if len(x) == 1:  # Is this len() fail proof?
          return 0
    else:
      return suma_distancias/(len(x) - 1)  # le resto 1 porque en x está p también  #! VERIFICAR QUE SIRVE BIEN ¡¡
  else:
    return suma_distancias/(len(x)) 

def disidente(x_i):
  # Given a dataframe with (x,y,i) where i is the index
  # Returns the index of the point in the dataframe which in average is farther apart from the rest
  disidente = 0
  max_prom = 0
  for punto in x_i:
    dis_promedio = dis_promedio_punto(punto[:2],x_i[:,:2])
    if dis_promedio > max_prom:
      max_prom = dis_promedio
      disidente = punto[2]
  return int(disidente)

def a_disidente(p,U,D):
  # Given a point, the father dataframe and the disident dataframe
  # Returns True if the point should be in the disident dataframe using average distance
  #print(len(p),p.shape,D.shape,U.shape)
  #print(dis_promedio_punto(p,D),dis_promedio_punto(p,U))
  if dis_promedio_punto(p,D) < dis_promedio_punto(p,U):
    return True
  else:
    return False

def not_disidente(p,U,D):
  # Given a point, the father dataframe and the disident dataframe
  # Returns True if the point should NOT be in the disident dataframe using average distance
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
  cdict = {0:'b', 1:'g', 2:'r', 3:'c', 4:'m', 5:'y', 6:'k'}#, 7:'w'}
  plt.figure(figsize=(13,8))
  #plt.xlabel('Midterm', fontsize = 20) 
  #plt.ylabel('Final', fontsize = 20)
  for g in np.unique(group):
      ix = np.where(group == g)
      plt.scatter(scatter_x[ix], scatter_y[ix], c = cdict[g%7])
  plt.show()

def cluster_divisivo(X,k): 
  if X.shape[0] < k:
    import warnings
    warnings.warn('k number of clusters can´t be larger than number of points in the dataframe')
    return None
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
    max_cambios_no_disi = X.shape[0]*2
    cambios = 0
    while hubo_cambios == True and cambios != max_cambios_no_disi:
      #print(3)
      hubo_cambios = False
      for i in range(len(cluster_mayor_lista)):
        #print(labels)
        #print()
        if labels[int(cluster_mayor_lista[i][2])] == cluster_mayor_label:
          if a_disidente(cluster_mayor_lista[i][:2],M[:,:2],m[:,:2]):
            hubo_cambios = True
            #print(int(cluster_mayor_lista[i][2]))
            labels[int(cluster_mayor_lista[i][2])] = clusters[-1]
            #print(int(cluster_mayor_lista[i][2]))
            M = lista_cluster(X,labels,cluster_mayor_label)
            m = lista_cluster(X,labels,clusters[-1])
        else:
          #print('hola')
          if not a_disidente(cluster_mayor_lista[i][:2],M[:,:2],m[:,:2]):
            #print('hubo')
            hubo_cambios = True
            #print(int(cluster_mayor_lista[i][2]))
            labels[int(cluster_mayor_lista[i][2])] = cluster_mayor_label
            #print(int(cluster_mayor_lista[i][2]))
            M = lista_cluster(X,labels,cluster_mayor_label)
            m = lista_cluster(X,labels,clusters[-1])
            cambios += 1

  return(list(labels))
