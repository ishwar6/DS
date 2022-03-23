const http = require('http');
const WebSocketServer = require("websocket").server
let connection = null;

const httpserver = http.createServer((req, res) => {
	console.log('we have received a request');
});


httpserver.listen(8000, () => console.log('my server is listening'));

websocket.on("request", request=> {

    connection = request.accept(null, request.origin)
    connection.on("open", () => console.log("Opened!!!"))
    connection.on("close", () => console.log("CLOSED!!!"))
    connection.on("message", message => {

        console.log(`Received message ${message.utf8Data}`)
        connection.send(`got your message: ${message.utf8Data}`)
    })