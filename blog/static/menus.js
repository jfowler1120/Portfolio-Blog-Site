let mainmenu = document.getElementById("navdropdownbutton")
let content = document.getElementById("2")
let background = document.getElementById("1")
let menuopened = false;

let usermenu = document.getElementById("userdropdownbutton")
let usercontent = document.getElementById("U2")
let userbackground = document.getElementById("U1")
let usermenuopened = false;



mainmenu.addEventListener("click", () => {
    if (menuopened == false) {
        menuopened = true
        content.style.position = "relative";
        content.style.display = "inline-block";
        content.style.width = "200px";
        content.style.height = "fit-content";
        content.style['font-size'] = "1.5em";
        content.style['z-index'] = "15";
        content.style.top = "-10px";
        content.style['padding-top'] = "30px";
        content.style['padding-bottom'] = "30px";
        content.style['padding-right'] = "30px";

        background.style.display = "block";
        background.style.position = "absolute";
        background.style['background-color'] = "rgb(244, 244, 244)";
        background.style.width = "160px";
        background.style.height = "140px";
        background.style.float = "left";
        background.style['z-index'] = "auto";
        background.style.top = "67px";
        background.style['box-shadow'] = "2px 2px 2px rgb(180, 180, 180)";
        background.style['border-radius'] = "5%";
    } else {
        menuopened = false;
        content.style.display = "none";
        background.style.display = "none";
    }
    
})

usermenu.addEventListener("click", () => {
    if (usermenuopened == false) {
        usermenuopened = true
        usercontent.style.position = "relative";
        usercontent.style.display = "inline-block";
        usercontent.style.width = "0px";
        usercontent.style.height = "fit-content";
        usercontent.style['font-size'] = "1.5em";
        usercontent.style['z-index'] = "15";
        usercontent.style.top = "-10px";
        usercontent.style.right = "100px";
        usercontent.style['padding-top'] = "30px";
        usercontent.style['padding-bottom'] = "30px";
        usercontent.style['padding-right'] = "30px";

        userbackground.style.display = "block";
        userbackground.style.position = "absolute";
        userbackground.style['background-color'] = "rgb(244, 244, 244)";
        userbackground.style.width = "160px";
        userbackground.style.height = "140px";
        userbackground.style.float = "left";
        userbackground.style['z-index'] = "auto";
        userbackground.style.top = "55px";
        userbackground.style.right = "-45px";
        userbackground.style['box-shadow'] = "2px 2px 2px rgb(180, 180, 180)";
        userbackground.style['border-radius'] = "5%";
    } else {
        usermenuopened = false;
        usercontent.style.display = "none";
        userbackground.style.display = "none";
    }
    
})