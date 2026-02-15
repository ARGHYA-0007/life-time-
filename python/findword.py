with open("find.txt","w") as f:
    f.write("""In the small town of Glenridge, the arrival of spring always brought a sense of renewal. The trees, once bare and skeletal against the gray winter sky, began to bloom with vibrant shades of green, while the flowers pushed their delicate heads through the damp soil, creating patches of color across the fields. Children ran freely along the winding paths that cut through the meadows, their laughter mingling with the soft murmur of the nearby river. Farmers tended to their gardens with renewed energy, planting seeds they hoped would grow into bountiful crops over the coming months. Even the townsfolk who preferred quieter days found themselves drawn outdoors, taking long walks to soak in the warmth of the sun and the gentle breeze that carried the scent of fresh grass and blossoms.

One afternoon, an unexpected delivery arrived at the local library. Among the stacks of books that chronicled history, science, and fiction was a single, heavy volume with a title that caught the eye of the town’s young readers: a guide to learning Python. Though most had never considered programming, the idea of exploring a new world through the language of computers sparked curiosity and excitement. Conversations about algorithms and coding puzzles soon replaced the usual debates over gardening techniques and local gossip. The presence of this single book reminded everyone that learning could take many forms, and that even in a town defined by tradition, new ideas could flourish alongside old customs.

As the days lengthened and the town awoke fully from its winter slumber, people discovered that the world around them seemed richer. Birds returned to the rooftops, the river swelled with snowmelt, and the simple act of stepping outside brought a sense of wonder that could not be ignored. And somewhere, tucked in a corner of the library, that one Python book waited, quietly opening doors for anyone curious enough to pick it up and take the first step into a new adventure.""")
with open("find.txt") as f:
    i=f.read()
    if("python" in i.lower()):
        print("yes")
    else:
        print("no")