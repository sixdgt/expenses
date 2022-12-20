const usernameField = document.querySelector("#usernameField");
const emailField = document.querySelector("#emailField");
const feedBackArea = document.querySelector(".invalid_feedback");
const emailFeedBackArea = document.querySelector(".invalid_email");
const usernameSuccessOutput = document.querySelector('.usernameSuccessOutput');
const passwordField = document.querySelector('#passwordField');
const emailSuccessOutput = document.querySelector('.emailSuccessOutput');
const showPasswordToggle = document.querySelector('.showPasswordToggle');
const submitBtn = document.querySelector('.submit-btn');

const handleToggleInput = (e)=> {
    if(showPasswordToggle.textContent == "SHOW"){
        showPasswordToggle.textContent = "HIDE";
        passwordField.setAttribute("type", "text");
    }else {
        showPasswordToggle.textContent = "SHOW";
        passwordField.setAttribute("type", "password");
    }
};

showPasswordToggle.addEventListener('click', handleToggleInput);

usernameField.addEventListener('keyup', (e)=>{
    const usernameVal = e.target.value;

    usernameSuccessOutput.textContent = `Checking ${usernameVal}`;

    usernameField.classList.remove("is-invalid");
    feedBackArea.style.display = "none";
    usernameSuccessOutput.style.display = "block";
    if (usernameVal.length > 0){
        try{
            fetch("/authentication/validate-username", {
                body: JSON.stringify({ username: usernameVal }),
                method: "POST",
            })
            .then((res) => res.json())
            .then((data) => {
                usernameSuccessOutput.style.display = "none";
                console.log("data", data);
                if(data.username_error){
                    submitBtn.disabled = true;
                    usernameField.classList.add("is-invalid");
                    feedBackArea.style.display = "block";
                    feedBackArea.innerHTML = `<p>${data.username_error}</p>`;
                }else{
                    submitBtn.removeAttribute("disabled");
                }
            });
        }catch(err){
            console.log(err);
        }
    }
});

emailField.addEventListener('keyup', (e)=>{
    const emailVal = e.target.value;
    emailSuccessOutput.textContent = `Checking ${emailVal}`;
    emailField.classList.remove("is-invalid");
    emailFeedBackArea.style.display = "none";
    emailSuccessOutput.style.display = "block";

    if (emailVal.length > 0){
        try{
            fetch("/authentication/validate-email", {
                body: JSON.stringify({ email: emailVal }),
                method: "POST",
            })
            .then((res) => res.json())
            .then((data) => {
                
                emailSuccessOutput.style.display = "none";
                console.log("data", data);
                if(data.email_error){
                    submitBtn.disabled = true;
                    emailField.classList.add("is-invalid");
                    emailFeedBackArea.style.display = "block";
                    emailFeedBackArea.innerHTML = `<p>${data.email_error}</p>`;
                }else{
                    submitBtn.removeAttribute("disabled");
                }
            });
        }catch(err){
            console.log(err);
        }
    }
});