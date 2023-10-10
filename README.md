# ValorantBindPath
Generate a path for attackers on Bind for the Valorant map. 

BindPath is a Python application that assists in generating random paths 
and suggesting strategies for the game Valorant, specifically focusing on
the map Bind. The application starts by allowing users to choose a 
starting and ending point. The first three steps of the generated path 
are random with weighted edges, followed by utilizing Breadth-First Search 
(BFS) to reach the designated site.

Bind stands out as a unique map due to its unidirectional aspects, 
notably the Teleporters on both A and B sides, setting it apart from 
all other maps that are entirely bidirectional in terms of pathways.
