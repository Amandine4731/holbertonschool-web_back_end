const Utils = require("./utils.js");
const sendPaymentRequestToApi = require('./5-payment.js')
const sinon = require("sinon");
const expect = require("chai").expect;
const assert = require("assert")

describe("sendPaymentRequestToApi", function(){

    let spyConsoleLog;

    beforeEach(function(){
        spyConsoleLog = sinon.spy(console, 'log');
    })

    afterEach(function(){
        spyConsoleLog.restore()
    })

    it("should return the good string 'The total is: 120'", function(){
        sendPaymentRequestToApi(100, 20)
        assert(spyConsoleLog.calledOnceWithExactly("The total is: 120"))
    });
    
    it("should return the good string 'The total is: 20'", function(){
        sendPaymentRequestToApi(10, 10)
        assert(spyConsoleLog.calledOnceWithExactly("The total is: 20"))
    });
});
