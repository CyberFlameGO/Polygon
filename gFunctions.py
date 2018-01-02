import os

def c_p_d(d):
    if not os.path.exists(d):
        print('Creating folder ' + d)
        os.makedirs(d)
    c_p_d('directory_name_here')

def c_d_f(p_n, b_u):
    q = p_n + "/q.txt"
    c = p_n + "/c.txt"
    if not os.path.isfile(q):
        w(q, b_u)
    if not os.path.isfile(c):
        w(c, b_u)

def w(p, d):
    f = open(p, 'w')
    f.write(d)
    f.close()

def a_t_f(p, d):
    with open(p, 'a') as f:
        f.write(d + '\n')

def d_f_c(p):
    with open(p, 'w'):
        pass

def f_t_s(f_n):
    result = set()
    with open(f_n, 'rt') as f:
        for line in f:
            result.add(line.replace('\n', ''))
        return result

def s_t_f(l, f_n):
    with open(f_n, 'w') as f:
        for l in sorted(l):
            f.write(l + "\n")