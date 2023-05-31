function color () {
  const el = $('HEADER');

  el.toggleClass(function () {
    if (el.hasClass('green')) {
      el.removeClass('green');
      return 'red';
    } else {
      el.removeClass('red');
      return 'green';
    }
  });
}

$(document).ready(() => {
  $('DIV#toggle_header').click(color);
});
