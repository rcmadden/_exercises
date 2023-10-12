// create a functoin to calculate the sum of all numbers from 1 up to (and including) some number n
function addUpTo(n) {
	let total = 0;
    for (let i = 1; i <= n; i++) {
    	total += i;
    }
    return total;
}

addUpTo(10)