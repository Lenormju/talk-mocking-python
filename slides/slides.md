<!-- .slide: data-background-image="./sgalagaev--5iSCtrJX5o-unsplash.jpg" -->

# Dompter les mocks !

<!--
TODO:
* trouver une image de couverture
* style CSS pour que les titres ressortent sur les images
-->

---

## Merci aux sponsors

- TODO sponsors PyCon Fr 2025

-v-

## Présentation

Julien Lenormand

Notes:
- qui je suis : Pythonista, Craft, Test

---

# Introduction

TODO: image

Notes:
* objectif 5-6 minutes max, pour laisser du temps pour la démo, et pour la conclusion
* n'hésitez pas à poser vos questions tout du long, je verrai si j'ai le temps ou pas

-v-

## Pourquoi parler des mocks ?

* sujet un peu has been ?  <!-- .element: class="fragment" -->
* outil pratique !  <!-- .element: class="fragment" -->
* mais difficile à utiliser ...  <!-- .element: class="fragment" -->

Notes:
* mon histoire avec les mocks, le tuto que j'aurais voulu avoir en 2018

-v-

## Sondage

1. qui ne connaît pas du tout et veut découvrir ?  <!-- .element: class="fragment" -->
2. qui a déjà eu du mal à les utiliser et veut s'améliorer ?  <!-- .element: class="fragment" -->
3. qui maîtrise déjà et va un peu s'ennuyer ?  <!-- .element: class="fragment" -->

-v-

## Objectif

* Comprendre ce qu'est un mock  <!-- .element: class="fragment" -->
* Connaître les problèmes qu'il résout  <!-- .element: class="fragment" -->
  * et qu'il cause (!)  <!-- .element: class="fragment" -->
* Savoir les appliquer  <!-- .element: class="fragment" -->
  * sans trop galérer  <!-- .element: class="fragment" -->
  * et donc savoir les débugger !  <!-- .element: class="fragment" -->

---

# Un petit peu de théorie

TODO: image

-v-

## A quoi ça ressemble ?

```python
from unittest.mock import Mock

my_mock = Mock()
str(my_mock)  # <Mock id='127122938802736'>
```
<!-- .element: class="fragment" -->

```python
my_mock.toto  # pas d'erreur !
# <Mock name='mock.toto' id='127122938803408'>
```
<!-- .element: class="fragment" -->

```python
my_mock.toto.titi().tutu  # toujours pas d'erreur !
# <Mock name='mock.toto.titi().tutu' id='127122938804080'>
```
<!-- .element: class="fragment" -->

Notes:
* récursif

-v-

```python
from unittest.mock import MagicMock

len(Mock())  # TypeError: object of type 'Mock' has no len()
len(MagicMock())  # 0
Mock()[0]  # TypeError: 'Mock' object is not subscriptable
MagicMock()[0]  # <MagicMock name='mock.__getitem__()' id='127122939480112'>
```
<!-- .element: class="fragment" -->

```python
from unittest.mock import NonCallableMock

NonCallableMock()  # <NonCallableMock id='127122938805760'>
NonCallableMock()()  # TypeError: 'NonCallableMock' object is not callable
```
<!-- .element: class="fragment" -->

Notes:
* autres variantes : Property, Async, Threading (3.13 !)

-v-

## Des métamorphes !

![](./Metamorph-RFVF.png)

Notes:
* ils peuvent prendre n'importe quelle forme, et on peut même les configurer pour bidouiller

-v-

## A quoi ça sert ?

* à tester  <!-- .element: class="fragment" -->
  * rappel : c'est --TRÈS-- important de tester !  <!-- .element: class="fragment" -->
* "améliorer" des tests  <!-- .element: class="fragment" -->
  * FIRST : Fast, Independant, Repeatable, Self-sufficient, Timely  <!-- .element: class="fragment" -->

