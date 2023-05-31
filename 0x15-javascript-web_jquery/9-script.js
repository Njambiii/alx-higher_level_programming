const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
function onResponse (data) {
  $('DIV#hello').text(data.hello)
}

$(document).ready(() => {
  $.ajax({
    url: url,
    method: 'GET'
  }).done(onResponse);
});
