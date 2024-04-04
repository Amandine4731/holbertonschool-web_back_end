const assert = require("assert");
const { response } = require("express");
const request = require("request")

describe("Index page", function(){
    it("should the correct status code 200 when id is a number", function(done){
        options = {
            url: 'http://localhost:7865',
            method: 'GET',
        }
        request("http://localhost:7865/cart/12", function(err, response, body){
            assert.equal(response.statusCode, 200)
            assert.equal(response.body, "Payment methods for cart 12")
            done();
        })
    });

    it("should return SC 200 and Welcome to the payment system", function(done){
        request.get("http://localhost:7865", function(e, r, b){
            assert.equal(r.statusCode, 200)
            assert.equal(r.body, "Welcome to the payment system")
            done();
        })
    });

    it("should the correct status code 200 when id is not a number", function(done){
        request("http://localhost:7865/cart/test", function(err, response, body){
            assert.equal(response.statusCode, 404)
            done();
        })
    });
})
