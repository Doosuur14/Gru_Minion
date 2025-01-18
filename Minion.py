#!/usr/bin/env python3
import os
import sys
import time
import random

def main():
    if len(sys.argv) != 2:
        print("Usage: python minion.py <S>")
        sys.exit(1)

    sleep_time = int(sys.argv[1])
    pid = os.getpid()
    ppid = os.getppid()

    print(f"Minion[{pid}]: created. Parent PID {ppid}.", file=sys.stderr)
    time.sleep(sleep_time)

    exit_status = random.choice([0, 1])

    print(f"Minion[{pid}]: before terminated. Parent PID {ppid}. Exit status {exit_status}.", file=sys.stderr)
    sys.exit(exit_status)

if __name__ == "__main__":
    main()
