const assert = require("assert")
const request = require("request")

describe("Index page", function(){
    it("should return correct status code 200 and good response.body", function(done){
        request("http://localhost:7865", function(err, response, body){
            assert.equal(response.statusCode, 200)
            assert.equal(response.body, "Welcome to the payment system");
            done();
        })
    })
})
