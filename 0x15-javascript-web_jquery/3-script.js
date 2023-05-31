function color () {
  $('header').addClass('red');
}

$(document).ready(() => {
  $('DIV#red_header').click(color);
});
