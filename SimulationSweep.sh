#!/bin/bash

exp_dir=Simulation_Saves`date "+%Y-%m-%d_%H.%M.%S"`

mkdir $exp_dir

cd $exp_dir
limit=$1
numWom=$2
numEmu=$3
numPoss=$4
numKanga=$5
numFoxes=$6

for p in `seq $limit $numWom $numEmu $numPoss $numKanga $numFoxes`;
do
    echo "Experiment: " $p
        python3 Main.py $p  
done