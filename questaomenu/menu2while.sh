### Calculadora com while ###

entrada=0
while [ $entrada -ne 5 ]
do

    echo " 1) Soma"
    echo " 2) Subtracao"
    echo " 3) Multiplicação"
    echo " 4) Divisão"
    echo " 5) Sair"
    echo -n "Escolha uma das operações matemáticas: "

    read entrada

    case $entrada in
        1) echo -n "Digite o primeiro numero: "
	   read numero1
	   echo -n "Digite o segundo número: "
	   read numero2
	   echo "O valor da soma é $(( $numero1+$numero2 ))"
	   echo
	   ;;
	2) echo -n "Digite o minuendo: "
	   read sub1
	   echo -n "Digite o subtraendo: "
	   read sub2
	   echo "O valor da subtração é $(( $sub1-$sub2 ))"
	   echo
	   ;;
	3) echo -n "Digite o primeiro fator: "
	   read mult1
	   echo -n "Digite o segundo multiplicando: "
	   read mult2
	   echo "O resultado da multiplicação é $(( $mult1*$mult2 ))"
	   echo
	   ;;
	4) echo -n "Digite o dividendo: "
	   read div1
	   echo -n "Digite o divisor: "
	   read div2
	   echo "O resultado da divisao é $(( $div1/$div2 ))"
	   echo
	   ;;
	5) echo "Programa será encerrado";;
	*) echo "Opção inválida!";;
    esac
done

echo "Programa encerrado com sucesso"
