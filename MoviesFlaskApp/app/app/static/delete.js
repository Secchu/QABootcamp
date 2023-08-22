function deleteEntity(id, link, entity)
{
	let acknowledge = confirm('You are about to delete ' + entity + '. All data related to ' 
	+ entity + ' on this movie will also be deleted. Please confirm')
	
	if(!acknowledge)
		return false
	
	let response = SendRequest(link)
	
	let spantag = document.getElementById(id)
	
	alert(response)
	spantag.innerHTML = "<h3 class='header'>" + response + "</h3>"
	
	return true
	
}

function SendRequest(link)
{
	const xhttp = new XMLHttpRequest()
	
	//We have to set this to async to false. Otherwise we get blank output.
	xhttp.open('GET', link, false)
	
	xhttp.send()
	
	response = xhttp.responseText
	
	return response
}

function deleteAndHideRow(rowid, link, entity, removeEntity)
{
	let ack = confirm('You are about to remove ' 
	+ entity + ' from ' + removeEntity + 
	'. All data related to ' + entity + ' on this movie will also be deleted. Please confirm')
	
	if(!ack)
		return false
	
	let response = SendRequest(link)
	
	let row = document.getElementById(rowid)
	
	row.style.display = "none"
	
	alert(response)
}