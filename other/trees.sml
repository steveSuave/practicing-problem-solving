datatype 'a tree = Empty | Leaf of 'a | Node of 'a * 'a tree list;

val atree = Node(1, [Leaf(2), Node(3, [Leaf(4), Leaf(5)])]);

fun treemap(f, Empty) = Empty
  | treemap(f, Leaf(x)) = Leaf(f(x))
  | treemap(f, Node(x, l)) = Node(f(x), map (fn v => treemap(f, v)) l);

treemap(fn x => x+1, atree);

fun flat(Empty) = []
  | flat(Leaf(x)) = [x]
  | flat(Node(x, l)) = x::List.concat(map (fn t=>flat(t)) l);

flat(atree);

