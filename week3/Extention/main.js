$('#tdl').keypress(function(e) {

    if(e.which==13){
        Create();
    }
});



function Create()
{
    var task = document.createElement("div");
    task.className = 'task';
//-------------------------------------
    var task_text = document.getElementById('tdl').value;
    if(task_text===''||task_text===' ')
    {
        return;
    }
    
    var text = document.createElement("div");
    text.className = 'textt';

    var ttext = document.createElement("p");
    ttext.innerHTML = task_text;
    ttext.className = 'notdoneyet';
    text.appendChild(ttext);
    document.getElementById('tdl').value = '';

 //----------------------------   
    var check = document.createElement('div');
    check.className = 'check';

    var checkBox = document.createElement('input');
    checkBox.type = 'checkbox';
    
    check.appendChild(checkBox);
    
    checkBox.onclick = function action(){
        var t = this.parentElement.parentElement.getElementsByClassName('textt')[0].firstChild;
        
        if(this.checked)
        {
            t.className = 'done';
        }
        else 
        {
            t.className = 'notdoneyet';
        }
    }
//------------------------------------
    var deletion = document.createElement("div");
    deletion.className = 'dele';
    var btn = document.createElement("button");

    var btn_img = document.createElement("img");
    btn_img.src = "./res/delete.png";
    btn.onclick = function del()
    {
        this.parentElement.parentElement.remove();
    }
    btn.appendChild(btn_img);
    deletion.appendChild(btn);
//--------------------------------
    

    task.appendChild(check);
    task.appendChild(text);
    
    task.appendChild(deletion);
//----------------------------------------
    var list = document.getElementById('contb');
    list.appendChild(task);    
}
