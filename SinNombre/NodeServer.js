var redis = require('redis')
var config = require('./config.json')
var ontologia = require('./ontologia.json')

function sendRedis(callback){	
	var redisClient = redis.createClient(config.redis.port, config.redis.host)
	redisClient.on('error',function(error){
		console.log("Se presentó un error con redis")
	})
	callback(redisClient)
	redisClient.quit();
}

function addSet(root, json){	
	for(var subRoot in json){
		clave = root + ':' + subRoot
		for(var i=0;i<json[subRoot].length;i++){
			sendRedis(function(redisClient){				
				console.log("sadd "+clave+" " +json[subRoot][i])
				redisClient.sadd(clave,json[subRoot][i],redisClient.print)
			})
		}
	}	
}

process.on("exit",function(){	
		console.log('A continuación se poblará la base de datos de REDIS')
		addSet("nodos", ontologia.nodos);
		addSet("relaciones", ontologia.relaciones);
		addSet("sinonimos", ontologia.sinonimos);
		}

	)
