#! /bin/bash
while true
do
	read -p "Enter a command: " input
	if [[ $input == "hello" ]];	then
		echo "Hello $USER"
	elif [[ $input == "whereami" ]]; then
		echo "$PWD"
	elif [[ $input == "quit" ]]; then
		echo "Goodbye"
		break
	elif [[ $input == "compile" ]]; then
		for File in *.c
		do
			if gcc -Wall -Werror ${File} -o ${File}.o; then
				echo "Compilation succeeded for: $File"
			else
				echo "Compilation failed for: $File"
			fi
		done
	else
		echo "unrecognized input"
	fi
	echo ""
done
exit 0
