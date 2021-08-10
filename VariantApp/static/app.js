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
  
  // Error handling
  if (userYear > 2021 | !userYear ) {
    var search = d3.select("h6");
    var variants = d3.select(".variant-list");
    search.html(""); //clear previous text
    variants.html("");  //clear previous text
    search.append("h5").html('Miss Minutes says, "Please enter a<br>4-digit year 2020 or before."');  
  }
  else if (!userName) {
    var search = d3.select("h6");
    var variants = d3.select(".variant-list");
    search.html(""); //clear previous text
    variants.html(""); //clear previous text
    search.append("h5").html('Miss Minutes says, "Please enter your name."');  
  }
  else {
    
    // API call
    const url = `/api/info?userName=${userName}&userYear=${userYear}`;
      
    d3.json(url).then(function(response) {
      console.log(response);
      // Write results to page
      var variants = d3.select(".variant-list");
      var search = d3.select("h6");
      search.html("");
      // Clear previous data
      variants.html("");
      variants.append("h5").html(response.one);   
      variants.append("h6").text("—————————————————————");
      variants.append("h5").html(response.two);
      variants.append("h6").text("—————————————————————");
      variants.append("h5").html(response.three);

    }); //end api call
  
  }  //end else statement

};  //end RunEnter function