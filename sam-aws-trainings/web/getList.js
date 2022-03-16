/*
function getList() {
    const form = document.getElementById('getcategory');
    const category = form.elements['category'];

    // getting the element's value
    let categoryName = category.value;
    alert(categoryName);   
}
*/

async function postData(data = {}){
    // Default options are marked with *
    // alert(data.CategoryName);
    // alert(JSON.stringify(data));
    const response = await fetch('https://j7xmn2nv1k.execute-api.eu-central-1.amazonaws.com/dev-stage/courses', {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
        'Content-Type': 'application/json'
        // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(data) // body data type must match "Content-Type" header
        // body: data
    });
    // alert(response.json().CategoryName); 
    return response.json(); // parses JSON response into native JavaScript objects
}

const form = document.getElementById('getcategory');
const courseName = document.getElementById('courselist');

form.addEventListener("submit", function (event) {
	// stop form submission
	event.preventDefault();
    const category = form.elements['category'];
    const categoryName = category.value;
    // alert(categoryName);   
    const param = {CategoryName: categoryName};
    postData(param)
    .then(response => {
        courseName.innerHTML = response.CategoryName;
        // console.log(data); // JSON data parsed by `data.json()` call
    });
    // let result = postData(param);
    // alert(result);
    // courseName.innerHTML = postData(param);
});
