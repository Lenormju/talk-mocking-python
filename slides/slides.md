<style>
.reveal section[data-background-image] h1:not(:empty) {
  background: rgba(0, 0, 0, 0.6);
  padding: 20px 40px;
  border-radius: 10px;
  display: inline-block;
  color: AliceBlue;
}
</style>

<!-- .slide: data-background-image="./Lion_tamer_(LOC_pga.03749).jpg" -->

# Dompter les mocks !

<!--
TODO:
-->

---

<!-- .slide: data-background-image="./sebastian-coman-photography-ZGgIYaL9lYk-unsplash.jpg" -->

# Introduction

Notes:
* objectif 5-6 minutes max, pour laisser du temps pour la démo, et pour la conclusion

-v-

## Julien Lenormand

Slides : [https://github.com/Lenormju/talk-mocking-python/](https://github.com/Lenormju/talk-mocking-python/)

<img src="./qr-code-slides.png" width="600">

Notes:
* qui je suis : Pythonista, Craft, Test
* n'hésitez pas à poser vos questions tout du long, je verrai si j'ai le temps ou pas
* les slides sont disponibles en ligne, je remets le QR code à la fin

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

<!-- .slide: data-background-image="./vitaly-gariev-Z0s6MM2YD8g-unsplash.jpg" -->

# Un petit peu de théorie

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

.

1. vérifier ou bloquer des interactions à l'intérieur du code  <!-- .element: class="fragment" -->
2. rendre pilotable certaines parties du code  <!-- .element: class="fragment" -->
3. isoler des dépendances que je ne contrôle pas  <!-- .element: class="fragment" -->

➡️ rendre testable du code qui ne l'est pas tellement / pas du tout  <!-- .element: class="fragment" -->

Notes:
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

Solution : tricher, modifier le programme  <!-- .element: class="fragment" -->

-v-

## Des doublures ?

![](./acteurs-et-doublures-11.png)  <!-- .element: class="fragment" -->

* dummy ou stub ou spy ou fake ou mock ?  <!-- .element: class="fragment" -->
* en Python, on ne fait que des Mock !  <!-- .element: class="fragment" -->

Notes:
* "point vocabulaire" sur les différentes formes de doublures
* en Python : une seule classe pour tout faire, donc on utilise le même terme pour tout, et peuvent être tout sauf des mocks
* according to Martin Fowler :
  * dummy : unused value, passed around
  * stub : canned answers
  * spy : stub + recording calls
  * fake : alternative implementation
  * mock : spy with pre-programmed expectations

-v-

![](./Crash-test-with-airbag-and-safty-belt.jpg)

---

<!-- .slide: data-background-image="./godfrey-nyangechi-YzKdrThXLIk-unsplash.jpg" -->

# Mise en pratique !

Notes:
* IDE, thème clair
* TODO: démo de la fragilité du mock, et de la non-garantie que ça marche vraiment

-v-

## Première situation : météo incontrôlable !

Notes:
* j'ai du code qui dépend de la météo
* run les tests
* run les tests avec couverture
* problème !
* schéma excalidraw
* mock la fonction : monkeypatching avec mock, puis sans mock
* mock l'exception : side_effect
* problème : test le if, et pas le get_weather
* mock le requests.get
* couverture !
* interface : tradeoff, status_code
* mocker proprement : patch
* configurer

-v-

## Seconde situation : TODO

Notes:
* système d'import et modèle objet
* tout est objet !
* memory_graph
* "where to patch" : where defined versus where used
* Zen of Python : "Namespaces are one honking great idea -- let's do more of those!"

-v-

## Troisième situation : pytest

TODO

Notes:
* fixtures
* monkeypatch
* plugins :
  * pytest-freezer
  * pytest-mock
  * pytest-azure
  * pytest-bigquery-mock
  * pytest-boto-mock
  * pytest-http-mocker
  * pytest-minio-mock
  * pytest-mock-api
  * pytest-mockredis
  * pytest-mocktcp
  * ...

---

<!-- .slide: data-background-image="./trainer-puts-his-head-lions-600w-2397220271.png" -->

# Conclusion

-v-

## Conclusion

* les mocks c'est bien : isolation, perf, économies, ...  <!-- .element: class="fragment" -->
* les mocks c'est mal : isolation, fragilité, complexité, ...  <!-- .element: class="fragment" -->
* repenser l'architecture et la stratégie de test :  <!-- .element: class="fragment" -->
  * adapter pattern (narrow width)  <!-- .element: class="fragment" -->
  * inversion de dépendance (SOLID)  <!-- .element: class="fragment" -->
  * architecture héxagonale etc...  <!-- .element: class="fragment" -->
  * fakes --> simulateurs  <!-- .element: class="fragment" -->
  * TestContainers  <!-- .element: class="fragment" -->
  * contract testing  <!-- .element: class="fragment" -->
  * ...  <!-- .element: class="fragment" -->
  * mock en dernier recours  <!-- .element: class="fragment" -->

Notes:
* too much mocking, "mocking hell", complexité, test de mock, "quand on a un marteau ..."
* symptome d'une archi ou strat de test ratée (ou même pas visée du tout)
* béquille

---

# Pour aller + loin

* concernant les mocks :
  * [`unittest.mock` — mock object library](https://docs.python.org/3/library/unittest.mock.html)
  * [`unittest.mock` — getting started](https://docs.python.org/3/library/unittest.mock-examples.html)
  * [Julien Lenormand - Tout comprendre des mocks Python](https://kaizen-solutions.net/kaizen-insights/articles-et-conseils-de-nos-experts/tout-comprendre-des-mocks-python/)
  * [Martin Fowler - Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)
  * [Hynek Schlawack - “Don’t Mock What You Don’t Own” in 5 Minutes](https://hynek.me/articles/what-to-mock-in-5-mins/)
  * [Philippe Bourgau - Careless Mocking Considered Harmful](https://philippe.bourgau.net/careless-mocking-considered-harmful/)
  * [Ned Batchelder - Why your mock doesn’t work](https://nedbatchelder.com/blog/201908/why_your_mock_doesnt_work.html)
  * [`mock_open`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.mock_open), [`fakefs`](https://pypi.org/project/pyfakefs/), fakes locaux Cloud, [`responses`](https://pypi.org/project/responses/), [VCR.py](https://pypi.org/project/vcrpy/), [`io.StringIO`](https://docs.python.org/3/library/io.html#io.StringIO), ...
* sur les tests auto :
  * Julien Lenormand et Jonathan Gaffiot - L'enfer des tests autos, bientôt en replay
  * [Brett Schuchert et Tim Ottinger - tests "FIRST"](https://agileinaflash.blogspot.com/2009/02/first.html)
  * [Robert C. Martin (Uncle Bob) - Test Contra-variance](https://blog.cleancoder.com/uncle-bob/2017/10/03/TestContravariance.html)
* sur l'architecture :
  * [Julien Lenormand - Une approche différente de l'architecture hexagonale](https://kaizen-solutions.net/kaizen-insights/articles-et-conseils-de-nos-experts/une-approche-differente-de-l-architecture-hexagonale/) et [replay vidéo](https://www.youtube.com/watch?v=GLAK047VNYk)
  * [adapter](https://refactoring.guru/design-patterns/adapter) ou [facade](https://refactoring.guru/design-patterns/facade) design patterns
  * programmation fonctionnelle (fonctions pures)

---

# Crédits photos

* [Степана on Unsplash - Brown rabbit on window during daytime](https://unsplash.com/photos/brown-rabbit-on-window-during-daytime--5iSCtrJX5o)
* [Godfrey Nyangechi on Unsplash - Black flat screen computer monitor](https://unsplash.com/photos/brown-rabbit-on-window-during-daytime--5iSCtrJX5o)
* [Vitaly Gariev on Unsplash - Professor writing complex mathematical equations on a chalkboard](https://unsplash.com/photos/black-flat-screen-computer-monitor-YzKdrThXLIk)
* [Sebastian Coman Photography on Unsplash - Small appetizers arranged on a silver plate](https://unsplash.com/photos/small-appetizers-are-arranged-on-a-silver-plate-ZGgIYaL9lYk)
* [linternaute.com - Les acteurs et leurs doublures](https://www.linternaute.com/lifestyle/loisirs/1174307-les-acteurs-et-leurs-doublures/)
* [pokepedia.fr - Métamorph](https://www.pokepedia.fr/Fichier:M%C3%A9tamorph-RFVF.png)
* [wikimedia.org - Lion tamer](https://commons.wikimedia.org/wiki/File:Lion_tamer_(LOC_pga.03749).jpg)
* [wikimedia.org - Crash test with airbag and safety belts](https://commons.wikimedia.org/wiki/File:Crash-test-with-airbag-and-safty-belt.jpg)
* [Valerii Mishanov - The trainer puts his head in the lion's mouth](https://www.shutterstock.com/image-vector/trainer-puts-his-head-lions-mouth-2397220271)

---

# Remerciements

* les sponsors, qui ont rendu cet évènement possible et accessible
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

LinkedIn : Julien Lenormand

Slides : [https://github.com/Lenormju/talk-mocking-python/](https://github.com/Lenormju/talk-mocking-python/)

<img src="./qr-code-slides.png" width="600">

---

# Extra (en vrac)

1. lib `mock` est pour Python < 3.3 (2012, ajout à la stdlib), ✝️ Michael Foord
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

> Si vous avez déjà essayé de mocker, vous avez sûrement eu du mal à bien les appliquer.
> Si vous en avez plein vos tests, vous avez surement remarqué qu'ils sont faillibles et fragiles.
> Mais ils peuvent aussi être très puissants, ce qui les rend très utiles pour le test.
> 
> Afin de les utiliser efficacement, il faut d'abord **comprendre vraiment** comment ils fonctionnent, leur interaction avec le système d'import, le modèle objet de Python, et l'architecture des programmes.
> En particulier, il faudra apprendre à discerner les "références" que Python utilise partout (des sortes de "pointeurs"), et les concepts d'immutabilité et de passage-par-copie/référence.
> Avec tous ces savoirs, vous pourrez prédire le comportement des mocks, et réussir à les utiliser sereinement.
> Vous confronterez alors cette compréhension à des exercices concrets de comment appliquer des mocks.
> Enfin, vous aurez des conseils d'outils à utiliser pour tirer un maximum de vos mocks, mais surtout de quand ne pas les utiliser.
