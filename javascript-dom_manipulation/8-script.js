document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      const salut = document.querySelector('#hello');
      salut.textContent = data.hello;
    });
});
