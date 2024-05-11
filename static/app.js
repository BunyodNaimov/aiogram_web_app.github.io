let tg = window.Telegram.WebApp

tg.expand();

tg.MainButton.textColor = '#FFFFFF';
tg.MainButton.color = '#2cab37';

let r_name = ""
let r_price = ""


let rmv_btn = document.getElementById("rmv_btn");
let add_btn = document.getElementById("add_btn");
let num = document.getElementById("num");
let count_num = 0;


add_btn.addEventListener("click", function () {
    num.innerText = count_num += 1;
})
rmv_btn.addEventListener("click", function () {
    num.innerText = count_num -= 1;
})

function func(name, price) {
    add_btn.style.display = "none";
    add_btn.style.display = "inline-block";
    rmv_btn.style.display = "inline-block";
    num.style.display = "inline-block";
    tg.MainButton.setText(name);
    r_name = name;
    r_price = price;
    tg.MainButton.show();
}


Telegram.WebApp.onEvent("mainButtonClicked", function () {
    tg.sendData(r_name + "/" + r_price);
});


let usercard = document.getElementById("usercard");

let p = document.createElement("p");

p.innerText = `${tg.initDataUnsafe.user.first_name}
${tg.initDataUnsafe.user.last_name}`;

usercard.appendChild(p);








