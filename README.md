# rockband2manualAP

Implementation of Rock Band 2 into Archipelago Manual

**Game:** Rock Band 2

**Options:**

- `exclude_instruments`:
  Array of instruments to exclude. Select from ["Bass", "Drums", "Guitar", "Vocals"]. Only 2 instruments can be excluded without generation failures.
- `starting_songs`:
  Number of Tier 0 songs to start with. Can be any value between 1 and 12 (inclusive).

**Checks:** Each chart from each instrument from every song in the game.

**Key Items:** Song unlocks and Progressive Tier unlocks.

**Other Items:** Use of Overdrive, various traps involving lefty flip (or righty if you are a lefty!), performance mode and use of (or lack of) hyper speed. Filler includes Fans, Money, and various unlockables/characters from RB2.

**Victory Condition:** Since RB2 doesn't exactly have a real victory condition, the one I have made up is getting a certain percentage of the Stars available from songs in Tier 6. I calculate the number of stars using a formula: `[percentage] * 72 Stars * [# of instruments`. This scales the number of stars required to how many instruments you are playing in your seed. **This also counts achieving Gold Stars as collecting 6 Stars.** These are all stars collected from each instrument from Tier 6 songs.

For example, if I wanted 50% of the stars and I was playing with all four instruments, my goal would be to collect 50% * 72 * 4 = 144 stars from Tier 6. 

Obviously, since this is just my suggestion, you are free to create your own goal, whether that is stars, completing a certain number of songs, getting a number of FCs, etc.

**Notes:** Implementation of this is pretty basic, which makes it compatible with other RB2-related games with the same setlist, such as RB3 or YARG. There are six Progressive Tier unlocks that unlock each tier past the very first tier (0 dot) and allow you to play the songs that are contained within the unlocked tiers. All of the tiering is based off of the band tier from Rock Band 2 - this tiering may differ if you decide to play this in a different game other than RB2, such as RB3, YARG, or Clone Hero. In that case, refer to the tiering listed in the "Items Received" section of the Manual client.

I also do not suggest doing this in a synchronous AP game - due to the nature of the game, this is very likely to take a long time and is much, MUCH better suited for an async scenario. Your choice, though!
