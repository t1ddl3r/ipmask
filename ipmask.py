import sys

def get_mask(nums):
    mask_ips = []
    for i in range(33):
        mask_ips.append(2 ** i)
    mask_ips.reverse()
    for i in mask_ips:
        if(nums >= i):
            return str(mask_ips.index(i))

def get_next_ip(ip, mask):
    _ = [255**3, 255**2, 255, 1]
    ips = 2 ** (32 - mask)
    for i, num in enumerate(_):
        if ips > num:
            ip = ip.split('.')
            ip[i] = str(int(ip[i]) + ips / num)
            return '.'.join(ip)

def ipr2ipm(start_ip, end_ip):
    _res = []
    while True:
        _s = map(eval, start_ip.split('.'))
        _e = map(eval, end_ip.split('.'))
        _num = (_e[3] + 1 - _s[3]) * (_e[2] + 1 - _s[2]) * (_e[1] + 1 - _s[1]) * (_e[0] + 1 - _s[0])
        if _num <= 0:
            break
        _mask = get_mask(_num)
        _res.append(start_ip + '/' + _mask)
        start_ip = get_next_ip(start_ip, int(_mask))
    return _res




if __name__ == '__main__':
    fname = sys.argv[1]
    with open(fname, 'r') as f:
        ls = f.readlines()
        for i in ls:
            results = []
            i = i.strip().split(' ')
            res = ipr2ipm(i[0], i[1])
            for r in res:
                open('ipm_' + fname, 'a+').write(r + '\n')

            
    
