MODULE LinkedList;
  IMPORT Out;

  CONST pwidth = 5;

  TYPE
    Node = POINTER TO NodeDesc;
    NodeDesc = RECORD
      key: INTEGER;
      next: Node
    END;

  VAR sentinel: Node;

  PROCEDURE populateList(VAR p: Node; n: INTEGER);
    VAR q: Node;
  BEGIN
    WHILE n > 0 DO
      NEW(q); q.next := p;
      p := q; q.key := n;
      DEC(n)
    END
  END populateList;

  PROCEDURE searchFor(n: INTEGER; VAR node: Node): BOOLEAN;
    VAR found: BOOLEAN;
  BEGIN found := FALSE;
    sentinel.key := n;
    WHILE node.key # n DO node := node.next END;
    IF node # sentinel THEN found := TRUE END;
    RETURN found
  END searchFor;

  PROCEDURE insertBefore(n, newval: INTEGER; VAR root: Node);
    VAR q, tmp: Node;
  BEGIN tmp := root;
    WHILE (tmp # NIL) & (tmp.key # n) DO tmp := tmp.next END;
    NEW(q); q^ := tmp^; tmp.key := newval; tmp.next := q
  END insertBefore;

  PROCEDURE insertAfter(n, newval: INTEGER; VAR root: Node);
    VAR q, tmp: Node;
  BEGIN tmp := root;
    WHILE (tmp # NIL) & (tmp.key # n) DO tmp := tmp.next END;
    NEW(q); q.key := newval; q.next := tmp.next; tmp.next := q
  END insertAfter;

  (* it must be assured that there exist no other variables pointing to the now deleted element *)
  PROCEDURE delete(n: INTEGER; VAR root: Node);
    VAR tmp: Node;
  BEGIN tmp := root;
    WHILE (tmp # NIL) & (tmp.key # n) DO tmp := tmp.next END;
    tmp^ := tmp.next^;
  END delete;

  PROCEDURE deleteAfter(n: INTEGER; VAR root: Node);
    VAR tmp, deletable: Node;
  BEGIN tmp := root;
    WHILE (tmp # NIL) & (tmp.key # n) DO tmp := tmp.next END;
    (* possible NPE here *)
    deletable := tmp.next;
    tmp.next := deletable.next;
    deletable.next := NIL;
  END deleteAfter;

  PROCEDURE printList(l: Node);
    VAR tmp: Node;
  BEGIN tmp := l;
    (* add nil check for safety? *)
    WHILE tmp # sentinel DO
      Out.Int(tmp.key, pwidth); Out.Ln;
      tmp := tmp.next
    END;
    Out.Ln
  END printList;

  (* tests *)
  PROCEDURE doIt;
    VAR root: Node;
  BEGIN
    NEW(sentinel); root := sentinel;
    populateList(root, 4);
    printList(root);

    insertBefore(4, 8, root);
    printList(root);

    delete(8, root);
    printList(root);

    insertAfter(2, 9, root);
    printList(root);

    deleteAfter(2,root);
    printList(root);
  END doIt;

BEGIN
  doIt;
END LinkedList.
