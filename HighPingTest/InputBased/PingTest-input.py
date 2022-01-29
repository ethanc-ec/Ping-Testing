# pathlib for the file locations
from pathlib import Path

def high_ping_checker(file_name):
    # Safely opens the file and closes it when done
    with open(Path(__file__).parent / file_name) as test_log:

        # Copies the data from the file and puts each line into a list
        contents = test_log.read().splitlines()
        
        high_ping_times = {}
        
        for idx, reply in enumerate(contents):
            
            # Skips past ping command, timeouts, etc.
            if "Reply" in reply:
                
                # Checks to see if ping has at least three digits by seeing if time={}ms has three ints
                try:
                    
                    # Checks for ping w/ 3 or more digits
                    int(reply[34:37])
                    
                    # Splits the selected string into separate pieces, able to take "time=___ms"
                    ping_times = reply.split(" ")
                    
                    high_ping_times[idx] = ping_times[4]
                    
                # Skips that line if it does not start with "Reply"    
                except:
                    pass
            
            # Just checks for timeouts 
            elif "Request timed out." in reply:
                high_ping_times[idx] = reply
        
        # Checks if there actually are high pings, if so, it'll print out the time and ping as a line
        if high_ping_times != {}:
            print("Here is a list of the times with high ping:")
            
            for i in high_ping_times:
                print(i, high_ping_times[i])
                
        else:
            return print("There were no instances of high ping")


def valid_file_input():
    # Choose demo file or custom file
    file_picker = input("Do you want to use the demo file? (y/n) ")

    # Section for dealing with input
    if file_picker == "y":
        return "PingTestDemo.txt"
        
    elif file_picker == "n":
        return input("Name of the file: ")
        
    else:
        print("Your input was invalid, try again")
        return valid_file_input()
            
            
def file_check_caller(input_test_file):
    # Actually checking the input file
    try:
        return high_ping_checker(input_test_file)
    
    # If it doesn't work it just prints an error message and goes to the exception function
    except:
        print("A file with that name was not found in the same directory as the script")
        return file_check_caller_except()
        
        
def file_check_caller_except():
    # Checks to see if the user wants to go agane
    tryAgain = input("Do you want to try again? (y/n) ")
    
    if tryAgain == "y":
        return run_file_functions()
    
    elif tryAgain == "n":
        return print("What are you doing?")
    
    else:
        print("Your input was invalid, try again")
        return file_check_caller_except()

                   
def run_file_functions():
    # Basically calls everything and actually runs the script
    input_test_file = valid_file_input()
    
    print("Checking file with name: {}".format(input_test_file))
    
    return file_check_caller(input_test_file)
    
if __name__ == "__main__":
    run_file_functions()