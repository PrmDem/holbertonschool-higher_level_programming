const addBtn = document.querySelector('#add_item');
const ul = document.querySelector('.my_list');
addBtn.addEventListener('click', () => {
  const li = document.createElement('li');
  li.appendChild(document.createTextNode('Item'));
  ul.appendChild(li);
});
