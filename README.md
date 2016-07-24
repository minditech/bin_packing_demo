# Bin packing example

This example is made to help get started with [Docker](http://docker.com), [Mindi](http://mindi.io), and optimization (in particular [bin packing](https://en.wikipedia.org/wiki/Bin_packing_problem)).

The included python script simply takes a list of numbers, splits it into 12 lists and prints them to screen with label 'b'.

    bash:~$ python demo.py sample_numbers.txt
    b 0.0304437038691 0.0550591177055 0.10692602761 0.0698771592269 0.0521772518303 0.0791941296578 0.0394415410649 0.154128246055 0.0215590419223 0.000334376636143 0.0302126958387 0.134037727702
    b 0.0352142985773 0.1396457691 0.0600325573749 0.0887641645095 0.130337188323 0.058749202688 0.035236023438 0.106275073132 0.0747404335501 0.084700152514 0.000397351186534 0.141416690466
    ...

To use it on Mindi, you will first need to install Docker (see these [excellent instructions](https://docs.docker.com/engine/installation/)).

Next, run the following (be sure to replace the all caps keywords):

    docker login -u DOCKERHUB_USERNAME -p DOCKERHUB_PASSWORD
    docker build -t DOCKERHUB_USERNAME/SOLVER_NAME:SOLVER_VERSION .
    docker push DOCKERHUB_USERNAME/SOLVER_NAME:SOLVER_VERSION

Finally, log into Mindi and submit the container URL under the bin packing challenge.

The script will be evaluated based on difference between the maximum sum and minimum sum of the lists. The lower the score the better!
