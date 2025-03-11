import threading
import time

def input_with_timeout(prompt, timeout):
    # Function to read input from the user
    def target():
        nonlocal result
        result = input(prompt)
    
    result = None
    thread = threading.Thread(target=target)
    thread.start()
    thread.join(timeout)
    
    if thread.is_alive():
        print("Timeout!")
        return None
    else:
        return result

# Main logic
prompt = "Enter something within 5 seconds: "
timeout = 5
user_input = input_with_timeout(prompt, timeout)

if user_input is not None:
    print(f"Received input: {user_input}")
else:
    print("No input received within the timeout period.")
