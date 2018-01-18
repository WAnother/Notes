#! /bin/bash
(( $# != 2 )) && echo "Usage: sh lab01_gamestats.sh <file> <game>" && exit 1
[[ ! -e $1 ]] && echo "$1 does not exit" && exit 2
total_student=0
total_time=0
Highest_student=0;
Lowest_student=0;
Highest_student_name=0;
Lowest_student_name=0;
while IFS=, read f1 f2 f3
do
	if [[ "$f2" == "$2" ]]; then
		(( total_student++))
		(( total_time+=$f3))
		(( $f3 > $Highest_student )) && Highest_student_name=$f1 && Highest_student=$f3;
		(( $Lowest_student == 0 )) && Lowest_student_name=$f1 && Lowest_student=$f3
		(( $f3 < $Lowest_student )) && Lowest_student_name=$f1 && Lowest_student=$f3
	fi
done < $1
echo "Total Student: $total_student"
echo "Total hours spent in a day: $total_time"
echo "$Highest_student_name spent the highest amount of time in a day: $Highest_student"
echo "$Lowest_student_name spend the lowest amount of time in a day: $Lowest_student"
exit 0