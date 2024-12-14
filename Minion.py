#!/usr/bin/env python3

import os
import sys
import time
import random

def main():
    if len(sys.argv) != 2:
        print("Usage: python Minion.py <S>")
        sys.exit(1)

    sleep_time = int(sys.argv[1])
    pid = os.getpid()
    ppid = os.getppid()

    print(f"Minion[{pid}]: created. Parent PID {ppid}.")

    # Sleep for S seconds
    time.sleep(sleep_time)

    # Randomly decide exit status (0 for success, 1 for failure)
    exit_status = random.choice([0, 1])

    print(f"Minion[{pid}]: before terminated. Parent PID {ppid}. Exit status {exit_status}.")

    # Exit with the chosen status
    sys.exit(exit_status)

if __name__ == "__main__":
    main()
