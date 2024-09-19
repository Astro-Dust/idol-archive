getData = () => {
  fetch('http://localhost:8000/get-idols')
    .then((response) => response.json())
    .then((data) => {
		const idolNames = Object.values(data);
		console.log(idolNames);
    })
}

getData();
