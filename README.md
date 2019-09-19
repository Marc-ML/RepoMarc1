# Semaine 1 : Fondamentaux de Python

## Résumé de la semaine

Nous mettons un premier pied à l'étrier avec cette semaine d'introduction à Python. Retenez dans cette partie quelques choses intéressantes


### Les conditions & les boucles

Ceci est la base de tout langage de programmation. Souvenez vous donc :

  1. Des différents opérateurs liés aux conditions
    * ```==``` --> égal à
    * ```!=``` --> Différent de
    * ```<=``` --> Inférieur ou égal à

  2. Vous utiliserez principalement les boucles ``for``

  3. N'oubliez pas que Python est sensible aux tabulations. C'est d'ailleurs comme cela que le langage a été construit. De fait, n'oubliez pas de les mettre au bon endroit lorsque vous créez vos blocs de code. Ex:
  ```python
  if a == 2:
    print("{} equals 2".format(a))
  ```


### Fonctions et collections de données

Dans cette partie, il est important de vous souvenir que les fonctions servent :

  1. Ne pas vous répéter
  2. Vous pouvez définir des arguments ou non
  3. Si vous définissez des arguments, il est bon de définir des arguments par défaut. Ex:
  ```python
  def hello_world(name=None):
    if name==None:
      print("Hello Mister Nobody")
    else:
      print("Hello {}".format(name))

  ```

Pour ce qui est des collections de données, souvenez-vous principalement des listes, des tuples ainsi que des dictionnaires. Ce sont les types de données que vous verrez le plus souvent.

Souvenez-vous aussi des `list comprehension` qui sont extrêmement souvent utilisées en code. Voici un exemple extrêmement simple :  

```
[i for i in range(10)]
```

### Programmation Orientiée Objet

Vous monterez en compétence au fur et à mesure sur ce qui est la POO. Ne vous stressez pas cependant du fait de ne pas être à l'aise avec les concepts pour le moment.

Souvenez-vous principalement du vocabulaire :

1. Un objet ---> Tout instance de classe est un objet
2. Un attribut ---> Tout élément dans une classe est un attribut
3. Une méthode ---> Est une fonction dans une classe

Souvenez vous ensuite de la structure d'une classe :

```python

class Hello:
  def __init__(self, name):
    self.name = name

  def bonjour():
    print("Bonjour {}".format(self.name))

hello = Hello("Antoine")
hello.bonjour()

>>>> "Bonjour Antoine"

```

### Pandas

Pandas est une librairie extrêmement populaire en Data Science. Il est bon que vous passiez un peu de temps dessus pour vous familiariser en profondeur avec ceci.

Principalement, souvenez vous :

  1. Les deux nouveaux types de données --> DataFrame & Series
  2. Souvenez-vous comment localiser des données avec ```loc``` & ```iloc```
  3. Souvenez-vous comment utiliser ```.apply(lambda x: )```
  4. Souvenez-vous comment manipuler des bases de données avec ```GroupBy```
  5. Souvenez-vous que vous pouvez lire n'importe quel type de fichiers avec ```pd.read_```


### Numpy

Numpy est la seconde librairie populaire à connaître en Data Science. Elle sert particulièrement pour la manipulation de tenseurs.

Principalement, souvenez vous :

  1. Créer un tenseurs via `np.array()``
  2. Les manipulations basiques
  3. La forme d'un tenseur avec `.shape`
  4. Manipuler la forme d'un tenseur avec `.reshape()`
