func ()
{
  if [[ $1 == 0 ]]
  then
    echo "$2"
    return
  fi

  a=`func $2 $1%$2`
  return a
}

read -p "two numbers: " $one $two
func one two
