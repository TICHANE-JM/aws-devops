var http = require("http")

http.createServer(function (request, response) {

   // Send the HTTP header
   // HTTP Status: 200 : OK
   // Content Type: text/plain
   response.writeHead(200, {'Content-Type': 'text/plain'})

   //Envoyer le corps de la réponse sous la forme "Hello World"
   response.end('Hello World\n')
}).listen(3000)

// La console imprimera le message
console.log('Server running')
