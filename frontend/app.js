function showMenu(){

    document
        .getElementById("homePage")
        .classList.add("hidden");

    document
        .getElementById("dashboard")
        .classList.remove("hidden");

}


function exitApp(){

    alert("Thank you for using SentinelAI!");

}


function showModule(module){

    document
        .getElementById("moduleTitle")
        .innerHTML = module + " Detection";


    let form = "";


    if(module === "Internship"){

        form = `
        <h2>Internship Fraud Detection</h2>

        <input type="text" placeholder="Company Name">

        <input type="email" placeholder="Email">

        <input type="text" placeholder="Salary">

        <input type="text" placeholder="Website URL">

        <button class="analyze-btn">
            Analyze
        </button>
        `;
    }


    else if(module === "Job"){

        form = `
        <h2>Job Fraud Detection</h2>

        <input type="text" placeholder="Company Name">

        <input type="email" placeholder="Email">

        <input type="text" placeholder="Salary">

        <button class="analyze-btn">
            Analyze
        </button>
        `;
    }


    else if(module === "Email"){

        form = `
        <h2>Email Phishing Detection</h2>

        <input type="text" placeholder="Subject">

        <input type="email" placeholder="Sender Email">

        <textarea rows="6"
        placeholder="Paste email content"></textarea>

        <button class="analyze-btn">
            Analyze
        </button>
        `;
    }


    else if(module === "SMS"){

        form = `
        <h2>SMS Scam Detection</h2>

        <textarea rows="6"
        placeholder="Paste SMS message"></textarea>

        <button class="analyze-btn">
            Analyze
        </button>
        `;
    }


    else if(module === "Website"){

        form = `
        <h2>Website Fraud Detection</h2>

        <input type="text"
        placeholder="Enter Website URL">

        <button class="analyze-btn">
            Analyze
        </button>
        `;
    }


    else if(module === "WhatsApp"){

        form = `
        <h2>WhatsApp Scam Detection</h2>

        <textarea rows="6"
        placeholder="Paste WhatsApp message"></textarea>

        <button class="analyze-btn">
            Analyze
        </button>
        `;
    }


    else if(module === "QR Code"){

        form = `
        <h2>QR Code Detection</h2>

        <input type="file">

        <button class="analyze-btn">
            Analyze
        </button>
        `;
    }


    else if(module === "Image"){

        form = `
        <h2>Image Deepfake Detection</h2>

        <input type="file">

        <button class="analyze-btn">
            Analyze
        </button>
        `;
    }


    else if(module === "Video"){

        form = `
        <h2>Video Deepfake Detection</h2>

        <input type="file">

        <button class="analyze-btn">
            Analyze
        </button>
        `;
    }


    document
        .getElementById("inputArea")
        .innerHTML = form;

}
