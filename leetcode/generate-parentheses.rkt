;; Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

;; Example 1:
;; Input: n = 3
;; Output: ["((()))","(()())","(())()","()(())","()()()"]

;; Example 2:
;; Input: n = 1
;; Output: ["()"]

;; Constraints:
;;     1 <= n <= 8

(define/contract (generate-parenthesis n)
  (-> exact-integer? (listof string?))
  (local
      [(define (fn-for-lop accumulator ret)
         (if (empty? accumulator)
             ret
             (fn-for-par (first accumulator) (rest accumulator) ret)))
       (define (fn-for-par par accumulator ret)
         (cond [(or (> (first par) n)
                    (< (first par) (second par)))
                (fn-for-lop accumulator ret)]
               [(= (string-length (third par)) (* 2 n))
                (fn-for-lop accumulator (cons (third par) ret))]
               [else
                (fn-for-lop (append `((,(+ (first par) 1)
                                       ,(second par)
                                       ,(string-append (third par) "(")))
                                    `((,(first par)
                                       ,(+ (second par) 1)
                                       ,(string-append (third par) ")")))
                                    accumulator)
                            ret)]))]
    (fn-for-lop '((0 0 "")) '())))
