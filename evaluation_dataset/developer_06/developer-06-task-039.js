function(immediateFN, connectFN, disconnectFN, port) {
	var app = require('express')(),
		server = require('http').createServer(app),
		io = require('socket.io').listen(server),
		path = require('path'),
		browserify = require('browserify-middleware');
	io.set('log level', 2);
	server.listen(port || process.env.PORT || 80);
	var browserifyOptions = {};
	browserifyOptions[path.join(__dirname + '/npm_crafty.client.js')] = {expose: 'npm_crafty'};
	app.get('/npm_crafty.js', browserify([browserifyOptions]));
	app.get('/crafty_client.js', function (req, res) {
		res.sendfile(path.join(__dirname + '/crafty_client.js'));
	});
	io.sockets.on('connection', function (socket) {
		console.log("Connected ", socket.id);
		connectFN(socket);
		socket.on('disconnect', function (arg) {
			console.log("Disconnected ", socket.id);
			disconnectFN(socket);
		});
	});
	process.nextTick(immediateFN);
	var _server = new Server(io.sockets);
	_server.app = app;
	_server.server = server;
	_server.io = io;
	return _server;
}