function toggleMenu() {
  const menu = document.querySelector(".menu-links");
  const icon = document.querySelector(".mobile-icon");
  menu.classList.toggle("open");
  icon.classList.toggle("open");
}


// for contact form

const form = document.querySelector('form');

// for contact variable 

const Name = document.getElementById("name");
const email = document.getElementById("email");
const subject = document.getElementById("subject");
const message = document.getElementById("message");


function sendEmail(){
  const bodyMessage =`Full Name :${Name.value}<br> Email: ${email.value}
  <br> Message: ${message.value}`
  Email.send({
    SecureToken:"b2463ca2-2c72-4946-a1a4-597a63a85512",
    // Host : "smtp.elasticemail.com",
    // Username : "techsolvespace@gmail.com",
    // Password:"E2F60FC1CA7D9E9F6BE57A08E48366B621DC",
    //OUTLOOK Password : "C1069284D8D137DAEEE491352920EA2D721F",
    // API:"68C8F52642D68BCB748A728F9241B25E08C8E520F317FBED7220FA60C9816988191801D4F7BA03B95113BF768DE2314E",
    To : 'techsolvespace@gmail.com',
    From : "techsolvespace@gmail.com",
    Subject : subject.value,
    Body : bodyMessage
}).then(
  message =>{
    if(message =="OK"){
      Swal.fire({
        title: "Success!",
        text: "Message sent successfully!",
        icon: "success"
      });
    }
  }
);
}

function checkInputs(){
  const items = document.querySelectorAll(".item");
  for(const item of items){
    if(item.value==""){
      item.classList.add("error");
      item.parentElement.classList.add("error");
    }
    
    if (items[1].value != ""){
      checkEmail();
    }
    items[1].addEventListener("keyup", () =>{
      checkEmail();
  });

    item.addEventListener("keyup", () => {
      if(item.value != ""){
        item.classList.remove("error");
        item.parentElement.classList.remove("error");
      }
      else{
        item.classList.add("error");
        item.parentElement.classList.add("error");
      }
    });
  }

}

function checkEmail(){
  const emailRegex = /^([a-z\d\.-]+)@([a-z\d-]+)\.([a-z]{2,3})(\.[a-z]{2,3})?$/;
  
  if(!email.value.match(emailRegex)){
    email.classList.add("error");
    email.parentElement.classList.add("error");
  }
  else{
    email.classList.remove("error");
    email.parentElement.classList.remove("error");
  }
}


form.addEventListener("submit", (e)=>{
    e.preventDefault();
    checkInputs();

    if (!Name.classList.contains("error") && !email.classList.contains("error") && !subject.classList.contains("error") &&
    !message.classList.contains("error")){
     sendEmail();
     form.reset();
     return false;
    }

    
});

