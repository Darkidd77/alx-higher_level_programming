// Adds an LI element to list when div#add_item tag clicked
//  new element must be <li>Item</li> and must be added to UL.my_list

$('div#add_item').click(function () {
    let element = '<li>Item</li>';
    $('ul.my_list').append(element);
  });