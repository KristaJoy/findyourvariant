var button = d3.select("#buttontext");

// Create event handlers 
button.on("click", runEnter);

// Function on click event
function runEnter() {

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var input_name = d3.select(".userName");
  var input_year = d3.select(".userYear");

  // Value of the input element
  var userName = input_name.property("value");
  var userYear = input_year.property("value");

  console.log(userName);
  console.log(userYear);

  // API call
  const url = `/api/info?userName=${userName}&userYear=${userYear}`;
  
  d3.json(url).then(function(response) {
    console.log(response);
    // Write results to page
    var variants = d3.select(".variant-list");
    
    // Clear previous data
    variants.html("");

    variants.append("p").text(response.one);   
    variants.append("p").text(response.two);
    variants.append("p").text(response.three);


  });


};