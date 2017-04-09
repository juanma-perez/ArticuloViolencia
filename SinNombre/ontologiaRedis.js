var redis = require('redis')
var config = require('./config.json')
var ontologia = require('./ontologia.json')
var express=require('express') //Import 
var app=express();

function sendRedis(callback){	
	var redisClient = redis.createClient(config.redis.port, config.redis.host)
	console.log("Conectandose a redis")
	redisClient.on('error',function(error){
		console.log("Se presentó un error con redis")
	})
	console.log("Se envío mensaje a redis")
	callback(redisClient)
	console.log("Se envio acabó el mensaje")
	
}


function testRedis(redisClient){
	//redisClient.set('test','It's working,redis.print)
	redisClient.get('test',function(error,value){
			if(error){
				throw error
			}
			console.log("Testing a query in redis")
			console.log("-->" + value)
		})
	redisClient.quit();
}

function addSet(root, json){
	sendRedis(function(redisClient){
		for(var subRoot in json){
			clave = root + ':' + subRoot
			for(var i=0;i<json[subRoot].length;i++){
				console.log("sadd "+clave+" " +json[subRoot][i])
				sendRedis(function(redisClient){
					redisClient.sadd(clave,json[subRoot][i], function(err,res){
						if(err){
							console.log("Falló la ejecución del comando: " + err)
						}
					})
				})
				
			}
		}
	})
}


app.get('/', function(request, response){ //Start the main page 
	console.log("Conecting to Node Server...")
	//
	response.render('index.html');
	console.log("Connection completed");
	sendRedis(testRedis);
	addSet("nodos", ontologia.nodos);		
		addSet("relaciones", ontologia.relaciones);
		addSet("sinonimos", ontologia.sinonimos);
		
}).listen(3000)
