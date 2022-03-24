primeirofor=0
if [ $1 -le 10 ]
then
	primeirofor=$1
else
	primeirofor=10
fi
	for i in $(seq 1 $primeirofor); do
		estrelas="*"
		for j in $(seq $i 9); do
		    estrelas="${estrelas}*"
		done
		echo "$estrelas"
	done	
	if [ $1 -ge 11 ]
	then
		menosdez=$(($1-10))
		estrelas="*"
		for i in $(seq 1 $menosdez); do
			estrelas="${estrelas}*"
			echo "$estrelas"
		done
	fi

# for i in $(seq 1 $1); do
#     echo counter: $i
# done
