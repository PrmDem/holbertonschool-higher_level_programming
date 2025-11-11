fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    const charas = document.querySelector('#character');
    charas.textContent = `${data.name}`;
  });
