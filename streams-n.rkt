(define pentagonal
  (stream-cons 1
    (add-streams pentagonal
                 (add-streams (scale-stream 3 integers) ones))))
