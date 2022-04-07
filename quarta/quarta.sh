#ip=8.8.8.8

#echo `ping -q -c1 $ip | grep received | cut -d " " -f 4`

#select arq in `ls`
#do
#	cat $arq
#done

valor=1

while [ $valor -eq 1  ]
do
	echo "entrou no while"
	ping -c 1 8.8.8.8 >> saida.sh
	sleep 6
done
