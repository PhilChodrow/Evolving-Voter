# C++ parameters
CC = g++
CFlags = -O3 -Wall -o

# needed for bin
voter_files = main.cpp Dynamic_Voter.cpp Node.cpp Edge.cpp Random1.cpp 

# directories and file paths
DATA_DIR = data
BIN_DIR = bin
bin_loc = bin/DynamicVoter

# run simulation
data: $(bin_loc) run.py
	if [ ! -d "$(DATA_DIR)" ]; then \
	  mkdir $(DATA_DIR);           \
	fi
	python run.py

# compile bin
$(bin_loc): $(voter_files)
	if [ ! -d "$(BIN_DIR)" ]; then \
	  mkdir $(BIN_DIR);            \
	fi
	$(CC) $(voter_files) $(CFlags) $(bin_loc)

all: $(bin_loc) data

clean: 
	rm -rf bin
	rm -rf data