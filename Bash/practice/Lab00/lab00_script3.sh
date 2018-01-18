#! /bin/bash
for ((counter=$1; counter >= 0; counter--))
do
	((counter%3 == 0)) && echo "$counter"
done
exit 0