var assert = require("assert");
const calculateNumber = require('./0-calcul.js');

describe('Test Rounded', function(){
    it('should work', function(){
        assert.equal(calculateNumber(2, 3), 5);
        assert.equal(calculateNumber(2, 3.5), 6);
        assert.equal(calculateNumber(1.23, 6.65), 8);
    });
    it('should work with a negative number', function(){
        assert.equal(calculateNumber(-2.56, -17,89), -20)
        assert.equal(calculateNumber(-5.39, -1.19), -6)
        assert.equal(calculateNumber(-1783758.3, -3830384.7), -5614143)
    });
})
