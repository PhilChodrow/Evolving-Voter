## What is in here?

This code implements a variation of the co-evolving voter model from
> Richard Durrett, James P. Gleeson, Alun L. Lloyd, Peter J. Mucha, Feng Shi, David Sivakoff, Joshua E. S. Socolar, and Chris Varghese; Graph fission in an evolving voter model; PNAS 2012 109 (10) 3682-3687

> F Shi, PJ Mucha, R Durrett; Multiopinion coevolving voter model with infinitely many phase transitions; Physical Review E 88 (6), 062818

The new model includes a mutation process in addition to the co-evolving voter model.

## How to compile it?

Any standard C++ compiler should work. To compile
```
g++ main.cpp Dynamic_Voter.cpp Node.cpp Edge.cpp Random1.cpp -O3 -Wall -o DynamicVoter
```

## How to run it?
If the code is compiled as above, it can be run as `./DynamicVoter` with the following flags:
```
-n number_of_nodes: default value 1000
-m number_of_edges: default value 2000
-u number_of_opinions initial_densities: initial_densities is a sequence of numbers separated by whitespace. There should be as many numbers as number_of_opinions with each number indicating the initial density of the corresponding opinion.
-a alpha: rewiring probability $\alpha$
-l lambda: mutation probability
-t dt: print simulation results every dt steps
-T max_steps: when to terminate the simulation. If -1, it will run until there is no discordant edges. Default value is -1.
-o output_filename: two output files will be generated with filenames as output_filename.summary and output_filename.process. Defaul value is evolving_voter. See below for details on these files.
```

## What is the ouput?
The program will generate two output files: evolving_voter.summary and evolving_voter.process (or any names specified as above).

evolving_voter.summary has the summary information for the simulation. It is a whitespace delimited text file with the following columns
```
nodes: number of nodes
edges: number of edges
alpha: rewiring probability
lambda: mutation probability
u0: number of 0-nodes in the end
u1: number of 1-nodes in the end
steps: how many steps are taken 
time: clock time for the simulation
```
evolving_voter.process saves system states at every step or every dt steps. It is a whitespace delimited text file with the following columns. 
``` 
step: how many step has taken so far
action: what is done in this step. 0 - adapt, 1 - rewire, 2 - mutate
N0: number of 0-nodes
N1: number of 1-nodes 
N00: number of 0-0 edges
N01 N11 N000 N001 N010 N011 N101 N111: see N00
```
