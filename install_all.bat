@echo off
set NLM=^


set NL=^^^%NLM%%NLM%^%NLM%%NLM%
echo Installing Required Libraries ...
pip install -r requirements.txt
echo done.%NL%

set inputForDistanceCalculation=
set inputForProductionCost=
set outputForProductionCost=

echo Computing Arcs and Distances ...
set /p inputForDistanceCalculation="(optional) Enter input file (press enter to skip): "

if NOT "%inputForDistanceCalculation%" == "" (
    python distanceCalculation.py %inputForDistanceCalculation%
) else (
    python distanceCalculation.py
)

echo done.%NL%

echo Production of the shortest path ...
set /p inputForProductionCost="(optional) Enter input file (press enter to skip): "
set /p outputForProductionCost="(optional) Enter output file (press enter to skip): "

if NOT "%inputForProductionCost%" == "" (
    if NOT "%outputForProductionCost%" == "" (
        python ProductionCost.py -in %inputForProductionCost% -out %outputForProductionCost%
    ) else (
        python ProductionCost.py -in %inputForProductionCost%
    )
) else if NOT "%outputForProductionCost%" == "" (
    python ProductionCost.py -out %outputForProductionCost%
) else (
    python ProductionCost.py
)

echo done.%NL%

echo Shortest Path is:

set /p Build=<%outputForProductionCost%
echo %Build%
