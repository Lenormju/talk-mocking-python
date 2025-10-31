<!-- .slide: data-background-image="./sgalagaev--5iSCtrJX5o-unsplash.jpg" -->

# Dompter les mocks !

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

Notes:
* objectif 5-6 minutes max, pour laisser du temps pour la démo, et pour la conclusion
* n'hésitez pas à poser vos questions tout du long, je verrai si j'ai le temps ou pas

-v-

## Pourquoi parler des mocks ?

* sujet un peu has been ?
* outil pratique !
* mais difficile à utiliser ...

Notes:
* mon histoire avec les mocks, le tuto que j'aurais voulu avoir en 2018

-v-

## Sondage

1. qui ne connaît pas du tout et veut découvrir ?
2. qui a déjà eu du mal à les utiliser et veut s'améliorer ?
3. qui maîtrise déjà et va un peu s'ennuyer ?

-v-

## Objectif

* Comprendre ce qu'est un mock
* Connaître les problèmes qu'il résout
  * et qu'il cause (!)
* Savoir les appliquer
  * sans trop galérer
  * et donc savoir les débugger !

---

# Un petit peu de théorie

TODO: image

-v-

## C'est quoi ?

TODO

Notes:
* à quoi ça ressemble :
  * unittest.mock.Mock, récursif
  * ses variantes : Magic, NonCallable, Property, Async, Threading (3.13 !)

-v-

## Des métamorphes !

TODO

![](./Metamorph-RFVF.png)

-v-

## A quoi ça sert ?

TODO

* à tester
  * c'est important de tester !
* "améliorer" des tests
  * FIRST : Fast, Independant, Repeatable, Self-sufficient, Timely
* "collaboration testing" : tester le "how"
* rendre testable du code qui ne l'est pas tellement / pas du tout

Notes:
* code récalcitrant ("ennemis") : side-effects ("spooky action at a distance", "que fait cette méthode ?"), (global/static) state, IO, singletons, time, locale, network, files, env, GPU, unclear pre/post-conditions, non-determinism, (G)UI vs API, concurrency et threading, random (non-deterministic), complex outputs and high dimensionality
  * API payante
  * API lente
  * API instable
  * l'API n'existe pas encore
  * exception ou rareté
* besoin de "tricher" un peu
* pied de biche versus scalpel chirurgical

-v-

Quelques exemples de ce qui rend difficile de tester :

* le code intéragit avec une API payante
* ou l'API est très lente
* ou l'API est instable
* ou l'API n'existe même pas encore !

Solution : tricher, modifier le programme

-v-

## Des doublures

TODO

![](./acteurs-et-doublures-11.png)

Notes:
* différentes formes de doublures (cf https://martinfowler.com/articles/mocksArentStubs.html) "point vocabulaire"
  * dummy : unused, passed around
  * stub : canned answers
  * spy : stub + recording
  * fake : alternative implementation
  * mock : pre-programmed expectations
  * en Python : une seule classe pour tout faire, donc on utilise le même terme pour tout, et peuvent être tout sauf des mocks

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

* les mocks c'est bien : isolation, perf, économies, ...
* les mocks c'est mal : isolation, fragilité, complexité, ...
* repenser l'architecture et la stratégie de test :
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
* [Martin Fowler - Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)
* [Hynek Schlawack - “Don’t Mock What You Don’t Own” in 5 Minutes](https://hynek.me/articles/what-to-mock-in-5-mins/)
* Conférence "l'enfer des tests autos", bientôt en replay
* [Tout comprendre des mocks Python](https://kaizen-solutions.net/kaizen-insights/articles-et-conseils-de-nos-experts/tout-comprendre-des-mocks-python/)
* [Brett Schuchert et Tim Ottinger - tests "FIRST"](https://agileinaflash.blogspot.com/2009/02/first.html)

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
5. Comment mesurer la fiabilité des tests ? Et leur maintenabilité ?
6. Définition de "test unitaire"

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
