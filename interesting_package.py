# Wikipedia

import wikipedia

print(wikipedia.summary("Wikipedia"))
print(wikipedia.search("Barack"))
print(wikipedia.search("Moldova"))

ny = wikipedia.page("New York City")
print(ny.title)
print(ny.url)
print(ny.content)
print(ny.links[1])

wikipedia.set_lang("ru")
print(wikipedia.summary("Facebook", sentences=1))
