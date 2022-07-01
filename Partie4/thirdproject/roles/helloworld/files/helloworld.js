var http = require("http")

http.createServer(function (request, response) {

   // Envoyer l'en-tête HTTP
   // Statut HTTP : 200 : OK
   // Type de contenu : texte/brut
   response.writeHead(200, {'Content-Type': 'text/plain'})

   // Envoyer le corps de la réponse sous la forme "Hello World"
   response.end('Hello World\n')
}).listen(3000)

// La console affichera le message
console.log('Server running')
