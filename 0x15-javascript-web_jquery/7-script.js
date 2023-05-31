function doRequest (url) {
  $.get(url, function (data) {
    $('DIV#character').text(data.name);
  });
}

$(document).ready(() => {
  doRequest('https://swapi-api.hbtn.io/api/people/5/?format=json');
});
