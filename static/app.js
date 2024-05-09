let tg = window.Telegram.WebApp

tg.expand();

tg.MainButton.textColor = '#FFFFFF';
tg.MainButton.color = '#2cab37';

let r_name = ""
let r_price = ""
function func(name, price) {
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








