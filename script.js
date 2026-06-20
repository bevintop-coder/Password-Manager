function save(){


let site=
document.getElementById("site").value;


let pass=
document.getElementById("pass").value;



localStorage.setItem(
site,
pass
);



document.getElementById(
"result"
).innerHTML=
"Password Saved";


}
