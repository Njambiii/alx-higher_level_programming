function updateList () {
  const item1 = $('<li></li>').text('Item');
  $('UL.my_list').append(item1);
}

$(document).ready(() => {
  $('DIV#add_item').click(updateList);
});
