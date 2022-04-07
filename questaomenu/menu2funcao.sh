### Calculadora com função ###

## Somar ##
somar ()
{
	echo -n "Digite o primeiro número: "
	read num1
	echo -n "Digite o segundo número: "
	read num2
	echo "O valor da soma é $(( $num1+$num2 ))"
	echo
}

## Subtração ##
subtrair ()
{
	echo -n "Digite o minuendo: "
	read num1
	echo -n "Digite o subtraendo: "
	read num2
	echo "O valor da subtração é $(( $num1-$num2 ))"
	echo
}

## Multiplicação ##
multiplicar ()
{
	echo -n "Digite o primeiro fator: "
	read num1
	echo -n "Digite o segundo multiplicando: "
	read num2
	echo "O resultado da multiplicação é $(( $num1*$num2 ))"
	echo
}

## Divisão ##
dividir ()
{
	echo -n "Digite o dividendo: "
	read dividendo
	echo -n "Digite o divisor: "
	read divisor
	echo "O resultado da divisão $(( $dividendo/$divisor ))"
	echo
}

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
        1) somar;;
	2) subtrair;;
	3) multiplicar;;
	4) dividir;;
	5) echo "Programa será encerrado"
	   sleep 2;;
	*) echo "Opção inválida!";;
    esac
done

echo "Programa encerrado com sucesso"
