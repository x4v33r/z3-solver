(declare-fun b () Bool)
(declare-fun a () Bool)
(declare-fun l () Bool)
(declare-fun r () Bool)
(assert (= l (=> a b)))
(assert (= r (or (not a) b)))
(assert (distinct r l))
(check-sat)
(get-model)
