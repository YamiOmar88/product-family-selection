# Product Family Selection

## Introduction

The present code allows the user to determine a product family, as defined in Value Stream Mapping (VSM). Different products may well follow different paths though the production line and trying to study all of them simultaneously produces little to no insights about the manufacturing process. Therefore, equivalently to product family selection in terms of VSM, a product family must be determined using the principle of similarity. According to this principle, products with similar process sequences are grouped into the same family. In other words, “a product family (...) includes all products which are produced in similar production steps and on mostly identical machines”. (See K. Erlach, *Value Stream Design - The Way Towards a Lean Factory*. Springer, 2013)


## Similarity Metric: Jaccard

Given that the path a manufactured item takes through a manufacturing network can be abstracted as a set of workstations, the Jaccard similarity of sets seems appropriate. This similarity measure is defined as follows:

**Definition:** Given two sets S and T, the Jaccard similarity J(S; T) is the ratio of the size of the intersection of S and T to the size of their union.


## Available code

The following modules are available:
* `fileread.py` allows to read the data from .txt files.
* `pathsets.py` calculates the sets of paths (useful when there are multiple paths with the same workstations used in different order).
* `family.py` can be used for product family search.

In addition, an example of code used is available in `main.py`.
