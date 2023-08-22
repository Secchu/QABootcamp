//Working. Just pass in the lstbox. Parameter are strings of the lstbox item. text and value
//would be the same.
function addSelectValue(lstBox, value)
{
    var option = document.createElement("OPTION");
    option.text = value;
    option.value = value;
	option.selected = true
    lstBox.options.add(option);
}

/*
copySelected() copies fromLstBox to toListBox. Both are id of the listboxes.
*/

function copySelected(fromLstbox, toListbox)
{
    let srcBox = document.getElementById(fromLstbox)

    let dstBox = document.getElementById(toListbox)

	let lastIndex = srcBox.options.length-1

    for(var i=lastIndex; i>=0; i--)
    {
        let selected = srcBox[i].selected;
        if(selected)
        {
            addSelectValue(dstBox, srcBox[i].value)
            srcBox.remove(i)
        }
    }
    
}
    
//Moves all options from fromLstBox to toLstBox by adding the option to toLstBox then removing the 
//option on fromLstBox. For this to work we must iterate on fromLstBox in reverse order as we 
//are removing options from fromLstBox and each removal will make the array smaller therefore
//it is important we start from the top.  
function moveAll(fromLstbox, toListbox)
{
    let srcBox = document.getElementById(fromLstbox)

    let dstBox = document.getElementById(toListbox)
	
	let lastIndex = srcBox.options.length-1

    for(var i=lastIndex; i>=0; i--)	
        addSelectValue(dstBox, srcBox[i].value);
    
    copyAll(srcBox);
}

//Working. Just passing in the lstbox.
function copyAll(select_id)
{
    for(var i=select_id.options.length-1;i>=0;i--)
		select_id.remove(i)
}

function stopDeselection(listBox_id)
{
	listBox = document.getElementById(listBox_id)
	
	for(var i=0; i<listBox.length; i++)
		listBox[i].selected = true
}