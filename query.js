$(document).ready(function() {
    // Fetch data from an API
    $.get("https://example.com/api/data", function(data) {
      // Update the contents of the info box with the fetched data
      $(".info-box").html(data.message);
    });
  });
  