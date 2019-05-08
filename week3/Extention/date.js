time();
moment();
function time(){
    var date = new Date();
    var dd = date.getDate();
    var mm = date.getMonth() + 1;
    var y = date.getFullYear();
    var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    var someDate = dd + ' '+ months[mm-1] + ' '+ y;
    var dat = document.getElementById("date");
    dat.innerHTML = someDate;
    
}
function moment(){
    var date = new Date();
    var h = date.getHours();
    var m = date.getMinutes();
    var moment = document.getElementById("moment");
    if(h<9)
    {
        h ='0'+ h;
    }
    if(m<9)
    {
        m ='0'+m;
    }
    var mom = h + ':' + m;
    moment.innerHTML = mom;
}