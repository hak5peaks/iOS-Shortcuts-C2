import http.server
import socketserver
from urllib.parse import unquote

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        with open('http-logs.txt', 'a') as log_file:
            log_entry = f"{self.client_address[0]} - - [{self.log_date_time_string()}] {format % args}\n"
            log_file.write(log_entry)

    def do_GET(self):
        client_ip = self.client_address[0]
        path = unquote(self.path.split('?')[0])
        directory = path[1:] if path.startswith('/') else path
        print(f"IP: {client_ip} Data Sent: {directory}")
        self.send_html_response()

    def send_html_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = """
        <html>
        <head>
            <title>Welcome to Fight Club</title>
        </head>
        <body>
            <h1>Welcome to Fight Club</h1>
        </body>
        </html>
        """
        self.wfile.write(html.encode('utf-8'))

def main():
    PORT = 8080

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(""" 
               ▌▄▄▄   ▄▄▄▄▄▄▄▄▄▄   ▄▄▌            
                ▄ ███ ▀████████▌ ███ ▄             
             ▄██▀ ███▌          ▐███ ▀██▄          
           ▄██▀ ▄███▀ ▄████████▄ ▀███▄ ▀██▄       
         ▄███▀ ████ ▄████████████▄ ████ ▐███▄      
        ████▀ ████▌ ▀▀           ▀▀ ▐████ ▀████    
       ████   ██████▄▄██████████▄▄██████   ████   
      ████  █▌ ▀█████████▀▀▀▀█████████▀ ▄█  ████   
     ████  ▄███  ▐████▀        ▀████▌  ███▌  ███▌  
     ███▌  ███▌  ████            ████  ████  ████  
     ███▌  ███▌  ███▌            ▐███  ▐███  ████  
     ███▌  ███▌  ████            ████  ████  ████  
     ████  ▀███   ████▄        ▄███████▄▀█▌  ███▌  
      ████  ████▄  ▀█████▄▄▄▄█████▀ ████ ▀  ████   
       ████  ▀████▄  ▀▀████████▀▀  ▄████   ████   
        ████▄  ▀████▄▄          ▄▄████▀  ▄████    
         ▀████▄  ▀██████████████████▀  ▄████▀      
           ▀████▄    ▀▀▀██████▀▀▀   ▄▄████▀       
             ▀▀  ▄▀           ▄▄▄███████▀          
              ▄███▄█████████████████▀             
             █████████▀▀▀▀▀▀▀▀▀▀                  
            ████████▄                              
           ██▀                                    
                           
             """)
        print("                  iOS C2 Beta 2")
        print("                 ---------------") 
        print("                   Http Server")
        print(f"Serving at port {PORT}")
        print("-----------------------------")
        httpd.serve_forever()

if __name__ == "__main__":
    main()
