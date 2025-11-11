const toggleHead = document.querySelector('#toggle_header');
toggleHead.addEventListener('click', () => {
  const redClass = toggleHead.classList.contains('red');
  toggleHead.classList.toggle('red', !redClass);
  toggleHead.classList.toggle('green', redClass);
});
