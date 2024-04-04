const Utils = require("./utils")

function sendPaymentRequestToApi(totalAmount, totalShipping){
    let result = Utils.calculateNumber("SUM", totalAmount, totalShipping);
    console.log(`The total is: ${result}`);    
}

module.exports = sendPaymentRequestToApi;
