const Utils = require("./utils.js");
const sendPaymentRequestToApi = require('./4-payment.js')
const sinon = require("sinon");
const expect = require("chai").expect;

describe("sendPaymentRequestToApi", function(){
    const spyConsoleLog = sinon.spy(console, 'log');
    it("should use correctly Utils.calculateNumber", function(){
        // Stub de Utils.calculateNumber pour contrôler son comportement
        const stubCalculateNumber = sinon.stub(Utils, "calculateNumber").returns(10)
        // appel de la fonction sendPayment....
        sendPaymentRequestToApi(100, 20)
        // Vérification si calculateNumber() à été utiliser une fois avec les bons arguments
        expect(stubCalculateNumber.calledOnceWithExactly("SUM", 100, 20)).to.be.true
        // Vérification si console.log est appelé une fois avec le bon message
        expect(spyConsoleLog.calledOnceWithExactly("The total is: 10"))
        stubCalculateNumber.restore()
        spyConsoleLog.restore()
    });
});
