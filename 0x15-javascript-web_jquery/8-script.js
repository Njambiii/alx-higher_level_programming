function doRequest (url) {
  $.get(url, function (data) {
    for (const x in data.films) {
      $.get(data.films[x], function (res) {
        $('UL#list_movies').append($("<li></li>").text(res.title));
      });
    }
  });
}

$(document).ready(() => {
  doRequest('https://swapi-api.hbtn.io/api/people/5/?format=json');
});
