
if [ $USER == "backupuser" ]
then
cp ./arquivos/* ./backup
echo 'Operação realizada com sucesso!'
else
echo 'Usuário sem permissão'
fi
