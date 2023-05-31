function color () {
  $('header').css('color', '#FF0000');
}

$(document).ready(() => {
  $('DIV#red_header').click(color);
});
