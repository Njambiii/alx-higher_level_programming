function updateHeader () {
  $('HEADER').text('New Header!!!');
}

$(document).ready(() => {
  $('DIV#update_header').click(updateHeader);
});
