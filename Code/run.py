import numpy as np
import subprocess
from itertools import product

count=1;
node=2000; # number of nodes
c = np.arange(3, 20); # mean degree 
dt=100; # save results every dt steps
alph = [0.4] # rewiring probability
lam = 2.0**(-np.arange(3, 11)) # mutation rate
g=2; # number of opinions
max_steps = 100000
realizations = np.arange(0,2)

U0=1.0/g*np.ones(g,); # list of initial densities
U0[-1]=1-sum(U0[:-1]);
mode = [1]

pars = product(realizations, mode, alph, lam, c)
for realization, mode, alpha, lamb, cee in pars:

    outfile = 'data/test_' + str(count)
    edge = node*cee/2.0

    cmd='./bin/DynamicVoter -n {} -m {} -a {} -l {} -t {} -T {} -o {} -u {} '.format(node,edge,alpha,lamb, dt, max_steps, outfile, g);
    for i in xrange(g):
        cmd=cmd+' '+str(U0[i]);
    print cmd
    subprocess.call(cmd, shell=True);
    count=count+1;

print str(count-1)+' files submitted.';
print 'Mission Complete!';
