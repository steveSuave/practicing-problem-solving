package tree;

import java.util.NoSuchElementException;
import java.util.Queue;

/** Binary search tree */
public class BST<T extends Comparable<? super T>> extends BinaryTree<T> {

  public BST(T val) {
    super(val);
  }

  // Construct a BST from a queue of elements.
  public static <T extends Comparable<? super T>> BinaryTree<T> buildBST(
      Queue<T> sourceOfElements) {

    BinaryTree<T> bst = new BST<>(sourceOfElements.poll());
    while (sourceOfElements.size() > 0) {
      bst.insert(sourceOfElements.poll());
    }
    return bst;
  }

  @Override
  public void insert(T val) {
    if (val == null) throw new IllegalArgumentException("Cannot insert null value to BST");
    insert(val, this);
  }

  private BinaryTree<T> insert(T val, BinaryTree<T> tree) {
    if (tree == null) return new BST<T>(val);
    int comparison = val.compareTo(tree.getKey());
    if (comparison < 0) tree.setLeft(insert(val, tree.getLeft()));
    else if (comparison > 0) tree.setRight(insert(val, tree.getRight()));
    return tree;
  }

  @Override
  public void remove(T val) {
    if (val == null) throw new IllegalArgumentException("Cannot delete the null value from BST");
    remove(val, this);
  }

  private BinaryTree<T> remove(T val, BinaryTree<T> tree) {
    if (tree == null) throw new NoSuchElementException("Value not found in BST");
    int comparison = val.compareTo(tree.getKey());
    if (comparison < 0) tree.setLeft(remove(val, tree.getLeft()));
    else if (comparison > 0) tree.setRight(remove(val, tree.getRight()));
    else { // found node with val
      if (tree.getLeft() == null) return tree.getRight();
      else if (tree.getRight() == null) return tree.getLeft();
      else {
        BinaryTree<T> oldNode = tree;
        // leftmost node of the right branch
        tree = min(oldNode.getRight());
        // StackOverflowError if the following two setters switch order
        // because deleteMin needs the original left branch
        // evaluate the example tree with remove(6) to see this
        tree.setRight(deleteMin(oldNode.getRight()));
        tree.setLeft(oldNode.getLeft());
      }
    }
    return tree;
  }

  /*
                      4
          ┌───────────┴───────────┐
          1                       6
          └─────┐           ┌─────┴─────┐
                3           5           7
             ┌──┘
             2
  */

  private BinaryTree<T> min(BinaryTree<T> tree) {
    if (tree.getLeft() == null) return tree;
    else return min(tree.getLeft());
  }

  private BinaryTree<T> deleteMin(BinaryTree<T> tree) {
    if (tree.getLeft() == null) return tree.getRight();
    tree.setLeft(deleteMin(tree.getLeft()));
    return tree;
  }
}
