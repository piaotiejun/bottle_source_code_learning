#!/usr/bin/python
#coding=utf8

import itertools

def xrange_double(start, end=None, inc=1.0):
    """类似xrange的生成器，生成浮点数
    :start: 开始的数
    :end: 结束的数
    :inc: 步长 默认为1.0
    """
    if not end:
        end = start + 0.0
        start = 0.0

    assert inc # inc 如果为0报错

    if (start <= end and inc < 0) or (start >= end and inc > 0):
        raise 'start/end/inc wrong'

    for i in itertools.count():
        next = start + i * inc
        if (inc > 0 and next >= end) or (inc < 0 and next <= end):
            break
        yield next

for i in xrange_double(1, 10):
    print(i)

Infinite iterators:
count([n]) --> n, n+1, n+2, ...
cycle(p) --> p0, p1, ... plast, p0, p1, ...
repeat(elem [,n]) --> elem, elem, elem, ... endlessly or up to n times

Iterators terminating on the shortest input sequence:
chain(p, q, ...) --> p0, p1, ... plast, q0, q1, ... 
compress(data, selectors) --> (d[0] if s[0]), (d[1] if s[1]), ...
dropwhile(pred, seq) --> seq[n], seq[n+1], starting when pred fails
groupby(iterable[, keyfunc]) --> sub-iterators grouped by value of keyfunc(v)
ifilter(pred, seq) --> elements of seq where pred(elem) is True
ifilterfalse(pred, seq) --> elements of seq where pred(elem) is False
islice(seq, [start,] stop [, step]) --> elements from
seq[start:stop:step]
imap(fun, p, q, ...) --> fun(p0, q0), fun(p1, q1), ...
starmap(fun, seq) --> fun(*seq[0]), fun(*seq[1]), ...
tee(it, n=2) --> (it1, it2 , ... itn) splits one iterator into n
takewhile(pred, seq) --> seq[0], seq[1], until pred fails
izip(p, q, ...) --> (p[0], q[0]), (p[1], q[1]), ... 
izip_longest(p, q, ...) --> (p[0], q[0]), (p[1], q[1]), ... 

Combinatoric generators:
product(p, q, ... [repeat=1]) --> cartesian product
permutations(p[, r])
combinations(p, r)
combinations_with_replacement(p, r)

