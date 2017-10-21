import numpy as np
import subprocess

# Path of igraph
# IGRAPH_INCLUDE='/usr/local/Cellar/igraph/0.7.1/include/igraph'#/usr/local/include/igraph
# IGRAPH_LIB='/usr/local/Cellar/igraph/0.7.1/lib'#/usr/local/lib
count=0;
node=10000; # number of nodes
edge=20000; # number of edges
numsteps=10000; # number of steps to take
dt=20; # save results every dt steps
degree=4;
smallworld=0.1 # rewiring probability in the Watts-Strogatz network
g=2; # number of opinions
U0=1.0/g*np.ones(g,); # list of initial densities
U0[-1]=1-sum(U0[:-1]);
for realization in [1]:
    for mode in [1]: # 1-rewire to random. 2-rewire to same.
        for gamma in [0]:
            for alpha in [0.1,0.2,0.3,0.4,0.5]:
                for u in range(10,91,20):
                    U0[0]=u*1.0/100; 
                    U0[1]=1.0-U0[0];
                    print U0 
                    cmd='./DynamicVoter -n {} -m {} -a {} -r {} -g {} -t {} -T {} -u {}'.format(node,edge,alpha,mode,gamma,dt,numsteps,g);
                    for i in xrange(g):
                        cmd=cmd+' '+str(U0[i]);
                    print cmd
                    subprocess.call(cmd, shell=True);
                    count=count+1;

print str(count)+' files submitted.';
print 'Mission Complete!';
