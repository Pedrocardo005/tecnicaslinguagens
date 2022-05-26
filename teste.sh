somar ()
{
	resultado=$[$1+$2]
	return $resultado
}

echo -n "5 + 7 = "

somar 5 7
echo $?
