read name
stri=$'\n'
if [[ -z $name || $name -eq stri ]]
then
  echo "empty"
  echo "${name}"
else
  echo "not empty"
  echo "${name}"
fi
