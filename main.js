

function Clicked_Bad(name)
{
    alert("Letting " + name + " know you are on your way!");
}

function Clicked_Repair(name)
{
    var ajax = new XMLHttpRequest();
    var header = document.getElementById("Header1");

    // set up anonymous function to be called when the
    //    request is completed
    /*
    ajax.onreadystatechange =
        function () {
            if (ajax.readyState == 4) {
                if (ajax.status == 200) {
                    header.innerHTML = ajax.responseText;
                    alert("Ajax Response: " + ajax.responseText);
                }
                else {
                    alert("No response");
                }
            }
        };
        */
    ajax.open("GET",
              "php_functions.php?name=" + name,
        true);

    ajax.send(null);
}