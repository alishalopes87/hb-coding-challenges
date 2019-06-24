# kit.imgix.net/products/32/06/awesome21-basic-cott-3206667a49a70fbce00aa8bac7a38209.png?auto=enhance,compress&bg=ffffff&cs=tinysrgb&fit=fill&fm=webp&h=250&pad=60&trim=color&w=250

# mec.imgix.net/medias/sys_master/high-res/high-res/8809969549342/4015090-NOC02.jpg?bg=FFF&fit=fill&fm=webp&h=300&q=40&w=300

# vhx.imgix.net/worldofwonder/assets/66d4e631-a65a-45cd-933e-40b07f3f37f8-ea6333ad.png?fit=crop&fm=jpg&h=135&w=240

# stz1.imgix.net/web/contentId/39936/type/Key/dimension/1536x2048?q=50&w=230

# iwdev.imgix.net/12220151537178.jpg?fit=crop&fm=pjpg&h=150&q=80&usm=10&w=300

# busbud.imgix.net/busbud-logos/busbud_logo.svg?auto=compress

# daysto.imgix.net/backgrounds/blurred/4.jpg?auto=compress&fit=crop&h=768&q=25&w=1366

# imgix.bustle.com/lovelace/uploads/448/d607a850-902b-0134-ce63-0aec1efe63a9.jpg?fit=max&fm=webp&q=70&w=646

def param_count(link):

	count={}

	query = link.index("?")
	#need to find actual index of ? to slice on 

	link_list = link[query+1:]

	link_list = link_list.split("=")

	#cannot split again on list so iterate over strings in list and split on each
	#append to result list 
	result = []
	for link in link_list:
		link = link.split("&")
		result.extend(link)

	for param in range(len(result)):
		if param % 2 == 0:
			count[result[param]] = count.get(result[param], 0) + 1

	return count   

print(param_count("imgix.bustle.com/lovelace/uploads/448/d607a850-902b-0134-ce63-0aec1efe63a9.jpg?fit=max&fm=webp&q=70&w=646"))