#!/bin/bash
while true
do
  echo 'enter your name:'
  read -r name
  if [[ -z $name ]]
    then
    echo 'bye'
    break
  fi

  if [[ $name == $'\x10' ]]
  then
  echo 'bye'
  break
  fi

  echo 'enter your age:'
  read -r age
  if [[ ${age} -eq 0 ]]
    then
    echo 'bye'
    break
  fi

  if [[ age -le 16 ]]
  then
  group='child'
  elif [[ age -gt 16 && age -le 25 ]]
  then
  group='youth'
  else
  group='adult'
  fi

  echo "${name}, your group is ${group}"
done
