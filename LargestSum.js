const largestSum = (arr) => {
  let winner;
  let score = 0;
  for (let i = 0; i < arr.length; i++) {
    const sub = [...arr].splice(i);
    for (let j = sub.length; j >= 0; j--) {
      const subArray = [...sub].splice(0, j);
      const sum = subArray.reduce((a, c, i) => {
        return a + c;
      }, 0);
      if (sum > score) {
        winner = sub;
        score = sum;
      }
      console.log(winner, score);
    }
  }
};
