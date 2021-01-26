# Devisive-Hierarchical-Clustering
Por ahora sólo aglomera con dataframes de 2 variables, pero sería relativamente fácil hacer que lo haga con n variables.

## Ejemplo de uso que divide en 2 clusters y grafica:

```py
import seaborn as sns

iris = sns.load_dataset('iris')
iris = iris[['sepal_length','sepal_width']]
graficar_labels(iris,cluster_divisivo(iris,3))
```
      
![image](https://user-images.githubusercontent.com/28678081/105900684-010fea80-5fe2-11eb-9ea0-d6f40afa998d.png)


