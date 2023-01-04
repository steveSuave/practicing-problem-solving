package tree;

public abstract class BinaryTree<T extends Comparable<? super T>> {

  private T key;
  private BinaryTree<T> left, right;

  public BinaryTree() {}

  public BinaryTree(T key) {
    this.key = key;
  }

  public abstract void insert(T val);

  public abstract void remove(T val);

  public void preOrderTraversal() {
    System.out.printf("%s ", key);
    if (left != null) left.preOrderTraversal();
    if (right != null) right.preOrderTraversal();
  }

  public void inOrderTraversal() {
    if (left != null) left.inOrderTraversal();
    System.out.printf("%s ", key);
    if (right != null) right.inOrderTraversal();
  }

  public void postOrderTraversal() {
    if (left != null) left.postOrderTraversal();
    if (right != null) right.postOrderTraversal();
    System.out.printf("%s ", key);
  }

  public void printTree() {
    printTree(0);
  }

  // Like inOrderTraversal but with some whitespace manipulation
  // h is the initial amount of indentation
  private void printTree(int h) {
    if (right != null) right.printTree(h + 1);
    for (int i = 0; i < h; i++) System.out.print("\t");
    System.out.println(key);
    if (left != null) left.printTree(h + 1);
  }

  // Like preorder traversal but with added parentheses to indicate branch relations
  public String lispify() {
    return new StringBuilder("(")
        .append(key)
        .append(left == null ? "" : left.lispify())
        .append(right == null ? "" : right.lispify())
        .append(")")
        .toString();
  }

  public T getKey() {
    return this.key;
  }

  public void setKey(T key) {
    this.key = key;
  }

  public BinaryTree<T> getLeft() {
    return this.left;
  }

  public void setLeft(BinaryTree<T> left) {
    this.left = left;
  }

  public BinaryTree<T> getRight() {
    return this.right;
  }

  public void setRight(BinaryTree<T> right) {
    this.right = right;
  }
}
