http_status = 501

match http_status:   
   case 200 | 201:     # if 200 0r 201
     print("success")
   case 400:        # elif 400
     print("Bad Request")
   case 500 | 501:       #elif 500 or 501
     print("Server Error")
   case _:      #else like default
    print("Unknown")
