#!/bin/bash

#Run RNAcode

DIR="./msa"
number=1
for n in {1..287}
  do
    if [ $number == 1 ]
    then
      DIR_first="${DIR}/first${n}"
      for m in {1..300}
        do
          DIR_second="${DIR_first}/second${m}"
          if [ "$(ls -A $DIR_second)" ]
          then
            for infile in $(ls ${DIR_second})
              do
                RNAcode ${DIR_second}/${infile} --tabular --outfile ./rnacode/first${n}/second${m}/${infile}.tsv
              done
          else
            number=0
            break
          fi
        done
    else
      break
    fi
  done
