#!/bin/bash

echo "Installing Required Libraries ..."
pip install -r requirements.txt
printf "done.\n"

inputForDistanceCalculation=""
inputForProductionCost=""
outputForProductionCost=""

echo "Computing Arcs and Distances ..."
read -p "(optional) Enter input file (press enter to skip): " inputForDistanceCalculation

if [ "$inputForDistanceCalculation" != "" ]
then
    python distanceCalculation.py %inputForDistanceCalculation%
else
    python distanceCalculation.py
fi

printf "done.\n"

echo Production of the shortest path ...
read -p "(optional) Enter input file (press enter to skip): " inputForProductionCost
read -p "(optional) Enter output file (press enter to skip): " outputForProductionCost

if [ "$inputForProductionCost" != "" ]
then
    if [ "$outputForProductionCost" != "" ]
    then
        python ProductionCost.py -in %inputForProductionCost% -out %outputForProductionCost%
    else
        python ProductionCost.py -in %inputForProductionCost%
    fi
elif [ "$outputForProductionCost" != "" ]
  then
    python ProductionCost.py -out %outputForProductionCost%
else
    python ProductionCost.py
fi

printf "done.\n"
echo "Shortest Path is:"

cat Resultat.txt