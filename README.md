# ATLA-Line-Visualization

inspired by this Reddit post:
https://www.reddit.com/r/dataisbeautiful/comments/g2f3ip/oc_most_popular_movie_genre_combinations

Avatar: The Last Airbender was released on US Netflix on May 15, 2020. This just so happens to align with the end of finals for me, so I've decided to rewatch it and see what combinations of characters had the most lines spoken to each other and model them in a fun, interactive way.

I identified the following characters as important enough to be counted:

Aang, Katara (including when in disguise as the Painted Lady), Sokka, Toph, Zuko (including when in disguise as the Blue Spirit), Iroh, Suki, Azula, Ozai, Mai, and Ty Lee (Sorry to all the Boomy, Gran-Gran, and Sozin fans out there)

For the purposes of this project, I defined a line of dialouge as a block of speech spoken by one character to another, unbroken by: the interuption of the block by another character speaking (including the person the speaker is talking to), the speaker switching the addresse of their speaking, a scene change, or the end of an episode.

Lines spoken from a character not listed to one that is (and vice versa) are not counted.

Lines spoken during dream sequences/flashbacks/episode recaps are not counted.

Notable edge cases:

107; Winter Solstice Part 1- The Spirit World: Aang tries the talk to Katara when he's in the spirit world, but she can't hear him. The first line was counted, since he thought he was in conversation; subsequent lines were not.

112; The Storm: Iroh's story to the Lieutenant portrays dialouge amongst himself, Zuko, and Ozai. These lines are not counted.

120; The Siege of the North- Part 2: Zuko directly addresses Aang's body while he is in the spirit world. I don't consider this dialouge, so I didn't count these lines.

204; The Swamp: Aang tries to talk to the swamp vision of Toph. Since this isn't really Toph, I didn't count these lines.

207; Zuko Alone: This episode famously features no important characters but Zuko, apart from flashbacks featuring himself, Azula, Mai, Ty Lee, and Ozai. I didn't want to put an empty document through the program so I just didn't make a file for this episode.
