const expect = require("chai").expect;
const getPaymentTokenFromAPI = require("./6-payment_token")
const chai = require("chai")

describe("getPaymentTokenFromAPI", function(){
    it("should getPaymentTokenFromAPI return succesfull response from API", function(done){
        getPaymentTokenFromAPI(true)
        .then(function(resolve){
            expect(resolve).to.include({ data: 'Successful response from the API' });
            done();
        })
        .catch(function(error){
            done(error);
        })
    })
})
