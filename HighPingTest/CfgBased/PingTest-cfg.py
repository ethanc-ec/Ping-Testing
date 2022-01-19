# pathlib for the file locations
import pathlib as pl

class CheckHighPing:
    
    def __init__(self, filename):
        self.filename = filename
        
    def HighPingChecker(filename):
        # Safely opens the file and closes it when done
        with open(pl.Path(__file__).parent / filename) as testLog:

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
                        
                        # Splits the selected string into separate pieces, able to take "time=___ms"
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
                return print("There were no instances of high ping")


def validFileInput():
    # Choose demo file or custom file
    with open(pl.Path(__file__).parent / "PingTestConfig.cfg") as config:
        
        configRead = config.read().splitlines()
        
        if "True" in configRead[0]:
            return "PingTestDemo.txt"
         
        elif "False" in configRead[0]:
            customeFileName = configRead[1].split("=")
            return customeFileName[1]
        
        else:
            return 'Failed'
            
            
def fileCheckCaller(inputTestFile):
    # Actually checking the input file
    try:
        return CheckHighPing.HighPingChecker(inputTestFile)
    
    # If it doesn't work it just prints an error message and goes to the exception function
    except:
        return print("A file with that name was not found in the same directory as the script")

                   
def runFileFunctions():
    # Basically calls everything and actually runs the script
    inputTestFile = validFileInput()
    
    if "Failed" in inputTestFile:
        return print("The setting for UseDemoFile is incorrect, it needs to be True or False")
    
    else:
        print("Checking file with name: {}".format(inputTestFile))
    
        return fileCheckCaller(inputTestFile)
    
if __name__ == "__main__":
    runFileFunctions()