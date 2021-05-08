;; The Catalan numbers is a sequence which satisfies the recurrence relation:
;; C(0) = 1
;; C(n+1) = ∑ i=0 to n: C(i) * C(n-i), n >= 0


;; Example for the 7th Catalan number:

;;   0  1  2  3   4   5   6    7
;;  [1, 1, 2, 5, 14, 42, 132,  X]  C(7):

;;   a        *           A    +
;;      b     *       B        +
;;         c  *   C            +
;;           d*D               +
;;         E  *   e            +
;;      F     *       f        +
;;   G        *           g

;; Notice that there is a repetition which has not
;; been taken into acccount in the following program.

(define (catalan n)

  (define (augment ls)
    (cons
     (foldl + 0
            (map (lambda (x y) (* x y))
                 ls
                 (reverse ls)))
     ls))

  (define (loop n ls)
    (if (<= n 0)
        (reverse ls)
        (loop (- n 1) (augment ls))))

  (loop n '(1)))

(catalan 25)

'(1
  1
  2
  5
  14
  42
  132
  429
  1430
  4862
  16796
  58786
  208012
  742900
  2674440
  9694845
  35357670
  129644790
  477638700
  1767263190
  6564120420
  24466267020
  91482563640
  343059613650
  1289904147324
  4861946401452)

;; =====================================
;; compact form just for silly enjoyment

(define (catalan n)
  (define (augment ls)
    (cons (foldl + 0 (map (lambda (x y) (* x y)) ls (reverse ls))) ls))
  (define (loop n ls)
    (if (<= n 0)
        (reverse ls)
        (loop (- n 1) (augment ls))))
  (loop n '(1)))
