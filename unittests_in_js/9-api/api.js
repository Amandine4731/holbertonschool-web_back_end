const express = require("express")
const app = express();
const port = 7865;

app.get('/', (request, response) => {
    response.send('Welcome to the payment system');
});

app.get("/cart/:id([0-9]+)", function(request, response){
    const id = request.params.id
    response.send(`Payment methods for cart ${id}`)
})

app.listen(port, function(){
    console.log(`API available on localhost port ${port}`)
})
