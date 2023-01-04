import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import tree.BST;
import tree.BalancedTree;
import tree.BinaryTree;

public class DS {

  public static void main(String[] args) {

    Queue<Integer> q =
        new LinkedList<>(
            Arrays.asList(
                8, 9, 11, 15, 19, 20, 21, 7, 3, 2, 1, 5, 6, 4, 13, 14, 10, 12, 17, 16, 18));

    BinaryTree<Integer> balancedTree = BalancedTree.buildBalancedTree(q);
    checkExpect(
        balancedTree.lispify(),
        "(8(9(11(15(19))(20(21)))(7(3(2))(1)))(5(6(4(13))(14(10)))(12(17(16))(18))))");

    BinaryTree<Integer> bst = BST.buildBST(new LinkedList<>(Arrays.asList(4, 1, 6, 3, 5, 7, 2)));
    checkExpect(bst.lispify(), "(4(1(3(2)))(6(5)(7)))");

    /*
                        4
            ┌───────────┴───────────┐
            1                       6
            └─────┐           ┌─────┴─────┐
                  3           5           7
               ┌──┘
               2
    */

    bst.remove(6);
    checkExpect(bst.lispify(), "(4(1(3(2)))(7(5)))");

    bst.remove(1);
    checkExpect(bst.lispify(), "(4(3(2))(7(5)))");

    bst.insert(1);
    checkExpect(bst.lispify(), "(4(3(2(1)))(7(5)))");

    bst.insert(6);
    checkExpect(bst.lispify(), "(4(3(2(1)))(7(5(6))))");

    bst.printTree();
    // bst.preOrderTraversal();
    // bst.inOrderTraversal();
    // bst.postOrderTraversal();

  }

  private static <T> void checkExpect(T got, T expected) {
    if (!got.equals(expected)) {
      System.out.println("Got: " + got);
      System.out.println("Expected: " + expected);
      System.out.println();
      // throw new IllegalStateException();
    }
  }
}
