;; You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
;; If a string is longer than the other, append the additional letters onto the end of the merged string.

;; Return the merged string.

;; Example 1:
;; Input: word1 = "abc", word2 = "pqr"
;; Output: "apbqcr"
;; Explanation: The merged string will be merged as so:
;; word1:  a   b   c
;; word2:    p   q   r
;; merged: a p b q c r

;; Constraints:
;;     1 <= word1.length, word2.length <= 100
;;     word1 and word2 consist of lowercase English letters.

(define/contract (merge-alternately word1 word2)
  (-> string? string? string?)
  (cond [(string=? word1 "") word2]
        [(string=? word2 "") word1]
        [else (string-append
               (substring word1 0 1)
               (string-append
                (substring word2 0 1)
                (merge-alternately
                 (substring word1 1)
                 (substring word2 1))))]))
