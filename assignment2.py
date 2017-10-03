def periodicSequence(s0, a, b, m):
    s=[]
    s.append(s0)
    for i in range(1,100):
        s.append((a * s[i - 1] + b) % m)
    
    count=0
    d = {i:s.count(i) for i in s}
    # for i in d:
    #     if d[i]==max(d.values()): count+=1
            
    # this works
    for j in d:
        if d[j]>1: count+=1
    return count






'''

A periodic sequence s is defined as follows:

s[0], a, b and m are all given positive integers;
s[i] for i > 0 is equal to (a * s[i - 1] + b) mod m.
Find the period of s, i.e. the smallest integer T such that for each i > k (for some integer k): s[i] = s[i + T].

Example

For s0 = 11, a = 2, b = 6 and m = 12, the output should be
periodicSequence(s0, a, b, m) = 2.

The sequence would look like this: 11, 4, 2, 10, 2, 10, 2, 10, 2, 10....

For s0 = 1, a = 2, b = 3 and m = 5, the output should be
periodicSequence(s0, a, b, m) = 4.

The sequence would look like this: 1, 0, 3, 4, 1, 0, 3, 4, 1, 0, 3, 4....

Input/Output

[time limit] 4000ms (py)
[input] integer s0

a positive integer representing s[0].

Guaranteed constraints:
1 ≤ s0 ≤ 100,
s0 < m.

[input] integer a

Guaranteed constraints:
2 ≤ a ≤ 100.

[input] integer b

Guaranteed constraints:
2 ≤ b ≤ 100.

[input] integer m

Guaranteed constraints:
5 ≤ m ≤ 100.

[output] integer

The sequence period.

'''
