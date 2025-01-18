# Gru_Minion
A project for simulating process creation and management in an operating system using Python, demonstrating forking, process execution, and error handling. This repo contains the Gru and Minion scripts for handling multiple child processes.

First of all you need to clone the repository
* git clone <repository_url>

Make the files executable
* chmod +x gru minion

Run the program
for N in {1..10}
do
  ./gru $N 1>"stdout-$N.log" 2>"stderr-$N.log"
done
