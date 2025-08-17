def https_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown Status"
        
print(https_status(200))  # Output: OK
print(https_status(404))  # Output: Not Found
print(https_status(500))  # Output: Server Error
print(https_status(123))  # Output: Unknown Status