1. vérifier ou bloquer des interactions à l'intérieur du code  <!-- .element: class="fragment" -->
2. rendre pilotable certaines parties du code  <!-- .element: class="fragment" -->
* isoler des dépendances que je ne contrôle pas  <!-- .element: class="fragment" -->

--> rendre testable du code qui ne l'est pas tellement / pas du tout  <!-- .element: class="fragment" -->

Notes:
* TODO emoji "flèche vers la droite"
* besoin de "tricher" un peu
* pied de biche versus scalpel chirurgical

-v-

Quelques exemples de ce qui rend difficile de tester :

* le code intéragit avec une API, dont j'ai pas le login  <!-- .element: class="fragment" -->
* ou l'API est payante  <!-- .element: class="fragment" -->
* ou l'API est très lente  <!-- .element: class="fragment" -->
* ou l'API est instable  <!-- .element: class="fragment" -->
* ou l'API n'existe même pas encore !  <!-- .element: class="fragment" -->
* ou l'API renvoie parfois des erreurs  <!-- .element: class="fragment" -->
* ou le code dépend de l'heure actuelle  <!-- .element: class="fragment" -->
* ou dépend de l'aléatoire  <!-- .element: class="fragment" -->
* ou écrit son résultat sur stdout  <!-- .element: class="fragment" -->
* ...  <!-- .element: class="fragment" -->

Solution : tricher, modifier le programme

-v-

## Des doublures ?

![](./acteurs-et-doublures-11.png)  <!-- .element: class="fragment" -->

* dummy ou stub ou spy ou fake ou mock ?  <!-- .element: class="fragment" -->
* en Python, on ne fait que des `Mock` !  <!-- .element: class="fragment" -->

Notes:
* "point vocabulaire" sur les différentes formes de doublures
* en Python : une seule classe pour tout faire, donc on utilise le même terme pour tout, et peuvent être tout sauf des mocks
* according to Martin Fowler :
  * dummy : unused value, passed around
  * stub : canned answers
  * spy : stub + recording calls
  * fake : alternative implementation
  * mock : spy with pre-programmed expectations

---

# Mise en pratique !

TODO: image

Notes:
* IDE, thème clair
* TODO: démo de la fragilité du mock, et de la non-garantie que ça marche vraiment

-v-

## Première situation : météo incontrôlable !

Notes:
* le problème : je veux tester ma fonction météo, le test avec couverture montre qu'il y a des trous, que faire ?
  * schéma excalidraw
  * mock la fonction
  * mock la request
  * fake server
* mocker sans mock : le monkeypatching
* mocker avec mock : utiliser un Mock
* mocker proprement : patch

-v-

## Seconde situation : TODO

Notes:
* système d'import et modèle objet
* tout est objet !
* memory_graph

-v-

## Troisième situation : pytest

TODO

Notes:
* fixtures
* monkeypatch

-v-

## Le recap !

* c'est quoi un mock
* à quoi ça sert
* comment on l'applique : patch, patch.object

---

# Conclusion

TODO: image

-v-

## Conclusion

* les mocks c'est bien : isolation, perf, économies, ...
* les mocks c'est mal : isolation, fragilité, complexité, ...
* repenser l'architecture et la stratégie de test :
  * adapter pattern (narrow width)
  * inversion de dépendance (SOLID)
  * architecture héxagonale etc...
  * fakes --> simulateurs
  * TestContainers
  * contract testing
  * mock en dernier recours

Notes:
* too much mocking, "mocking hell", complexité, test de mock, "quand on a un marteau ..."
* symptome d'une archi ou strat de test ratée (ou même pas visée du tout)
* béquille

---

# Pour aller + loin

