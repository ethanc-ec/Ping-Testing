from pathlib import Path

def high_ping_checker(file_name):
    
    config_scaler = 1.00
    
    #Reading config for the scaler
    with open(Path(__file__).parent / "StabTestConfig.cfg") as config:
        
        config_read = config.read().splitlines()
        
        config_read_scaler = config_read[2].split("=")
        
        config_scaler = float(config_read_scaler[1])
        
        print("The ping comparison scaler is: {}".format(config_scaler))
        
    # Reading data file
    with open(Path(__file__).parent / file_name) as test_log:

        # Copies the data from the file and puts each line into a list
            contents = test_log.read().splitlines()
            
            high_ping_times = {}
            
            total_pings, total_ping_count = 0, 0
            
            for i in contents:
                if "Reply" in i:
                    split_i = i.split(" ")
                    
                    ping_time_i = split_i[4]
                
                    ping_time = int(ping_time_i[5:-2]) # Only has time="___"ms
                        
                    total_pings += ping_time
                        
                    total_ping_count += 1
                
            avg_ping = round(total_pings/total_ping_count, 2)
            
            for idx, reply in enumerate(contents):

                # Skips past ping command, timeouts, etc.
                if "Reply" in reply:

                    # Splits the selected string into separate pieces, able to take "time=___ms"
                    content_split = reply.split(" ")
                    
                    ping_time_ms = content_split[4] # Contains "time=___ms"
                    
                    ping_time = int(ping_time_ms[5:-2]) # Only has time="___"ms
                    
                    if ping_time > avg_ping * config_scaler:
                        high_ping_times[idx] = ping_time_ms
                
                # Just checks for timeouts 
                elif "Request timed out." in reply:
                    high_ping_times[idx] = reply
            
            # Checks if there actually are high pings, if so, it'll print out the time and ping as a line
            if high_ping_times != {}:
                
                print("The average ping was {} ms".format(avg_ping))
                
                print("Here is a list of the times where the ping was higher than the average:") 
                
                for i in high_ping_times:
                    print(i, high_ping_times[i])
                    
            else:
                print("There were no instances where the ping was higher than the average")


def valid_file_input():
    
    # Choose demo file or custom file
    with open(Path(__file__).parent / "StabTestConfig.cfg") as config:
        
        config_read = config.read().splitlines()
        
        if "True" in config_read[0]:
            return "PingTestDemo.txt"
         
        elif "False" in config_read[0]:
            custom_file_name = config_read[1].split("=")
            return custom_file_name[1]
        
        else:
            return 'Failed'
            
            
def file_check_caller(input_test_file):
    
    # Actually checking the input file
    try:
        return high_ping_checker(input_test_file)
    
    # If it doesn't work it just prints an error message and goes to the exception function
    except:
        return print("Error: Either a file with the specified name does not exist or there is an issue with the config file")

                   
def run_file_functions():
    
    # Basically calls everything and actually runs the script
    input_test_file = valid_file_input()
    
    if "Failed" in input_test_file:
        return print("Error: The setting for UseDemoFile is incorrect, it needs to be True or False")
    
    else:
        print("Checking file with name: {}".format(input_test_file))
    
        return file_check_caller(input_test_file)
    
if __name__ == "__main__":
    run_file_functions()