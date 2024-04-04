const chai = require('chai');
const expect = chai.expect;
const calculateNumber = require('./2-calcul_chai.js');

describe('Test Calcul function', function(){
    describe("function type is SUM", function(){
        it('should work when type is SUM', function(){
            expect(calculateNumber("SUM", 2, 3)).to.equal(5);
        });
    });
    describe("function type is SUBTRACT", function(){
        it('should work when type is SUBTRACT', function(){
            expect(calculateNumber('SUBTRACT', 2, 3)).to.equal(-1);
            expect(calculateNumber('SUBTRACT', 5.75, 3.25)).to.equal(3);
            expect(calculateNumber('SUBTRACT', -10.25, -11)).to.equal(1);
        });
    });
    describe("function type is DIVIDE", function(){
        it('should work when type is DIVIDE', function(){
            expect(calculateNumber('DIVIDE', 3.25, 1.5)).to.equal(1.5);
            expect(calculateNumber('DIVIDE', 81.23, 8.75)).to.equal(9);
        });
        it("return 'Error' when b is equal to 0", function(){
            expect(calculateNumber('DIVIDE', 1.25, 0)).to.equal('Error');
        });
    });
});
