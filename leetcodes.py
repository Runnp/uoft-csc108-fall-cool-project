You
are
given
an
array
nums
of
distinct
positive
integers.You
need
to
sort
the
array in increasing
order
based
on
the
sum
of
the
digits
of
each
number.If
two
numbers
have
the
same
digit
sum, the
smaller
number
appears
first in the
sorted
order.

Return
the
minimum
number
of
swaps
required
to
rearrange
nums
into
this
sorted
order.

A
swap is defined as exchanging
the
values
at
two
distinct
positions in the
array.

Example
1:

Input: nums = [37, 100]

Output: 1

Explanation:

Compute
the
digit
sum
for each integer: [3 + 7 = 10, 1 + 0 + 0 = 1] → [10, 1]
Sort
the
integers
based
on
digit
sum: [100, 37].Swap
37
with 100 to obtain the sorted order.
Thus, the
minimum
number
of
swaps
required
to
rearrange
nums is 1.