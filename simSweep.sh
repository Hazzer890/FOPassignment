#!/bin/bash

exp_dir=Simulation_Saves`date "+%Y-%m-%d_%H.%M.%S"`

mkdir $exp_dir

cp Animal.py $exp_dir
cp AnimalClasses.py $exp_dir
cp SimulationBase.py $exp_dir
cp Main.py $exp_dir
cp simSweep.sh $exp_dir
cd $exp_dir
limit=$1
numWom=$2
numWomM=$3
numEmu=$4
numEmuM=$5
numPoss=$6
numPossM=$7
numKanga=$8
numKangaM=$9
numFoxes=$10
numFoxesM=$11
step=$12

for o in `seq $numWomM $step $numWom`;
do
    for i in `seq $numEmuM $step $numEmu`;
    do
        for u in `seq $numPossM $step $numPoss`
        do
            for y in `seq $numKangaM $step $numKanga`
            do
                for t in `seq $numFoxesM $step $numFoxes`
                do
                    echo "Experiment: " $p $o $i $u $y $t
                    python3 Main.py 10 $o $i $u $y $t
                done
            done
        done
    done
done
