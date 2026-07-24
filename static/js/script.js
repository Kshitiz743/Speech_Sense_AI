let recorder;
let audioChunks = [];


async function startRecording(){

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