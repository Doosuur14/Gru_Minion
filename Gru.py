#!/usr/bin/env python3
import os
import sys
import random

def main():
    if len(sys.argv) != 2:
        print("Usage: python gru.py <N>")
        sys.exit(1)

    N = int(sys.argv[1])
    if N <= 0:
        print("N should be greater than 0.")
        sys.exit(1)

    pid = os.getpid()
    print(f"Gru[{pid}]: starting.")

    child_pids = []
    
    for _ in range(N):
        child_pid = os.fork()
        if child_pid == -1:
            print("Fork failed", file=sys.stderr)
            sys.exit(1)
        elif child_pid == 0:  
            random_sleep_time = random.randint(5, 10)
            print(f"Child process PID {os.getpid()} executing Minion with sleep time {random_sleep_time}.", file=sys.stderr)
            os.execl("./minion", "minion", str(random_sleep_time))

        else:
            child_pids.append(child_pid)
            print(f"Gru[{pid}]: process created. PID {child_pid}.", file=sys.stderr)
    
    # Wait for all child processes to complete
    for child_pid in child_pids:
        pid, status = os.waitpid(child_pid, 0)
        exit_status = os.WEXITSTATUS(status)
        print(f"Gru[{pid}]: process terminated. PID {child_pid}. Exit status {exit_status}.", file=sys.stderr)

        if exit_status != 0:
            print(f"Gru[{pid}]: retrying process creation.", file=sys.stderr)
            retry_child_pid = os.fork()
            if retry_child_pid == -1:
                print("Fork failed", file=sys.stderr)
                sys.exit(1)
            if retry_child_pid == 0:
                random_sleep_time = random.randint(5, 10)
                os.execl("./minion", "minion", str(random_sleep_time))
            else:
                child_pids.append(retry_child_pid)
                print(f"Gru[{pid}]: process created. PID {retry_child_pid}.", file=sys.stderr)

    sys.exit(0)

if __name__ == "__main__":
    main()
