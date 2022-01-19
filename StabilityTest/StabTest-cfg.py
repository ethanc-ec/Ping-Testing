import pathlib as pl # pathlib for the file locations

def HighPingChecker(filename):
    
    configScaler = 1.00
    
    #Reading config for the scaler
    with open(pl.Path(__file__).parent / "StabTestConfig.cfg") as config:
        
        configRead = config.read().splitlines()
        
        configReadScale = configRead[2].split("=")
        
        configScaler = float(configReadScale[1])
        
        print("The ping comparison scaler is: {}".format(configScaler))
        
    # Reading data file
    with open(pl.Path(__file__).parent / filename) as testLog:

        # Copies the data from the file and puts each line into a list
            contents = testLog.read().splitlines()
            
            HighPingTimes = {}
            
            totalping, totalpingcount = 0, 0
            
            for i in contents:
                if "Reply" in i:
                    splitI = i.split(" ")
                    
                    pingTimeI = splitI[4]
                
                    pingTime = int(pingTimeI[5:-2]) # Only has time="___"ms
                        
                    totalping += pingTime
                        
                    totalpingcount += 1
                
            avgPing = round(totalping/totalpingcount, 2)
            
            for idx, reply in enumerate(contents):

                # Skips past ping command, timeouts, etc.
                if "Reply" in reply:

                    # Splits the selected string into separate pieces, able to take "time=___ms"
                    contentSplit = reply.split(" ")
                    
                    pingTimeMs = contentSplit[4] # Contains "time=___ms"
                    
                    pingTime = int(pingTimeMs[5:-2]) # Only has time="___"ms
                    
                    if pingTime > avgPing * configScaler:
                        HighPingTimes[idx] = pingTimeMs
                
                # Just checks for timeouts 
                elif "Request timed out." in reply:
                    HighPingTimes[idx] = reply
            
            # Checks if there actually are high pings, if so, it'll print out the time and ping as a line
            if HighPingTimes != {}:
                
                print("The average ping was {} ms".format(avgPing))
                
                print("Here is a list of the times where the ping was higher than the average:") 
                
                for i in HighPingTimes:
                    print(i, HighPingTimes[i])
                    
            else:
                print("There were no instances where the ping was higher than the average")


def validFileInput():
    
    # Choose demo file or custom file
    with open(pl.Path(__file__).parent / "StabTestConfig.cfg") as config:
        
        configRead = config.read().splitlines()
        
        if "True" in configRead[0]:
            return "PingTestDemo.txt"
         
        elif "False" in configRead[0]:
            customFileName = configRead[1].split("=")
            return customFileName[1]
        
        else:
            return 'Failed'
            
            
def fileCheckCaller(inputTestFile):
    
    # Actually checking the input file
    try:
        return HighPingChecker(inputTestFile)
    
    # If it doesn't work it just prints an error message and goes to the exception function
    except:
        return print("Error: Either a file with the specified name does not exist or there is an issue with the config file")

                   
def runFileFunctions():
    
    # Basically calls everything and actually runs the script
    inputTestFile = validFileInput()
    
    if "Failed" in inputTestFile:
        return print("Error: The setting for UseDemoFile is incorrect, it needs to be True or False")
    
    else:
        print("Checking file with name: {}".format(inputTestFile))
    
        return fileCheckCaller(inputTestFile)
    
if __name__ == "__main__":
    runFileFunctions()