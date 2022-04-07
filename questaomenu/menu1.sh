echo "Escolha uma das opções referentes ao Brasil:"
echo " (1) Língua"
echo " (2) Moeda"
echo " (3) Capital"
echo " (4) Continente"

read entrada

case $entrada in
	1) echo "A lingua oficial do Brasil é Português";;
	2) echo "A moeda do Brasil é o Real"
		;;
	3) echo "A capital do Brasil é Brasília";;
	4) echo "O Brasil está na América"
	   echo "Na América do Sul";;
	*) echo "Opção inválida!"
	esac
