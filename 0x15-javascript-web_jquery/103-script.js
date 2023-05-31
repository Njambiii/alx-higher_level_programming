const values = ['es', 'fr', 'en'];

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
  const inputVal = getInputVal();
  if (values.includes(inputVal)) {
    doRequest(inputVal);
  }
}

function getInputVal () {
  return $('INPUT#language_code').val();
}

function keyPress (ev) {
  const key = ev.which;
  if (key == 13) {
    translate();
  }
}

$(document).ready(() => {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').keypress(keyPress);
});
