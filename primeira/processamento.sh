# grep $1 ./entrada.sh | sort -r > saida.sh

grep $1 ./entrada.sh > intermediario.sh

cat intermediario.sh | sort > saida.sh

data=`date +%d/%m/%y`
bufferdata="data do script $data e usuario $USER"

echo $bufferdata >> saida.sh
