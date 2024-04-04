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

    it("should return Welcome :username and SC 200", function(done){
        const parametre = {
            url: 'http://localhost:7865/login',
            method: 'POST',
            json: {
              userName: 'Vaal34',
            },
          };
        request(parametre, function(err, response, body){
            assert.equal(response.statusCode, 200)
            assert.equal(response.body, "Welcome Vaal34")
            done();
        })  
    });

    it("should the correct status code 200 and JSON", function(done){
        request("http://localhost:7865/available_payments", function(err, response, body){
            assert.equal(response.statusCode, 200)
            assert.equal(response.body, '{"payment_methods":{"credit_cards":true,"paypal":false}}')
            done();
        })
    });
})
