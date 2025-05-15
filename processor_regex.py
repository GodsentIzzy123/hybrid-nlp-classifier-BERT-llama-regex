import re
def classify_with_regex(log_message):
    regex_patterns = {
        r"User User\d+ logged (out|in)." : "User Action",
        r"Account with ID \d+ created by User\d+." : "User Action",
        r"System reboot initiated by user .*" : "System Notification",
        r"System updated to version .*" : "System Notification",
        r"Backup started at .*" : "System Notification",
        r"Backup ended at .*": "System Notification",
        r"Backup completed successfully": "System Notification",
        r"File .* uploaded successfully by user .*" : "System Notification",
        r"Disk cleanup completed successfully." : "System Notification",
        r"Server .* suffered an abrupt restart during .*" : "System Diagnostic",
        r"Server .* .* potential security .*" :    "Security Notification",
        r"Security breach suspected from IP address .*" : "Security Notification",
        r"Possible hacking attempt identified from IP .*" : "Security Notification",
        r"Unauthorised access attempt from .*": "Security Notification",
        r"Unusual access attempt from .*" : "Security Notification",
        r"Account Account.* .* login" : "Login Issues",
        r".* RAID .*" : "Hard Disk Issues",
        r".*Critical system" : "Critical Error",
        r".*critical system" : "Critical Error"

    }    
    for pattern,label in regex_patterns.items():
    
        if re.search(pattern, log_message, re.IGNORECASE): 
            return label
    
    return None

if __name__ == "__main__":
    print(classify_with_regex("User User1 logged in."))
    print(classify_with_regex("User User2 logged out."))           
    print(classify_with_regex("Account with ID 12345 created by User1."))
    print(classify_with_regex("System reboot initiated by user admin."))
    print(classify_with_regex("System updated to version 1.2.3."))
    print(classify_with_regex("Backup started at 2023-10-01 12:00:00."))
    print(classify_with_regex("Backup ended at 2023-10-01 12:30:00."))
    print(classify_with_regex("Hey Brother , Whats up ?"))