uname = d3.select.value("#userName")
uyear = d3.select.value("#userYear")

console.log(data);
// /* data route */
const url = `/api/info?userName=${uname}&userYear=${uyear}`;
d3.json(url).then(function(response) {

  console.log(response);

  

});