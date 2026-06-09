function showMenu(){

    document
        .getElementById("homePage")
        .classList.add("hidden");

    document
        .getElementById("menuPage")
        .classList.remove("hidden");

}

function exitApp(){

    alert("Thank you for using SentinelAI!");

}

function detect(type){

    alert(type + " module selected.");

}
