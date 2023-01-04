package tree;

import java.util.Queue;

/**
 * A tree is perfectly balanced, if for each node the numbers of nodes in its left and right
 * subtrees differ by at most 1
 */
public class BalancedTree<T extends Comparable<? super T>> extends BinaryTree<T> {

  // Construct a perfectly balanced BinaryTree from a queue of elements.
  public static <T extends Comparable<? super T>> BinaryTree<T> buildBalancedTree(
      Queue<T> sourceOfElements) {
    return buildBalancedTree(sourceOfElements.size(), sourceOfElements);
  }

  private static <T extends Comparable<? super T>> BinaryTree<T> buildBalancedTree(
      int numOfChildren, Queue<T> sourceOfElements) {

    if (numOfChildren == 0) return null;
    BinaryTree<T> newBT = new BalancedTree<T>();
    newBT.setKey(sourceOfElements.poll());
    int numOfLeftNodes = numOfChildren / 2;
    int numOfRightNodes = numOfChildren - numOfLeftNodes - 1;
    newBT.setLeft(buildBalancedTree(numOfLeftNodes, sourceOfElements));
    newBT.setRight(buildBalancedTree(numOfRightNodes, sourceOfElements));
    return newBT;
  }

  @Override
  public void insert(T val) {
    // TODO
  }

  @Override
  public void remove(T val) {
    // TODO
  }
}
