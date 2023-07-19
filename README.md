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

**Other Items:** Overdrive and use of Hyper Speed as unlockables.

**Victory Condition:** Up in the air, but focused around songs in Tier 6. Whether it's an FC goal (such as 20 Tier 6 FCs) or a Star goal (50 Stars from Tier 6), it can be dependant on your skill level and time commitment.

**Notes:** Implementation of this is pretty basic, which makes it compatible with other RB2-related games with the same setlist, such as RB3 or YARG. There are six Progressive Tier unlocks that unlock each tier past the very first tier (0 dot) and allow you to play the songs that are contained within the unlocked tiers. All of the tiering is based off of the band tier from Rock Band 2 - this tiering may differ if you decide to play this in a different game other than RB2, such as RB3, YARG, or Clone Hero. In that case, refer to the tiering listed in the "Items Received" section of the Manual client.
