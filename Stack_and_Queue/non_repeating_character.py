

def non_repeat_chr(array):
    res = []
    s = []
    for i in array:
        if i in s:
            res.append(-1)
        else:
            res.append(i)
        s.append(i)
    return res

#print(non_repeat_chr(["a", "a", "b", "c"]))

num = eval(input())

for i in range(0, int(num)):
    size = int(eval(input()))
    array = eval(input())
    array = [ x for x in array.strip().split(" ") ]
    res = non_repeat_chr(array)
    print((" ".join(map(str, res))))

"""
284
w l r b b m q b h c d a r z o w k k y h i d d q s c d x r j m o w f r x s j y b l d b e f s a r c b y n e c d y g g x x p k l o r e l l n m p a p q f w k h o p k m c o q h n w n k u e w h s q m g b b u q c l j j i v s w m d k q t b x i x m v t r r b l j p t n s n f w z q f j m a f a d r r w s o f s b c n u v q h f f b s a q x w p q c a c e h c h z v f r k m l n o z j k p q p x r j x k i t z y x a c b h h k i c q c o e n d t o m f g d w d w f c g p x i q v k u y t d l c g d e w h t a c i o h o r d t q k v w c s g s p q o q m s b o a g u w n n y q x n z l g d g w

Its Correct output is:
w w w w w w w w w w w w w w w l l l l l l l l l l l l l l l l l l l l l l l l l a a a a a a z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z z -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

And Your Code's output is:
w l r b -1 m q -1 h c d a -1 z o -1 k -1 y -1 i -1 -...
"""