;; A binary tree is univalued if every node in the tree has the same value.
;; Return true if and only if the given tree is univalued.

; Definition for a binary tree node.

#|
; val : integer?
; left : (or/c tree-node? #f)
; right : (or/c tree-node? #f)
(struct tree-node
  (val left right) #:mutable #:transparent)

; constructor
(define (make-tree-node [val 0])
  (tree-node val #f #f))
|#

(define/contract (is-unival-tree root)
  (-> (or/c tree-node? #f) boolean?)

  (define (check-val root val)
    (cond [(not root) #t]
          [(not (= (tree-node-val root) val)) #f]
          [else (and (check-val (tree-node-left root) val)
                     (check-val (tree-node-right root) val))]))

  (check-val root (tree-node-val root)))
