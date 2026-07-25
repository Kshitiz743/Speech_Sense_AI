let progress = 0;

let percentage = document.getElementById("percentage");

let progressBar = document.getElementById("progress-bar");

let statusText = document.getElementById("status");


const messages = [

"Uploading Audio....",

"Recognizing Speech....",

"Calculating Word Count....",

"Analyzing Speaking Pace....",

"Detecting Pauses....",

"Evaluating Confidence....",

"Performing Tone Analysis....",

"Generating AI Suggestions....",

"Preparing Final Report....",

"Redirecting to Results...."

];


let count = 0;


let loading = setInterval(function(){


    progress += 1;


    percentage.innerHTML = progress + "%";


    progressBar.style.width = progress + "%";


    if(progress==10){

        statusText.innerHTML=messages[0];

    }

    else if(progress==20){

        statusText.innerHTML=messages[1];

    }

    else if(progress==30){

        statusText.innerHTML=messages[2];

    }

    else if(progress==40){

        statusText.innerHTML=messages[3];

    }

    else if(progress==50){

        statusText.innerHTML=messages[4];

    }

    else if(progress==60){

        statusText.innerHTML=messages[5];

    }

    else if(progress==70){

        statusText.innerHTML=messages[6];

    }

    else if(progress==80){

        statusText.innerHTML=messages[7];

    }

    else if(progress==90){

        statusText.innerHTML=messages[8];

    }

    else if(progress==100){

        statusText.innerHTML=messages[9];


        clearInterval(loading);


        setTimeout(function(){

            window.location.href="/analyze";

        },8000);

    }


},80);