function getPaymentTokenFromAPI(success){
    if(success == true) {
        return new Promise(function(resolve){
            resolve({data: 'Successful response from the API' })
        })
    }
}

module.exports = getPaymentTokenFromAPI;
