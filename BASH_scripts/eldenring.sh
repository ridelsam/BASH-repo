
echo
"You Died"
#!/bin/bash

echo "You Died"


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







