const express = require("express")
const app = express();
app.use(express.json());
const port = 7865;

app.get('/', (request, response) => {
    response.send('Welcome to the payment system');
});

app.get("/cart/:id([0-9]+)", function(request, response){
    const id = request.params.id
    response.send(`Payment methods for cart ${id}`)
})

app.get("/available_payments", function(request, response){
    response.json({
        "payment_methods": {
          "credit_cards": true,
          "paypal": false
        }
      })
})
app.post('/login', (req, res) => {
    res.end(`Welcome ${req.body.userName}`);
  });

app.listen(port, function(){
    console.log(`API available on localhost port ${port}`)
})
