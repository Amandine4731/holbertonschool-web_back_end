const Utils = require("./utils");
const sendPaymentRequestToApi = require('./3-payment.js')
const sinon = require("sinon");
const expect = require("chai").expect;

describe("sendPaymentRequestToApi", function(){
    it("should use correctly Utils.calculateNumber", function(){
        // spy pour suivre l'activité de Utils.calculateNumber
        const spyCalculateNumber = sinon.spy(Utils, "calculateNumber")
        // appel de la fonction sendPayment....
        sendPaymentRequestToApi(100, 20)
        // Vérification si calculateNumber() à été utiliser une fois avec les bons arguments
        expect(spyCalculateNumber.calledOnceWithExactly("SUM", 100, 20)).to.be.true
        spyCalculateNumber.restore()
    });
});
