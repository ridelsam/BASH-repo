#!/bin/bash


name=$1
compliment=$2

user=$(whoami)
date=$(date)
whereami=$(pwd)

echo "Good Morning $name!!"

sleep 1

echo "looking $compliment, $name"

sleep 1

echo "have a great day today, $name!"


echo "you are currently logged in as $user and you are in the directory $whereami. Today is $date"

