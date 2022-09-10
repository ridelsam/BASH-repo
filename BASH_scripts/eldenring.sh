#!/bin/bash

echo "You Died"

echo "Welcome tarnished. Please choose your starting class
1 - Samurai
2 - Prisoner
3 - Prophet

read class

case $class in 

	1)
		type="Samurai"
		hp=10
		attack=20
		;;
	2)
		type="Prisoner"
		hp=20
		attack=4;
		;;
	3)
		type="Prophet"
		hp=30
		attack=4
		;;
esac

echo "you have chosen the $type class. Your HP is $hp and your attack is $attack."



#first beast battle

beast=$(( $RANDOM % 2 ))

echo "Your first beast approaches. Prepare to battle. Pick a number between 0-1. (0/1)"

read tarnished

if [[ $beast == $tarnished || $tarnished == "cheatcode" ]]; then
	echo "Beast VANQUISHED!! Congrats fellow tranished"
else
	echo "You died!"
	exit 1
fi


sleep 2

echo "Boss battle. Get scraed. It's  Margit. Pick a number between 0-9. (0-9)"

read tarnished

beast=$(( $RANDOM % 10 ))

if [[ $beast == $tarnished || $tarnished == "cheatcode" ]]; then
	echo "beast vanquished"
elif [[ $USER == "bernard" ]]; then
	echo "Hey, bernard always wins. You vanquished the beast."
else
	echo "You Died"
fi







