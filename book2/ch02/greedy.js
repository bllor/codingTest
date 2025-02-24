const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function countCoins(n) {
  let count = 0;
  const coinTypes = [500, 100, 50, 10];

  for (const coin of coinTypes) {
    count += Math.floor(n / coin);
    n %= coin;
  }

  return count;
}

rl.question("금액을 입력하세요: ", (input) => {
  const n = parseInt(input, 10);
  if (!isNaN(n)) {
    console.log("필요한 동전 개수:", countCoins(n));
  } else {
    console.log("유효한 숫자를 입력하세요.");
  }
  rl.close();
});
