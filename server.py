from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
from datetime import datetime, timedelta
import random

class DashboardHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            # Generate some sample data
            data = {
                'temperature': random.uniform(10, 30),
                'humidity': random.uniform(20, 60),
                'pressure': random.uniform(15, 20),
                'energy': random.uniform(50, 100),
                'timeLabels': [(datetime.now() - timedelta(hours=x)).strftime('%H:%M') for x in range(6)],
                'temperatureHistory': [random.uniform(10, 30) for _ in range(6)],
                'humidityHistory': [random.uniform(20, 60) for _ in range(6)]
            }
            
            self.wfile.write(json.dumps(data).encode())
            return
            
        return SimpleHTTPRequestHandler.do_GET(self)

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, DashboardHandler)
    print('Server running on http://localhost:8000')
    httpd.serve_forever() 