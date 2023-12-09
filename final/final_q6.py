'''
Given a sequence of elements x1, . . . , xn with a given (partial) order , we want to increasingly reorder the
sequence as xi1 , xi2 , . . . , xin , where xik  xik+1 for k ∈ {1, . . . , n − 1}. For simplicity sake, you can think that
we have a sequence consisting of numbers (say {17, 5, 8, 13, 3}) with the order given by ≤, thus the ordered
sequence will be {3, 5, 8, 13, 17} since 3 ≤ 5, 5 ≤ 8 and so on.
A simple sorting algorithm to reorder such a sequence follows the pseudo code
a ← given sequence
while a is not sorted do
    for i = 0, until i ≤ length(a) − 1 do
        if not a[i] ≤ a[i + 1] then
            swap a[i], a[i + 1]
        else
            continue
        end if
    end for
end while

You can deﬁne the sequence as a Python list a=[17,5,8,13,3], and the steps are described in Figure 4.
Write a Python program that accepts a sequence of numbers and orders them using your implementation of
the previous pseudo code.
'''