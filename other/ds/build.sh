#!/bin/bash

# ds = data structures
project="$HOME/code/java/ds"
build="$project/target"

cd "$project" || exit 1

[[ -d "$build" ]] && rm -r "$build"

javac -d "$build" \
      tree/BinaryTree.java \
      tree/BalancedTree.java \
      tree/BST.java \
      DS.java

java -cp "$build" DS

