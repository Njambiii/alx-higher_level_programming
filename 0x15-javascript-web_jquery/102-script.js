function doRequest (val) {
  const url = `https://fourtonfish.com/hellosalut/?lang=${val}`;
  $.ajax({
    url: url,
    method: 'GET'
  }).done(onResponse);
}

function onResponse (data) {
  $('DIV#hello').text(data.hello)
}

function translate () {
  const values = ['es', 'fr', 'en'];
  const inputVal = $('INPUT#language_code').val();
  if (values.includes(inputVal)) {
    doRequest(inputVal);
  }
}

$(document).ready(() => {
  $('INPUT#btn_translate').click(translate);
});