* Doc de Python :
  * [`unittest.mock` — mock object library](https://docs.python.org/3/library/unittest.mock.html)
  * [`unittest.mock` — getting started](https://docs.python.org/3/library/unittest.mock-examples.html)
* [Julien Lenormand - Tout comprendre des mocks Python](https://kaizen-solutions.net/kaizen-insights/articles-et-conseils-de-nos-experts/tout-comprendre-des-mocks-python/)
* Julien Lenormand et Jonathan Gaffiot - L'enfer des tests autos, bientôt en replay
* TODO mon article archi héxa + replay youtube
* [Martin Fowler - Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)
* [Hynek Schlawack - “Don’t Mock What You Don’t Own” in 5 Minutes](https://hynek.me/articles/what-to-mock-in-5-mins/)
* [Brett Schuchert et Tim Ottinger - tests "FIRST"](https://agileinaflash.blogspot.com/2009/02/first.html)
* TODO design pattern guru : adapter
* [`mock_open`](TODO), [`fakefs`](TODO), fakes locaux pour les services Cloud, [`responses`](TODO) pour `requests`, [VCR](TODO), [`act`](TODO) pour les GitHub Actions, [`TODO.StringIO`](TODO) au lieu d'un `fd`, ...
* TODO podcasts ?
* programmation fonctionnelle

---

# Crédits photos

* TODO
* Photo of a rabbit by by [Степана](https://unsplash.com/@sgalagaev>Ансплэш) on [Unsplash](https://unsplash.com/photos/brown-rabbit-on-window-during-daytime--5iSCtrJX5o)
* [linternaute.com - Les acteurs et leurs doublures](https://www.linternaute.com/lifestyle/loisirs/1174307-les-acteurs-et-leurs-doublures/)
* [pokepedia.fr - Métamorph](https://www.pokepedia.fr/Fichier:M%C3%A9tamorph-RFVF.png)

---

# Remerciements

* Lucie Anglade pour la proposition inespérée !
  * (et la personne qui s'est décommandée)
* Bas Terwijn pour la lib [`memory_graph`](https://memory-graph.com/)
* Kaizen Solutions pour m'avoir sponsorisé pour l'écriture de mon premier article

---

<!-- .slide: data-background-image="./sgalagaev--5iSCtrJX5o-unsplash.jpg" -->

#

Notes:
* merci à vous
* voici une photo de lapin mignon, pour votre courage

---

# Questions

Slides : [https://github.com/Lenormju/talk-mocking-python/](https://github.com/Lenormju/talk-mocking-python/)

Notes:
* TODO QRcode vers les slides : https://github.com/Lenormju/talk-mocking-python/

---

# Extra (en vrac)

1. lib `mock` est pour Python < 3.3 (2012, ajout à la stdlib)
2. donner un `name` aux mocks, pour faciliter le debug
3. école *mockist* de London versus école *classicist* de Detroit
4. Dependency Inversion != Dependency Injection
5. Pytest = `assert` efficace, pas besoin de `class`, des fixtures, des plugins
6. Comment mesurer la fiabilité des tests ? Et leur maintenabilité ?
7. Définition de "test unitaire" ?
8. Définition de "legacy" ?
9. Quel intérêt au "collaboration testing" (tester le "how") ?

---

# Abstract

Si vous avez déjà essayé de mocker, vous avez sûrement eu du mal à bien les appliquer.
Si vous en avez plein vos tests, vous avez surement remarqué qu'ils sont faillibles et fragiles.
Mais ils peuvent aussi être très puissants, ce qui les rend très utiles pour le test.

Afin de les utiliser efficacement, il faut d'abord **comprendre vraiment** comment ils fonctionnent, leur interaction avec le système d'import, le modèle objet de Python, et l'architecture des programmes.
En particulier, il faudra apprendre à discerner les "références" que Python utilise partout (des sortes de "pointeurs"), et les concepts d'immutabilité et de passage-par-copie/référence.
Avec tous ces savoirs, vous pourrez prédire le comportement des mocks, et réussir à les utiliser sereinement.
Vous confronterez alors cette compréhension à des exercices concrets de comment appliquer des mocks.
Enfin, vous aurez des conseils d'outils à utiliser pour tirer un maximum de vos mocks, mais surtout de quand ne pas les utiliser.
