#!/bin/bash





echo "what is your name"

read name

echo "how old are you?"

read age

echo "hello $name, you are $age years old"


sleep 2
echo "Calculating"

echo "............."
sleep 1

echo "............."
sleep 1

echo "............."
sleep 1


getrich=$((( $RANDOM % 15 ) + $age ))

echo "$name, you will become a millionaire when you are $getrich years old"
