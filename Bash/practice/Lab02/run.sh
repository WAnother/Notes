#! /bin/bash
cd c-files
for File in *.c
do
	fn=$(echo $File | cut -f 1 -d '.')
	if  gcc -Wall -Werror $File 2>/dev/null ; then
		echo "Compiling file $File... Compilation succeeded."
		exec 3> ${fn}.out
		cat a.out >&3
	else
		echo "Compiling file $File... Compilation failed."
	fi
done
exit 0