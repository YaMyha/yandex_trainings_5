p, v = map(int, input().split())
q, m = map(int, input().split())

distance_between = abs(p-q)
if v+m < distance_between:
    print(2*(v+m+1))
else:
    left_tree, right_tree = min(p-v, q-m), max(p+v, q+m)
    print(abs(left_tree-right_tree)+1)
