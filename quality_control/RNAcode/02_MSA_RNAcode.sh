#!/bin/bash

# Multiple sequences alignment of each .fna family file.
# Run RNAcode

DIR="/home1/duanyq/GMSC/RNAcode_result/split"
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
                mafft --clustalout --auto ${DIR_second}/${infile} >RNAcode_result/msa/first${n}/second${m}/${infile}.aln
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
