var redis = require('redis')
var config = require('./config.json')
var ontologia = require('./ontologia.json')
var express=require('express') //Import 
var app=express();

 
function testRedis(redisClient){
	//redisClient.set('test','It's working,redis.print)
	redisClient.get('test',function(error,value){
			if(error){
				throw error
			}
			console.log("Testing a query in redis")
			console.log("-->" + value)
		})
}

function sendRedis(callback){	
	var redisClient = redis.createClient(config.redis.port, config.redis.host)
	console.log("Conectandose a redis")
	redisClient.on('error',function(error){
		console.log("Se presentó un error con redis")
	})
	console.log("Se envío mensaje a redis")
	callback(redisClient)
	redisClient.quit();
}
function printJson(json, mes,response){
	var print = mes 
	var clave = ''
	var valor = ''
	for(var root in json){		
		for(var subRoot in json[root]){
			valor = ''
			clave = root + ':' + subRoot
			for(var i=0;i<json[root][subRoot].length;i++){
				valor += json[root][subRoot][i] + ' ' 
				sendRedis(function(redisClient){
				redisClient.sadd(clave,json[root][subRoot][i])
				}
			)
			}

			print  += '<p>'+clave+' '+valor+'</p>'
		}
	}
	response.send(print)
	
}

var server = app.get('/', function(request, response){ //Start the main page 
	var msg = '<center><h1>Servidor del proyecto sin nombre</h1></center>' +
				  '<h3>A continuación se poblará la base de datos de REDIS</h3>'
	printJson(ontologia,msg,response);
	sendRedis(testRedis);
})
server.listen(config.node.port) 