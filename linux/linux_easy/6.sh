check_op1 ()
{
  case "$1" in
    "exit")
      echo "bye"
      exit 0
      ;;
    *)
      ;;
  esac
}


do_operation ()
{
  case "$2" in
    "+")
      let "res = $1 + $3"
      ;;
    "-")
      let "res = $1 - $3"
      ;;
    "*")
      let "res = $1 * $3"
      ;;
    "/")
      let "res = $1 / $3"
      ;;
    "%")
      let "res = $1 % $3"
      ;;
    "**")
      let "res = $1 ** $3"
      ;;
    *)
      echo "error"
      exit 0
      ;;
  esac

  echo "$res"
}

while true
do
  read -p "" op1 oper op2
  check_op1 $op1
  do_operation "${op1}" "${oper}" "${op2}"
done
