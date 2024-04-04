const assert = require("assert");
const calculateNumber = require('./1-calcul.js');

describe('Test Calcul function', function(){
    describe("function type is SUM", function(){
        it('should work when type is SUM', function(){
            assert.equal(calculateNumber("SUM", 2, 3), 5);
        });
    });
    describe("function type is SUBTRACT", function(){
        it('should work when type is SUBTRACT', function(){
            assert.equal(calculateNumber('SUBTRACT', 2, 3), -1);
            assert.equal(calculateNumber('SUBTRACT', 5.75, 3.25), 3);
            assert.equal(calculateNumber('SUBTRACT', -10.25, -11), 1);
        });
    });
    describe("function type is DIVIDE", function(){
        it('should work when type is DIVIDE', function(){
            assert.equal(calculateNumber('DIVIDE', 3.25, 1.5), 1.5);
            assert.equal(calculateNumber('DIVIDE', 81.23, 8.75), 9);
        });
        it("return 'Error' when b is equal to 0", function(){
            assert.equal(calculateNumber('DIVIDE', 1.25, 0), 'Error');
        });
    });
})
