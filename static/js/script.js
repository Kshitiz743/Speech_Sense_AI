let seconds=0;

let timer=null;
let recorder;
let audioChunks = [];


async function startRecording(){
    seconds = 0;

if(timer){
    clearInterval(timer);
}
    document.getElementById(

"recording-status"

).innerHTML="🔴 RECORDING";


document.getElementById(

"recording-message"

).innerHTML=

"AI is Listening Carefully...";


document.getElementById(

"voice-wave"

).style.visibility="visible";



timer=setInterval(function(){


seconds++;


let mins=Math.floor(

seconds/60

);


let secs=seconds%60;



document.getElementById(

"timer"

).innerHTML=

String(mins).padStart(2,"0")

+":"

+

String(secs).padStart(2,"0");


},1000);

    const stream =
    await navigator.mediaDevices.getUserMedia(
        {audio:true}
        );

    recorder = new MediaRecorder(stream);

    audioChunks=[];


    recorder.ondataavailable=(event)=>{

        audioChunks.push(event.data);

    }


    recorder.start();

    alert("Recording Started.");

}



function stopRecording(){
    clearInterval(timer);


document.getElementById(

"recording-status"

).innerHTML=

"✓ RECORDING COMPLETED";


document.getElementById(

"recording-message"

).innerHTML=

"Preparing Audio for Analysis...";


document.getElementById(

"voice-wave"

).style.visibility="hidden";


    recorder.stop();


    recorder.onstop=()=>{


        const audioBlob =

        new Blob(
            audioChunks,
            {type:"audio/webm"}
            );


        const formData = new FormData();


        formData.append(

            "audio",

            audioBlob,

            "speech.webm"

            );



        fetch("/upload",{

            method:"POST",

            body:formData

        })

        .then(response=>response.text())

        .then(data=>{

            document.open();

            document.write(data);

            document.close();

        });


    }


    alert("Recording Stopped.");

}