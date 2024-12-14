#!/usr/bin/env python3

# import os
# import sys
# import random

# def main():
#     # Check if the program was run with the correct number of arguments
#     if len(sys.argv) != 2:
#         print("Usage: python gru.py <N>")
#         sys.exit(1)

#     N = int(sys.argv[1])
#     if N <= 0:
#         print("N should be greater than 0.")
#         sys.exit(1)

#     pid = os.getpid()  # Get the parent PID
#     print(f"Gru[{pid}]: starting.")

#     child_pids = []
    
#     # Create N child processes
#     for _ in range(N):
#         child_pid = os.fork()
#         if child_pid == -1:
#             print("Fork failed")
#             sys.exit(1)
#         elif child_pid == 0:  # Child process
#             # Execute the minion program with a random number between 5 and 10
#             random_sleep_time = random.randint(5, 10)
#             print(f"Child process PID {os.getpid()} executing Minion with sleep time {random_sleep_time}.")
#             os.execl("./Minion.py", "Minion.py", str(random_sleep_time))
#         else:
#             # Parent process
#             child_pids.append(child_pid)
#             print(f"Gru[{pid}]: process created. PID {child_pid}.")
    
#     # Wait for all child processes to complete
#     for child_pid in child_pids:
#         pid, status = os.waitpid(child_pid, 0)
#         exit_status = os.WEXITSTATUS(status)
#         print(f"Gru[{pid}]: process terminated. PID {child_pid}. Exit status {exit_status}.")

#         # If the child process failed (exit status != 0), create another child process
#         if exit_status != 0:
#             print(f"Gru[{pid}]: retrying process creation.")
#             child_pid = os.fork()
#             if child_pid == -1:
#                 print("Fork failed")
#                 sys.exit(1)
#             if child_pid == 0:
#                 random_sleep_time = random.randint(5, 10)
#                 # os.execl("./Minion.py", "Minion.py", str(random_sleep_time))
#                 os.execl("/usr/bin/python3", "python3", "./Minion.py", str(random_sleep_time))
#             else:
#                 child_pids.append(child_pid)
#                 print(f"Gru[{pid}]: process created. PID {child_pid}.")

#     # If all child processes were successful, exit with status 0
#     sys.exit(0)

# if __name__ == "__main__":
#     main()





import os
import sys
import random

def main():
    # Check if the program was run with the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python gru.py <N>")
        sys.exit(1)

    N = int(sys.argv[1])
    if N <= 0:
        print("N should be greater than 0.")
        sys.exit(1)

    pid = os.getpid()  # Get the parent PID
    print(f"Gru[{pid}]: starting.")

    child_pids = []
    
    # Create N child processes
    for _ in range(N):
        child_pid = os.fork()
        if child_pid == -1:
            print("Fork failed")
            sys.exit(1)
        elif child_pid == 0:  # Child process
            random_sleep_time = random.randint(5, 10)
            print(f"Child process PID {os.getpid()} executing Minion with sleep time {random_sleep_time}.")
            # Ensure Minion.py is executed with Python 3
            os.execl("/usr/bin/python3", "python3", "./Minion.py", str(random_sleep_time))
        else:
            # Parent process
            child_pids.append(child_pid)
            print(f"Gru[{pid}]: process created. PID {child_pid}.")
    
    # Wait for all child processes to complete
    for child_pid in child_pids:
        pid, status = os.waitpid(child_pid, 0)
        exit_status = os.WEXITSTATUS(status)
        print(f"Gru[{pid}]: process terminated. PID {child_pid}. Exit status {exit_status}.")

        # If the child process failed (exit status != 0), create another child process
        if exit_status != 0:
            print(f"Gru[{pid}]: retrying process creation.")
            retry_child_pid = os.fork()
            if retry_child_pid == -1:
                print("Fork failed")
                sys.exit(1)
            if retry_child_pid == 0:
                random_sleep_time = random.randint(5, 10)
                os.execl("/usr/bin/python3", "python3", "./Minion.py", str(random_sleep_time))
            else:
                child_pids.append(retry_child_pid)
                print(f"Gru[{pid}]: process created. PID {retry_child_pid}.")

    # If all child processes were successful, exit with status 0
    sys.exit(0)

if __name__ == "__main__":
    main()
