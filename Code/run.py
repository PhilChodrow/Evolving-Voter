import numpy as np
import subprocess
from itertools import product
import os

count=len(os.listdir('data'));
node=10000; # number of nodes
c = np.array([3, 4, 6, 8, 20]); # mean degree 

dt=5000; # save results every dt steps
alph = np.linspace(1.0, 0.0, 101) # rewiring probability
lam = 2.0**(-np.arange(3, 11))
g=2; # number of opinions
max_steps = 5*10**6
realizations = np.arange(0,1)

# U_naught = np.linspace(0, 1.0, 11)
U_naught = [.5]

U0=1.0/g*np.ones(g,); # list of initial densities
U0[-1]=1-sum(U0[:-1]);
mode = [0, 1]

pars = product(realizations, lam, c, mode, alph, U_naught)
for realization, lamb, cee, mode, alpha, U0 in pars:

    outfile = 'data/mode_' + str(mode) + '_run_' + str(count)
    edge = node*cee/2.0

    cmd='./bin/DynamicVoter -n {} -m {} -a {} -l {} -t {} -M {} -T {} -o {} -u {}  '.format(node, edge, alpha, lamb, dt, mode, max_steps, outfile, U0);
#    for i in xrange(g):
#        cmd=cmd
    print cmd
    subprocess.call(cmd, shell=True);
    count=count+1;

print str(count-1)+' files submitted.';
print 'Mission Complete!';