#! /bin/bash
(( $# != 1 )) && echo "Usage: sort_logs.bash <input file>" && exit 1
[[ ! -r $1 ]] && echo "Error: $1 is not a readable file." && exit 2

if [[ -e $1.unsorted ]]; then
	remove=$(rm -f $1.unsorted)
	if (( remove )); then
		echo "Error: Could not remove $1.unsorted."
	else
		echo "Note: Removing existing file $1.unsorted."
	fi
fi
if [[ -e $1.sorted ]]; then
	remove2=$(rm -f $1.sorted)
	if ((remove2)); then
		echo "Error: Could not remove $1.sorted."
	else
		echo "Note: Removing existing file $1.sorted."
	fi
fi
exec 5< $1
exec 6> $1.unsorted
line=0
while read -a Data <&5
do
	length=${#Data[*]}
	if (( line == 0 )); then
		name=(${Data[*]})
	else
		for (( i=1; i<length; i++))
		do
			echo "${name[$i]},${Data[0]},${Data[$i]}" >&6
		done
	fi
	line=1
done

exec 7< $1.unsorted
exec 8> $1.sorted
temp=($(
	while read -a Data <&7
	do
		echo "${Data[*]}"
	done | sort -n -t "," -k 3r -k 1))
for (( i=0; i<${#temp[*]}; i++))
do
	echo "${temp[$i]}" >&8
done


exec 3< $1
exec 4> $1.out
line=0
while read -a Data <&3
do
	length=${#Data[*]}
	((real=$length-1))
	if (( $line == 1)); then
		time_2=${Data[0]}
		total=0
		for (( i=1; i<length;i++))
		do
			((total+=${Data[i]}))
		done
		average=$(echo "scale=2; $total/$real" | bc)
		sorted=($(
			for(( i=1; i<length;i++))
			do
				echo "${Data[i]}"
			done | sort -n))
		((mid=real/2))
		medium=0
		(( mid%2 == 0)) && medium=$(echo "scale=2; (${sorted[mid]} + ${sorted[mid - 1]})/2" | bc)
		(( mid%2 == 1)) && medium=$(echo "scale=2; ${sorted[mid]}/1" | bc)
		 echo "Average temperature for time $time_2 was $average C." >&4
		 echo "Median temperature for time $time_2 was $medium C." >&4
		 echo "" >&4
	fi
	line=1
done
for(( i=1; i<length; i++))
do
	total2=0
	sort_array=($(
		while read -a data
		do
			echo "${data[i]}"
		done <$1 | sort -n))
	length2=${#sort_array[*]}
	for (( j=1; j<length2; j++))
	do
		((total2+=${sort_array[j]}))
	done
	((real2=$length2-1))
	((mid2=length2/2))
	average2=$(echo "scale=2; $total2/$real2" | bc)
	medium2=0
	(( mid2%2 == 0)) && medium2=$(echo "scale=2; (${sort_array[mid2]} + ${sort_array[mid2-1]})/2" | bc)
	(( mid2%2 == 1)) && medium2=$(echo "scale=2; ${sort_array[mid2]}/1" | bc)
	echo "Average temperature for ${sort_array[0]} was $average2 C." >&4
	echo "Median temperature for ${sort_array[0]} was $medium2 C." >&4
	echo "" >&4
done
exit 0