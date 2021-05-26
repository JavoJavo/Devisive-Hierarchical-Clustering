# Devisive-Hierarchical-Clustering
Divide a numerical dataset in k clusters using the divisive approach.
## Algorithm
1. We start with a cluster made up of all the points.
2. From that cluster the farthest point with respect to the other points (dissident) is located. The dissident forms its
own cluster. 
3. Then we iterate through all the points checking their average distance to both clusters (or the total clusters formed) ,
they are assigned to the closest cluster. We keep iterating until there are no more changes\.*
4. We repeat steps from 2 until k specified clusters are formed.
## Specs
- Distance is euclidean
- Distance between clusters is average distance between all posible pairs of their points
- For now it only works with 2 variables (feel free to collaborate).

## Example

```py
import seaborn as sns

iris = sns.load_dataset('iris')
iris = iris[['sepal_length','sepal_width']]
graficar_labels(iris,cluster_divisivo(iris,3))
```
![](https://github.com/JavoJavo/Devisive-Hierarchical-Clustering/blob/main/iris_k3.png)


