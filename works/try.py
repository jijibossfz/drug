# coding=utf-8
from extra_apps.utils.email_send import email_status

# email_status('961445782@qq.com','/home/jianping/pywork/try27/drug/.pdb.pdbqt')
with open('/home/jianping/pywork/try27/drug/media/dock2/fz/1737/canji', 'r') as f:
    lines2 = f.readlines()
resn_lst = [n.rstrip() for n in lines2 if len(n) > 1]

x, y, z = [], [], []
for n in resn_lst:
    x.append(float(n[30:38]))
    y.append(float(n[38:46]))
    z.append(float(n[46:54]))

center_x = float('%.3f' % (sum(x) / len(x)))
center_y = float('%.3f' % (sum(y) / len(y)))
center_z = float('%.3f' % (sum(z) / len(z)))
size_x = max(x) - min(x)
size_y = max(y) - min(y)
size_z = max(z) - min(z)
print center_x,center_y,center_z