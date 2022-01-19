# pathlib for the file locations
import pathlib

class CheckHighPing:
    
    def __init__(self, filename):
        self.filename = filename
        
    def HighPingChecker(filename):
        # Safely opens the file and closes it when done
        with open(pathlib.Path(__file__).parent / filename) as testLog:

            # Copies the data from the file and puts each line into a list
            contents = testLog.read().splitlines()
            
            HighPingTimes = {}
            
            for idx, reply in enumerate(contents):
                
                # Skips past ping command, timeouts, etc.
                if "Reply" in reply:
                    
                    # Checks to see if ping has at least three digits by seeing if time={}ms has three ints
                    try:
                        
                        # Checks for ping w/ 3 or more digits
                        int(reply[34:37])
                        
                        pingTime = reply.split(" ")
                        
                        HighPingTimes[idx] = pingTime[4]
                        
                    # Skips that line if it does not start with "Reply"    
                    except:
                        pass
                
                # Just checks for timeouts 
                elif "Request timed out." in reply:
                    HighPingTimes[idx] = reply
            
            # Checks if there actually are high pings, if so, it'll print out the time and ping as a line
            if HighPingTimes != {}:
                print("Here is a list of the times with high ping:")
                for i in HighPingTimes:
                    print(i, HighPingTimes[i])
            else:
                return "There were no instances of high ping"


def validFileInput():
    # Choose demo file or custom file
    filePicker = input("Do you want to use the demo file? (y/n) ")

    # Section for dealing with input
    if filePicker == "y":
        return "PingTestDemo.txt"
        
    elif filePicker == "n":
        return input("Name of the file: ")
        
    else:
        print("Your input was invalid, try again")
        return validFileInput()
            
            
def fileCheckCaller(inputTestFile):
    # Actually checking the input file
    try:
        CheckHighPing.HighPingChecker(inputTestFile)
    
    # If it doesn't work it just prints an error message and goes to the exception function
    except:
        print("A file with that name was not found in the same directory as the script")
        fileCheckCallerException()
        
        
def fileCheckCallerException():
    # Checks to see if the user wants to go agane
    tryAgain = input("Do you want to try again? (y/n) ")
    
    if tryAgain == "y":
        return runFileFunctions()
    
    elif tryAgain == "n":
        return print("What are you doing?")
    
    else:
        print("Your input was invalid, try again")
        return fileCheckCallerException()

                   
def runFileFunctions():
    # Basically calls everything and actually runs the script
    inputTestFile = validFileInput()
    
    print("Checking file with name: {}".format(inputTestFile))
    
    fileCheckCaller(inputTestFile)
    
if __name__ == "__main__":
    runFileFunctions()