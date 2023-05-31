function addItem () {
  const item = $("<li></li>").text('Item');
  $('UL.my_list').append(item);
}

function removeItem () {
  $("UL.my_list LI:last-child").remove();
}

function clearList () {
  $("UL.my_list > LI").remove();
}

$(document).ready(() => {
  $('DIV#add_item').click(addItem);
  $('DIV#remove_item').click(removeItem);
  $('DIV#clear_list').click(clearList);
});
