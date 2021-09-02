$(document).ready(function() {
    if (navigator.geolocation)
    {
        navigator.geolocation.getCurrentPosition(successFunction, errorFunction);
    }
    else 
    {
       null
    }   
})

function successFunction(position) 
{
    var lat = position.coords.latitude;
    var long = position.coords.longitude;
    const pos = `Latitude: ${lat} + Longitude: ${long}`
    $.ajax({
        type: "POST",
        url: "/postmethod",
        contentType: "application/json",
        data: JSON.stringify({location: pos}),
        dataType: "json",
        success: function(response) {
        },
        error: function(err) {
            console.log(err);
        }
    });
}

function errorFunction(position) 
{
    alert('Error!');
}
// locate();