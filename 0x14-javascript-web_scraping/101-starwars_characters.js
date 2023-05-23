#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
function recur (array, i) {
  if (i >= array.length) return;
  request.get(array[i], function (error2, response2, body2) {
    console.log(JSON.parse(body2).name);
    recur(array, i + 1);
  });
}
request.get(url, function (error, response, body) {
  if (error) console.log(error);
  else {
    recur(JSON.parse(body).characters, 0);
  }
});
