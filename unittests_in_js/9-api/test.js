const request = require("request")

request("http://localhost:7865", function(e, r, b){
            console.log(r.body)
            console.log(b)
        })
