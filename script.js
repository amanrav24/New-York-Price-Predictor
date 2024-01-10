document.addEventListener('DOMContentLoaded', function () {
    fetch('../backend/info/columns.json')
    .then(response => response.json())
    .then(data => {
        const drop = document.getElementById('city');

        for(let i = 4; i < data.data_columns.length; i++) {
            const val = data.data_columns[i];
            const option = document.createElement('option');
            const modStr = val[0].toUpperCase() + val.slice(1)
            option.value = val;
            option.textContent = modStr;
            drop.appendChild(option)
        }
    } )
    .catch(error =>console.error('Error', error));
});

function predictionGetter(){
    const bed = document.getElementById('bedrooms').value
    const bath = document.getElementById('bathrooms').value
    const acre_lot = document.getElementById('acre').value
    const house_size = document.getElementById('size').value
    const location = document.getElementById('city').value

    fetch('http://127.0.0.1:5000/predict', {
        method : "POST",
        headers : {"Content-Type" : "application/json"},
        body : JSON.stringify({"bedrooms": bed, "bathrooms" : bath,"acre": acre_lot,"size" : house_size, "city" : location})
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.Price_estimate)
        document.getElementById('price').innerText= "$" + data.Price_estimate
    })



}

 